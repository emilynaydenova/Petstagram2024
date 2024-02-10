from django.shortcuts import render

from photos.models import Photo


# Create your views here.
def index(request):
    context = {
        "photos": Photo.objects.all()
    }
    return render(request, 'common/home-page.html', context)
