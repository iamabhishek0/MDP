from django.shortcuts import render
from .models import FormSubmit , ReferenceMail
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.http import HttpResponse


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
	formsubmit=FormSubmit(name=name,email=email,number=number,street=street,city=city,pincode=pincode,arrive=arrive,depart=depart,reference_email=reference_email,reference_name=reference_name)
	referencemail=ReferenceMail(reference_name=reference_name,reference_email=reference_email)
	referencemail.save()
	formsubmit.save()
	user = User.objects.create_user(username=name,
								 email=reference_email,
								 password='arpitarpit')

	#def create(self, validated_data):
		#user = User.objects.create(username=validated_data['name'],email=validated_data['reference_email'])
	user.is_active = False
	mail_subject = 'Activate your blog account.'
	user.save()
	message=render_to_string('referencemail.html',{'user': user,
				'reference_name' : reference_name ,
				'domain': '127.0.0.1:8000',
				'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
				'token': account_activation_token.make_token(user),})
	to_email=reference_email
	email=EmailMessage(mail_subject,message,to=[to_email])
	email.send()
	return render(request,"room/formsubmitted.html")




def activate(request, uidb64, token):
	try:
		uid = force_text(urlsafe_base64_decode(uidb64))
		user = User.objects.get(pk=uid)
	except(TypeError, ValueError, OverflowError, User.DoesNotExist):
		user = None
	if user is not None and account_activation_token.check_token(user, token):
		user.is_active = True
		user.save()

		# return redirect('home')
		return HttpResponse('Thank you for your confirmation')
	else:
		return HttpResponse('Activation link is invalid!')
