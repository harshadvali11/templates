from django.shortcuts import render

# Create your views here.
#HttpResponse is used for responding a string
#render function is used for responding an entire html file
#syntax of render function
    # render(request,'html filename along with extension')

def temp(request):
    return render(request,'h1.html')

def select(request):
    return render(request,'h2.html')