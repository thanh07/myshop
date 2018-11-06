from django.forms import ModelForm
from .models import Category

class CategoryForm(ModelForm):
	class Meta:
		model = Category
		fields = ['name', 'slug']
		"""docstring for Metaf __init__(self, arg):
		model = Category
		fields = ['name', 'slug']
			super(Meta__init__()
			model = Category
			fields = ['name', 'slug']
			self.arg = arg
			
