from django.shortcuts import render

# Create your views here.
def home(request):
	return render(request,'room/index.html')
def form(request):
	return render(request,'room/book_a_room.html')
	