from django.db import models
from django.contrib.auth.models import User


due_date = models.DateField(null=True, blank=True)


class Task(models.Model):

    STATUC_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    status = models.CharField(
        max_length=10,
        choices=STATUC_CHOICES,
        default='pending'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title