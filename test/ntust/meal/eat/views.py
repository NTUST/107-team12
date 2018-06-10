from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from .models import Restaurant, Food, Feedback
import random

def index(request):
	return render(request, 'eat/home.html')

def pick(request):
	random_idx = random.randint(0, Food.objects.count() - 1)
	random_object = Food.objects.all()[random_idx]
	return render(request, 'eat/pick.html', {'random_object': random_object})


def vote(request):
	restaurant = Restaurant.objects.all()
	if request.method == 'POST':
		try:
			selected_choice = restaurant.get(name=request.POST.get('best'))
		except (KeyError, Restaurant.DoesNotExist):
			return render(request, 'eat/vote.html', {'restaurant': restaurant})
		else:
			selected_choice.votes += 1
			selected_choice.save()
	return render(request, 'eat/vote.html', {'restaurant': restaurant})

def chowfan(request):
	chowfan = Restaurant.objects.get(name='炒飯炒麵')
	return render(request, 'eat/fan-info.html', {'chowfan': chowfan})

def cfmenu(request):
	chowfan = Restaurant.objects.get(name='炒飯炒麵')
	return render(request, 'eat/fan-menu.html', {'chowfan': chowfan})

def cffeedback(request):
	chowfan = Restaurant.objects.get(name='炒飯炒麵')
	if request.method == 'POST':
		title = request.POST.get('title')
		content = request.POST.get('content')
		chowfan.feedback_set.create(content=content, title=title)
	
	return render(request, 'eat/fan-fed.html', {'chowfan': chowfan})

def tofu(request):
	tofu = Restaurant.objects.get(name='豆腐麵線')
	return render(request, 'eat/tofu-info.html', {'tofu': tofu})

def tmenu(request):
	tofu = Restaurant.objects.get(name='豆腐麵線')
	return render(request, 'eat/tofu-menu.html', {'tofu': tofu})

def tfeedback(request):
	tofu = Restaurant.objects.get(name='豆腐麵線')
	if request.method == 'POST':
		title = request.POST.get('title')
		content = request.POST.get('content')
		tofu.feedback_set.create(content=content, title=title)
	
	return render(request, 'eat/tofu-fed.html', {'tofu': tofu})

def fried(request):
	fried = Restaurant.objects.get(name='鹹酥雞')
	return render(request, 'eat/fried-info.html', {'fried': fried})

def fmenu(request):
	fried = Restaurant.objects.get(name='鹹酥雞')
	return render(request, 'eat/fried-menu.html', {'fried': fried})

def ffeedback(request):
	fried = Restaurant.objects.get(name='鹹酥雞')
	if request.method == 'POST':
		title = request.POST.get('title')
		content = request.POST.get('content')
		fried.feedback_set.create(content=content, title=title)
	
	return render(request, 'eat/fried-fed.html', {'fried': fried})