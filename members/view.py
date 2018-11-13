from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from forms.models import FormSubmit , Room , Booking ,UserProfile
from django.core.mail import EmailMessage
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from forms.tokens import account_activation_token
from django.template.loader import render_to_string
from django.contrib.auth import authenticate, login ,logout


def login_member(request):
	return render(request,'login_members.html')
def login_(request):

	username = request.POST.get('username')
	password = request.POST.get('password')
	user = authenticate(request, username=username, password=password)
	profile = user.userprofile

	if user is not  None and profile.is_member is True :
		login( request , user)
		return HttpResponse('vy')

		# Redirect to a success page.
		...
	else:
		return HttpResponse('Sorry you are not a member')
		# Return an 'invalid login' error message.

def register(request):
	name=request.POST["name"]
	email=request.POST["email"]
	number=request.POST["number"]
	street=request.POST["street"]
	city=request.POST["city"]
	pincode=request.POST["post-code"]
	reference_name=request.POST["reference_name"]
	reference_email=request.POST["reference_email"]
	username=request.POST["username"]
	password=request.POST["password"]
	repass=request.POST["repassword"]

	if User.objects.filter(username=username).exists():
		return HttpResponse('Username not available')


	user = User.objects.create_user(username=username,email=email,password=password,first_name=name)
	profile = user.userprofile
	profile.street=street
	profile.city=city
	profile.pincode=pincode
	profile.number=number
	profile.reference_name=reference_name
	profile.reference_email=reference_email
	profile.applied_for_member=True
	profile.save()
	user.save()
	mail_subject = 'IIITM guest house'
	message=render_to_string('director_mail.html',{'user': user,
					'reference_name' : reference_name ,
					'domain': '127.0.0.1:8000/director/member',
					'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
					'token': account_activation_token.make_token(user),})
	email=EmailMessage(mail_subject,message,to=['imarpit02@gmail.com'])
	email.send()

	return  HttpResponse('Thank you for applying ')
def member_activate(request, uidb64, token):
	try:
		uid = force_text(urlsafe_base64_decode(uidb64))
		user = User.objects.get(pk=uid)
	except(TypeError, ValueError, OverflowError, User.DoesNotExist):
		user = None
	if user is not None and account_activation_token.check_token(user, token):
		profile = user.userprofile
		profile.is_member = True

		profile.save()
		return HttpResponse('Thank you for your confirmation')
	else:
		return HttpResponse('link is invalid! or You have already confirmed!!')
