from django.shortcuts import render

# Create your views here.
def news(request):
    return render(request, 'posts/news.html')

def update(request):
    context = {
        "update_list" : [
            "singed",
            "tamken",
            "yasuo",
            "lilia"
        ]
    }
    return render(request, 'posts/updatepage.html', context)

def tournament(request):
    context = {

    }
    return render(request, 'posts/tournamentpage.html', context)
