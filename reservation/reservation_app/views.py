from django.shortcuts import render
from django.views import View


# Create your views here.
class HomeView(View):
    def get(self, request):
        return render(request, "base.html")


class AddRoomView(View):
    def get(self, request):
        return render(request, "add_room.html")
