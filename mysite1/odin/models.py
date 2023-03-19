from django.db import models

# Create your models here.


class User(models.Model):
    user_name = models.CharField(max_length=200)

    def __str__(self):
        return str(self.id) + " " + self.user_name

class Topic(models.Model):
    topic_name = models.CharField(max_length=200)

    def __str__(self):
        return str(self.id) + " " + self.topic_name

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    created_at = models.DateTimeField('date published')