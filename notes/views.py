from django.shortcuts import render
from notes.models import Note

# Create your views here.
def home (request):
    x = Note.objects.all()
    context = {
        "N" : x
    }
    return render(request,'home.html',context)


def body (request, id):
    x = Note.objects.get(id = id)

    context = {
        "w" : x
    }
    return render(request,'body.html', context)

