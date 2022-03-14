from itertools import product
from django.db import models
from autoslug import AutoSlugField
from django.contrib.auth.models import User
# Create your models here.

# Slider
class Slider(models.Model):
	title = models.CharField(max_length=150)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	slideimg = models.FileField(upload_to = "slide/")
	def __str__(self):
		return self.title

# partnyor
class Partnyor(models.Model):
	title = models.CharField(max_length=150)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	partnyorimg = models.FileField(upload_to = "partimg/")
	def __str__(self):
		return self.title

# cataegory
class Category(models.Model):
    parent = models.ForeignKey('self', related_name='children', on_delete=models.CASCADE, blank = True, null=True)
    title = models.CharField(max_length=100) 
    slug = AutoSlugField(populate_from='title', unique=True, null=False, editable=False)
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
	category = models.ForeignKey(Category, on_delete = models.CASCADE)
	name = models.CharField(max_length = 100)
	slug = models.SlugField(max_length=100, db_index=True)
	price = models.IntegerField()
	weight = models.IntegerField()
	productimg = models.FileField(upload_to = "productimg/")
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	status = models.IntegerField(default=0)
	description = models.TextField()

	def __str__(self):
	    return 'name={0}, category={1}'.format(self.name, self.category)

# Images
class Images(models.Model):
	product=models.ForeignKey(Product,on_delete=models.CASCADE)
	title = models.CharField(max_length=50)
	productimg=models.FileField(upload_to="productimg/")
	def __str__(self):
		return self.title