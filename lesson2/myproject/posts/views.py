from django.shortcuts import render
from django.views.generic import TemplateView
from datetime import datetime
# Create your views here.
def posts_list(request):
    return render(request, 'posts/posts_list.html')

def update_page(request):
    now = datetime.now()

    context = { 
        "day": now.day,
        "month": now.month,
        "year": now.year,
        "heros_list": ["singed", "garen", "yasuo", "temken"]
    }
    return render(request, 'posts/update_page.html', context)

class AboutPage(TemplateView):
    template_name = "posts/about.html"