# shop/models.py
from django.db import models
from django.utils.text import slugify
from django.urls import reverse

class Category(models.Model):
	name = models.CharField(max_length=100, db_index=True)
	slug = models.SlugField(max_length=100, null=True,blank=True)
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ('-created','name',) # here
		verbose_name='Category'
		verbose_name_plural = 'Categories'

	def save(self, *args,**kwargs):
		self.slug = slugify(self.name, allow_unicode=True)

		return super(Category, self).save(*args, **kwargs)
	
	def get_absolute_url(self):
		return reverse('category_detail',args=[self.slug])
