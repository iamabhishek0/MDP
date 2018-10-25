from django.shortcuts import render
from .models import FormSubmit , ReferenceMail , Room , Booking ,UserProfile
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.http import HttpResponse
from dateutil import parser
from random import randint
def form_view(request):
	return render(request,'room/book_a_room.html')

def form_submit(request):
	name=request.POST["name"]
	email=request.POST["email"]
	number=request.POST["phone"]
	street=request.POST["street"]
	city=request.POST["city"]
	pincode=request.POST["post-code"]
	arrive=parser.parse(request.POST["arrive"]).date()
	depart = parser.parse(request.POST["depart"]).date()
	room_type = request.POST["room_type"]
	reference_name=request.POST["reference_name"]
	reference_email=request.POST["reference_email"]
	formsubmit=FormSubmit(name=name,email=email,number=number,street=street,city=city,pincode=pincode,arrive=arrive,depart=depart,reference_email=reference_email,reference_name=reference_name)
	referencemail=ReferenceMail(reference_name=reference_name,reference_email=reference_email)
	referencemail.save()
	formsubmit.save()

	found = 0
	for r in Room.objects.raw('SELECT * FROM forms_room WHERE status = "a" and room_type = %s', [room_type]):
		f = 1
		rID = r.roomID
		for b in Booking.objects.raw('SELECT * FROM forms_booking WHERE roomID = %s', [rID]):
			if(b.arrive > depart or b.depart < arrive):
				pass
			else:
				f=0
		if f == 1:
			booking = Booking(bookingID = formsubmit.id, roomID = rID, name = name, arrive = arrive, depart = depart)
			booking.save()
			found = 1
			break
		if found == 1:
			break
	if found == 0:
		HttpResponse('Sorry no rooms available for requested dates')
		#room not available


	user = User.objects.create_user(username=name+str(randint(0, 999)),email=email,password='arpitarpit',first_name=name)
	profile = user.userprofile
	profile.street=street
	profile.city=city
	profile.pincode=pincode
	profile.arrive=arrive
	profile.depart=depart
	profile.number=number
	profile.reference_name=reference_name
	profile.reference_email=reference_email
	profile.save()
	mail_subject = 'IIITM guest house'
	user.save()
	message=render_to_string('referencemail.html',{'user': user,
				'reference_name' : reference_name ,
				'domain': '127.0.0.1:8000',
				'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
				'token': account_activation_token.make_token(user),})
	message_director=render_to_string('director_mail.html',{'user': user,
				'reference_name' : reference_name ,
				'domain': '127.0.0.1:8000/director',
				'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
				'token': account_activation_token.make_token(user),})
	to_email=reference_email

	email=EmailMessage(mail_subject,message,to=[to_email])
	email_director=EmailMessage(mail_subject,message_director,to=['imarpit02@gmail.com'])
	email.send()
	email_director.send()
	return render(request,"room/formsubmitted.html")

def activate(request, uidb64, token):
	try:
		uid = force_text(urlsafe_base64_decode(uidb64))
		user = User.objects.get(pk=uid)
	except(TypeError, ValueError, OverflowError, User.DoesNotExist):
		user = None
	if user is not None and account_activation_token.check_token(user, token):
		profile = user.userprofile
		profile.reference_verified = True
		if profile.director_verified:
			profile.verified = True
			if not profile.booking_mail_sent:
				mail_subject = 'IIITM guest house'
				message=render_to_string('booking_mail.html',{'user': user,
				'arrive': profile.arrive,
				'depart' : profile.depart

				,})
				to_email=user.email
				profile.booking_mail_sent= True
				email=EmailMessage(mail_subject,message,to=[to_email])
				email.send()


		profile.save()
		return HttpResponse('Thank you for your confirmation')
	else:
		return HttpResponse('link is invalid! or You have already confirmed!!')
def director_activate(request, uidb64,token):
	try:
		uid = force_text(urlsafe_base64_decode(uidb64))
		user = User.objects.get(pk=uid)
	except(TypeError, ValueError, OverflowError, User.DoesNotExist):
		user = None
	if user is not None and account_activation_token.check_token(user, token):
		profile = user.userprofile
		profile.director_verified = True
		if profile.reference_verified:
			profile.verified = True
			if not profile.booking_mail_sent:
				mail_subject = 'IIITM guest house'
				message=render_to_string('booking_mail.html',{'user': user,
				'arrive': profile.arrive,
				'depart' : profile.depart

				,})
				to_email=user.email
				profile.booking_mail_sent= True
				email=EmailMessage(mail_subject,message,to=[to_email])
				email.send()

		profile.save()
		return HttpResponse('Thank you for your confirmation')
	else:
		return HttpResponse('link is invalid! or You have already confirmed!!')
