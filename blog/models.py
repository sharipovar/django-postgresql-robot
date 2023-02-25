from django.db import models

class User(models.Model):
    user_name = models.CharField(max_length=200)

class Topic(models.Model):
    topic_name = models.CharField(max_length=200)

class Message(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    topic_id = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    created_at = models.DateTimeField('date published')
