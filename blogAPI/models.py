from django.db import models
import uuid
# from django.contrib.auth.models import User

# Create your models here.

class Blog(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=250)
    post = models.TextField()
    date = models.DateField(auto_now_add=True)
    # author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blogs")

    def __str__(self):
        return self.title