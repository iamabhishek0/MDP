from django.shortcuts import render
from .models import FormSubmit

def form_view(request):
	return render(request,'room/book_a_room.html')

def form_submit(request):
	name=request.POST["name"]
	email=request.POST["email"]
	number=request.POST["phone"]
	street=request.POST["street"]
	city=request.POST["city"]
	formsubmit=FormSubmit(name=name,email=email,number=number,street=street,city=city)
	formsubmit.save()
	return render(request,"room/index.html")
