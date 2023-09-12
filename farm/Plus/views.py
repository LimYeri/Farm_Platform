from django.shortcuts import render

# Create your views here.

def live(request):
    return render(request, 'plus/livestream.html')

def farmer_diary(request):
    return render(request, 'plus/farmer-diary.html')