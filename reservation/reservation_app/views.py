from django.shortcuts import render, redirect
from django.views import View
from reservation_app.models import ConferenceRoom


# Create your views here.
class HomeView(View):
    def get(self, request):
        return render(request, "base.html")


class AddRoomView(View):
    def get(self, request):
        return render(request, "add_room.html")

    def post(self, request):
        name = request.POST.get('room-name')
        capacity = request.POST.get('capacity')
        if capacity:
            capacity = int(capacity)
        else:
            capacity = 0
        projector = request.POST.get('projector')
        if projector == 'true':
            projector = True
        else:
            projector = False

        if not name:
            return render(request, 'add_room.html', context={'form_error': 'Nie podano nawy sali'})
        if capacity <= 0:
            return render(request, 'add_room.html', context={'form_error': 'Pojemność sali musi być dodatnia'})
        if ConferenceRoom.objects.filter(name=name).first():
            return render(request, 'add_room.html', context={'form_error': 'Sala o podanej nazwie już istnieje'})

        ConferenceRoom.objects.create(name=name, capacity=capacity, projector_availability=projector)
        return redirect('rooms-list')


class RoomListView(View):
    def get(self, request):
        rooms = ConferenceRoom.objects.all()
        return render(request, "rooms.html", context={"rooms": rooms})
