from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse("IntelPress Index Page " )

def login(request):
	return HttpResponse("login")

def add(request):
	return HttpResponse("add")

def view(request,documentid):
	return HttpResponse("Page")

def delete(request,documentid):
	return HttpResponse("Page")

def approve(request,documentid):
	return HttpResponse("Page")

def addcomment(request,documentid):
	return HttpResponse("Page")

def download(request,documentid,locationid):
	return HttpResponse("Page "+documentid+" "+locationid)

def editcomment(request,documentidm,commentid):
	return HttpResponse("Page "+documentid+" "+locationid)

def deletecomment(request,documentidm,commentid):
	return HttpResponse("Page "+documentid+" "+locationid)
