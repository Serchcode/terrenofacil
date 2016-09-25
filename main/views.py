from django.shortcuts import render
from django.views.generic import View, TemplateView

class HomeView(View):
	def get(self,request):
		template_name="index.html"
		return render(request,template_name)

class HolaView(View):
	def get(self, request):
		template_name="hola.html"
		return render(request,template_name)