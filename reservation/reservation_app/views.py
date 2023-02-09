from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'base.html')


def add_room(request):
    return render(request, 'add_room.html')
