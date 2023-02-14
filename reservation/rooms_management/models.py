from django.db import models


# Create your models here.
class ConferenceRoom(models.Model):
    name = models.CharField(max_length=255, unique=True)
    capacity = models.PositiveIntegerField()
    projector_availability = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class RoomReservation(models.Model):
    room = models.ForeignKey(ConferenceRoom, on_delete=models.CASCADE)
    date = models.DateField()
    comment = models.TextField(blank=True)

    class Meta:  # wartość room_id, połączona z wartością date jest unikalna.
        unique_together = ("room", "date")
