from django.db import models

# Create your models here.
class FindMembers(models.Model):
    name = models.CharField(max_length=20)
    age = models.CharField(max_length=3)
    birth = models.TextField()
    email = models.TextField()

    def __str__(self):
        return f'[{self.pk}]{self.name}'

    def get_absolute_url(self):
        return '/members/{}'.format(self.pk)