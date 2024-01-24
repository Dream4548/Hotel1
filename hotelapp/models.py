from django.db import models

class Booking(models.Model):
    ROOM_TYPE_CHOICES = [
        ('standard', 'ธรรมดา'),
        ('superior', 'ซูพีเรียร์'),
        ('deluxe', 'ดีลักซ์'),
    ]
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=10, default='')
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    room_type = models.CharField(max_length=20, choices=ROOM_TYPE_CHOICES)

    def __str__(self):
        return self.name


