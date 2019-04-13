from django.shortcuts import render, get_object_or_404
from .models import Category

def category_detail(request,slug):
	category = get_object_or_404(Category,slug=slug)

	return render(request,'shop/category_detail.html',{'cateogry':category})
