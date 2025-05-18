from django.db import models

class BoardingHouse(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='boardinghouse_images/')
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name
