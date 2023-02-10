from django.shortcuts import render, redirect
from django.views import View
from rooms_management.models import ConferenceRoom


# Create your views here.
class HomeView(View):
    def get(self, request):
        return render(request, "rooms_management/base.html")


class AddRoomView(View):
    def get(self, request):
        return render(request, "rooms_management/add_room.html")

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
            return render(request, 'rooms_management/add_room.html', context={'error': 'Nie podano nazwy sali'})
        if capacity <= 0:
            return render(request, 'rooms_management/add_room.html', context={'error': 'Pojemność sali musi być dodatnia'})
        if ConferenceRoom.objects.filter(name=name):
            return render(request, 'rooms_management/add_room.html', context={'error': 'Sala o podanej nazwie już istnieje'})

        ConferenceRoom.objects.create(name=name, capacity=capacity, projector_availability=projector)
        return redirect('rooms-list')


class RoomListView(View):
    def get(self, request):
        rooms = ConferenceRoom.objects.all()
        return render(request, "rooms_management/rooms.html", context={"rooms": rooms})


class DeleteRoomView(View):
    def get(self, request, room_id):
        room = ConferenceRoom.objects.get(id=room_id)
        room.delete()
        return redirect('rooms-list')
