import sys
from django.db import models
from django.urls import reverse
# =============
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile

class Category(models.Model):
	name = models.CharField(max_length=200,
		db_index=True)
	slug = models.SlugField(max_length=200,
		unique=True)
	
	class Meta:
		ordering = ('name',)
		verbose_name = 'category'
		verbose_name_plural = 'categories'
		
	def __str__(self):
			return self.name

	def get_absolute_url(self):
		return reverse('shop:product_list_by_category',	args=[self.slug])

# Create your models here.
class Product(models.Model):
	category = models.ForeignKey(Category,
		related_name='products',
		on_delete=models.CASCADE)
	name = models.CharField(max_length=200, db_index=True)
	slug = models.SlugField(max_length=200, db_index=True)
	image = models.ImageField(upload_to='products/%Y/%m/%d',
		blank=True)
	description = models.TextField(blank=True)
	purchase = models.DecimalField(max_digits=10, decimal_places=2)
	wholesale = models.DecimalField(max_digits=10, decimal_places=2)
	block_price = models.DecimalField(max_digits=10, decimal_places=2)
	retail = models.DecimalField(max_digits=10, decimal_places=2)
	available = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ('name',)
		index_together = (('id', 'slug'),)
	
	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('shop:product_update', args=[self.slug])

	def save(self, *args, **kwargs):
		#Opening the uploaded image
		im = Image.open(self.image)

		output = BytesIO()
		#Resize/modify the image
		im = im.resize( (400,400) )
		#after modifications, save it to the output
		im.save(output, format='JPEG', quality=50)
		output.seek(0)
		#change the imagefield value to be the newley modifed image value
		self.image = InMemoryUploadedFile(output,'ImageField', "%s.jpg" %self.image.name.split('.')[0], 'image/jpeg', sys.getsizeof(output), None)
		super(Product, self).save(*args, **kwargs)

			