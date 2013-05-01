from django.http import HttpResponse
from django.shortcuts import render, redirect

def viewdocument(request):
	return HttpResponse("General User")