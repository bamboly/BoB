from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(*args, **kwargs):
	return HttpResponse("<h1>Hello World<h1>")

def contact_view(*args , **kwargs):
	return HttpResponse("<h1>Contact_Page<h1>")

def social_view(*args , **kwargs):
	return HttpResponse("<h1>social_Page<h1>")

def about_view(*args , **kwargs):
	return HttpResponse("<h1>About_Page<h1>")

def sobhan_view(*args , **kwargs):
	return HttpResponse("<h1>Sobhan khar ast<h1>")