from django.shortcuts import render

# Create your views here.
def ifelif(request):
    d={'a':10,'b':8,'c':6}
    return render(request,'ifelif.html')