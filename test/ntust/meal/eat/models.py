from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Restaurant(models.Model):
	image = models.ImageField(upload_to='images/', null=True, blank=True)
	name = models.CharField(max_length=20)
	info = models.CharField(max_length=500)
	phone_number = models.CharField(max_length=15, blank=True)
	address = models.CharField(max_length=50, blank=True)
	is_open = models.BooleanField(default=False)
	votes = models.IntegerField(default=0)
	
	def __str__(self):
		return self.name

class Food(models.Model):
	image = models.ImageField(upload_to='images/', null=True, blank=True)
	name = models.CharField(max_length=20)
	price = models.DecimalField(max_digits=3, decimal_places=0)
	comment = models.CharField(max_length=50, blank=True)
	full = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
	restaurant = models.ForeignKey('Restaurant', on_delete=models.PROTECT)

	def __str__(self):
		return self.name

class Feedback(models.Model):
	title = models.CharField(max_length=20, default="")
	pub_date = models.DateTimeField(auto_now_add=True)
	content = models.CharField(max_length=200, blank=True)
	restaurant = models.ForeignKey('Restaurant', on_delete=models.PROTECT)

	def __str__(self):
		return str(self.title)
