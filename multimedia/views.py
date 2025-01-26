from django.shortcuts import render
from .models import Media
from django.shortcuts import redirect
from .forms import MediaForm


# Create your views here.
def main(request):
    return render(request, 'main.html')


def add_media(request):
    if request.method == 'GET':
       form = MediaForm(request.GET)
       if form.is_valid():
            form.save() 
            return redirect('upload')
       else:
              return render(request, 'add_media.html')
   
def upload(request):
        media = Media.objects.all()
        return render(request, 'upload.html', {'media': media})
     
