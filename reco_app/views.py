from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import HttpResponse


## MODEL VIEW
from .forms import userinput_form
from .models import User_input

"""
def userinput_create_view(request):
	form = userinput_form(request.POST or None)
	if form.is_valid():
		form.save()
		form = ProductForm()

	context = {
		'form': form
	}
	return render(request, "userinput_page.html", context)
	#the slash is the folder, after the file we want to render
"""

def userinput_create_view(request):
	my_form = userinput_form()
	if request.method == "POST":
		my_form = userinput_form(request.POST or None) #create instance of a class
		if my_form.is_valid():
			User_input.objects.create(**my_form.cleaned_data) #if the form is valid create an instance in the database
		#now the data is good
		else: 
			print(my_form.errors) #print the error (missing field etc. -- this is detected automatically by django)

	context = {
		"form": my_form
	}
	return render(request, "userinput_page.html", context)
	
