import logging

from django.urls import reverse
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from website.celery import app
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from .models import UserProfile
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from .tokens import account_activation_token
from django.utils.encoding import force_bytes, force_text
from dateutil import parser
from django.utils.timezone import datetime
from easy_pdf.views import PDFTemplateView
@app.task
def send_verification_email(user_id):
	user=User.objects.get(username=user_id)
	profile = user.userprofile
	message=render_to_string('referencemail.html',{'user': user,
				'reference_name' : profile.reference_name ,
				'domain': '127.0.0.1:8000',
				'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
				'token': account_activation_token.make_token(user),})
	message_director=render_to_string('director_mail.html',{'user': user,
				'reference_name' : profile.reference_name ,
				'domain': '127.0.0.1:8000/director',
				'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
				'token': account_activation_token.make_token(user),})
	to_email=profile.reference_email
	mail_subject = 'IIITM guest house'
	email=EmailMessage(mail_subject,message,to=[to_email])
	email_director=EmailMessage(mail_subject,message_director,to=['imarpit02@gmail.com'])
	email.send()
	email_director.send()

@app.task
def send_feedback():
	for user in get_user_model().objects.all():
		profile = user.userprofile
		if profile.arrive == datetime.today().date() :
			message=render_to_string('feedback.html',{'user': user,
						})

			to_email=user.email
			mail_subject = 'Feedback'
			email=EmailMessage(mail_subject,message,to=[to_email])
			email.send()
@app.task
def store_bill():
	class HelloPDFView(PDFTemplateView):

		for user in get_user_model().objects.all():
			profile = user.userprofile
			if profile.depart == datetime.today().date() :
				template_name = 'feedback.html'
				base_url = 'file://' + settings.STATIC_ROOT
				download_filename = 'hello.pdf'
