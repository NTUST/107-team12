from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^vote/', views.vote, name='vote'),
	url(r'^pick/', views.pick, name='pick'),
	url(r'^chowfan/', views.chowfan, name='chowfan'),
	url(r'^tofu', views.tofu, name='tofu'),
	url(r'^fried', views.fried, name='fried'),
	url(r'^cfmenu/', views.cfmenu, name='cfmenu'),
	url(r'^tmenu', views.tmenu, name='tmenu'),
	url(r'^fmenu', views.fmenu, name='fmenu'),
	url(r'^cffeedback', views.cffeedback, name='cffeedback'),
	url(r'^tfeedback', views.tfeedback, name='tfeedback'),
	url(r'^ffeedback', views.ffeedback, name='ffeedback'),
]