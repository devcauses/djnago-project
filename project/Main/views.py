from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request,'main.html')
def aauthor(request):
    return render(request,'author.html')
    