from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
# Create your models here.

class Issue(models.Model):
    summary = models.CharField(max_length=256)
    description = models.TextField()
    reporter = models.ForeignKey(get_user_model(), on_delete=models.CASCADE
    )

    assignee = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='assignee'
    )
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    is_archived = models.BooleanField(default=False)

    def __str__(self):
        return self.summary[0:128]
    
    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])
    
class Status(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
    
