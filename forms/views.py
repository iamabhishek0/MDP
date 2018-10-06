from django.shortcuts import render
from .models import FormSubmit , ReferenceMail

def form_view(request):
	return render(request,'room/book_a_room.html')

def form_submit(request):
	name=request.POST["name"]
	email=request.POST["email"]
	number=request.POST["phone"]
	street=request.POST["street"]
	city=request.POST["city"]
	pincode=request.POST["post-code"]
	arrive=request.POST["arrive"]
	depart=request.POST["depart"]
	reference_name=request.POST["reference_name"]
	reference_email=request.POST["reference_email"]
	formsubmit=FormSubmit(name=name,email=email,number=number,street=street,city=city,pincode=pincode,arrive=arrive,depart=depart)
	referencemail=ReferenceMail(reference_name=reference_name,reference_email=reference_email)
	referencemail.save()
	formsubmit.save()
	return render(request,"room/formsubmitted.html")
