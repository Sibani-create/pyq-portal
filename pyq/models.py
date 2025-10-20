from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class PYQ(models.Model):
    title = models.CharField(max_length=250)
    subject = models.CharField(max_length=120)
    year = models.PositiveIntegerField()
    semester = models.CharField(max_length=50, blank=True)
    file = models.FileField(upload_to='pyqs/')
    uploaded_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.subject} - {self.year} - {self.title}"
