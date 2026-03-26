from django.shortcuts import render

def homepage(request):
    context = {
        "name": "Loi",
        "age": "18"
        }
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html')