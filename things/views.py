from django.shortcuts import render

# Create your views here.



#The request is an object created by Django containing all info it received in an HTTP request.
#Our view is responsible for generating a response to that request.
def home(request):
    return render(request, 'home.html')
