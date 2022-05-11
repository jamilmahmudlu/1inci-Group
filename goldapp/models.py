from django.db import models
from autoslug import AutoSlugField
from django.contrib.auth.models import User
# Create your models here.

# Slider
class Slider(models.Model):
	title = models.CharField(max_length=150, verbose_name='Title')
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	slideimg = models.FileField(upload_to = "slide/", verbose_name='Slide image')

	class Meta:
		verbose_name = "Slider"
		verbose_name_plural = 'Sliders'

	def __str__(self):
		return self.title

# partnyor
class Partnyor(models.Model):
	title = models.CharField(max_length=150, verbose_name='Title')
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	partnyorimg = models.FileField(upload_to = "partimg/", verbose_name='Partnyor Image')

	class Meta:
		verbose_name = "Partnyor"
		verbose_name_plural = 'Partnyors'

	def __str__(self):
		return self.title

# cataegory
class Category(models.Model):
    parent = models.ForeignKey('self', related_name='children', on_delete=models.CASCADE, blank = True, null=True, verbose_name='Parent')
    title = models.CharField(max_length=100, verbose_name='Title') 
    slug = AutoSlugField(populate_from='title', unique=True, null=False, editable=False, verbose_name = 'Slug')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.title

    class Meta:
        unique_together = ('slug', 'parent',)
        verbose_name_plural = "categories"     
	# iç içə kateqoriya
    def __str__(self):                           
        full_path = [self.title]                  
        k = self.parent
        while k is not None:
            full_path.append(k.title)
            k = k.parent
        return ' -> '.join(full_path[::-1])  


# Product
class Product(models.Model):
	category = models.ForeignKey(Category, on_delete = models.CASCADE, verbose_name='Category')
	name = models.CharField(max_length = 100, verbose_name='Name')
	slug = models.SlugField(max_length=100, db_index=True, verbose_name='Slug')
	price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Price')
	productimg = models.FileField(upload_to = "productimg/", verbose_name='Product image')
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	status = models.IntegerField(default=0)
	description = models.TextField(blank=True, verbose_name='Description')
	is_concrete = models.BooleanField(verbose_name='Concrete', default=False)

	class Meta:
		verbose_name = "Product"
		verbose_name_plural = "Products"

	def __str__(self):
	    return 'name={0}, category={1}'.format(self.name, self.category)

# Images
class Images(models.Model):
	product=models.ForeignKey(Product,on_delete=models.CASCADE, verbose_name='Product')
	title = models.CharField(max_length=50, verbose_name='Title')
	productimg=models.FileField(upload_to="productimg/", verbose_name='Product image')

	class Meta:
		verbose_name = "Image"
		verbose_name_plural = "Images"

	def __str__(self):
		return self.title

class ProductSlider(models.Model):
	title = models.CharField(max_length=150, verbose_name="Title")
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	prodslideimg = models.FileField(upload_to = "slide/", verbose_name="Product Slide Image")

	verbose_name = "Product Slider"
	verbose_name_plural = "Product Sliders"

	def __str__(self):
		return self.title

class ContactUs(models.Model):
	first_name = models.CharField(max_length=255, verbose_name='First Name', help_text='Max 255 character')
	email = models.EmailField(verbose_name='Email Address')
	telephone = models.CharField(max_length=20)
	message = models.TextField(verbose_name='Message')

	verbose_name = "Contact Us"
	verbose_name_plural = "Contact Us"

	def __str__(self):
		return self.first_name

