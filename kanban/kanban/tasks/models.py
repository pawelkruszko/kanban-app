from django.db import models

class Task(models.Model):
    # Definicja statusów zadania
    STATUS_CHOICES = [
        ('TODO', 'To Do'),
        ('IN_PROGRESS', 'In Progress'),
        ('DONE', 'Done'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,  # używamy STATUS_CHOICES
        default='TODO'
    )

    def __str__(self):
        return self.title
