from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import BookingForm

# Create your views here.
def home(request):
	form=BookingForm
	if request.method=='POST':
		bookForm=BookingForm(request.POST)
		if bookForm.is_valid():
			bookForm.save()
			messages.success(request,'Data has been added')
			return redirect('/')
	return render(request,'index.html',{'form':form})