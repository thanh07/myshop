from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Product
from django.forms import ModelForm
from django.forms import DateTimeField



class CategoryForm(ModelForm):
	class Meta:
		model = Category
		fields = ['name', 'slug']

class ProductForm(ModelForm):
	class Meta:
		model = Product
		fields = ['name', 'slug','category','image','description','purchase','wholesale','block_price',
		'retail','available',]


	 # start_date  = forms.DateField(widget=DateTextInput(format='d/m/y'), input_formats=('%d/%m/%y',))

# Create your views here.
def category_list(request):
	categories = Category.objects.all()
	return render(request,'shop/category/list.html',{'categories':categories})

def category_new(request):
	form = CategoryForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('shop:category_list')
	return render(request,'shop/category/form.html',{'form':form})

def category_update(request, slug):
	category = get_object_or_404(Category, slug=slug)
	form = CategoryForm(request.POST or None, instance = category)
	if form.is_valid():
		form.save()
		return redirect('shop:category_list')
	return render(request,'shop/category/form.html',{'form':form})


def product_list(request, category_slug = None):
	category = None
	categories = Category.objects.all()
	products = Product.objects.filter(available=True)
	if category_slug:
		category = get_object_or_404(Category, slug=category_slug)
		products = products.filter(category=category)
	return render(request,
			'shop/product/list.html',
			{'category': category,
			'categories': categories,
			'products': products})

def product_new(request):
	if request.method =='POST':
		form = ProductForm(request.POST, request.FILES)
		if form.is_valid():
			p = form.save(commit=False)
			p.image = request.FILES['image']
			p.save()
	else:
		form = ProductForm()
	return render(request,'shop/product/form.html',{'form':form})

# def product_detail(request,slug):
# 	product = get_object_or_404(Product, slug = slug)
# 	return render(request, 'shop/product/detail.html',{'product':product})

def product_update(request,slug):
	product = get_object_or_404(Product, slug = slug)
	form = ProductForm(request.POST or None, instance = product)
	if form.is_valid():
		p = form.save(commit=False)
		p.image = request.FILES['image']
		p.save()
		return redirect('shop:product_list')
	return render(request, 'shop/product/form.html',{'form':form})
	# product = get_object_or_404(Product, slug = slug)
	# form = ProductForm(request.POST or None, instance = product)
	# if form.is_valid():
	# 	p = form.save(commit = False)
	# 	p.save()
	# 	return redirect('shop:product_list')
	# return render(request, 'shop/product/form.html',{'form':form})
def product_delete(request,slug):
	product = get_object_or_404(Product, slug = slug)
	
	if request.method =='POST':
		product.delete()
		return redirect('shop:product_list')
	return render(request, 'shop/product/confirm_delete.html',{'object':product})