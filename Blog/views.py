from django.shortcuts import render
from django.views import View
from .models import *


class Home(View):
    def get(self,request):
        data = {"manzara":Manzara.objects.all()}
        return render(request,'index.html',data)


class Portfolio(View):
    def get(self,request):
        data = {"shaxar":Shaxar.objects.all()}
        return render(request,'portfolio.html',data)


class Contact(View):
    def get(self,request):
        data = {"muhandis":About.objects.all()}
        return render(request,'contact.html',data)


class Services(View):
    def get(self,request):
        data = {"din":Din.objects.all()}
        return render(request,'services.html',data)


class Blog(View):
    def get(self,request):
        return render(request,'blog_post.html')

