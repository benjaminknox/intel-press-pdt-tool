from django.http import HttpResponse
from django.shortcuts import render, redirect

def viewdocument(request, documentid=None):
	return HttpResponse("General User")