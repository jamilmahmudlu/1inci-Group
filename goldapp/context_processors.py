from django.shortcuts import render
from .models import Category

def menu(request):
	catg = Category.objects.filter(parent=None)
	context = {
		"catg":catg,
	}
	return context


	