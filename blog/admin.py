from django.contrib import admin

from .models import User, Topic, Message

admin.site.register([User, Topic, Message])
