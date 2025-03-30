from django.db import models

# Create your models here.
class Folder(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class File(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    folder = models.ForeignKey(to=Folder, on_delete=models.CASCADE)
    file = models.FileField(upload_to="media", null=True, blank=True)
    def __str__(self):
        return self.name
