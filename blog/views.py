from django.http import JsonResponse, Http404
from django.http import HttpResponse
from django.core.serializers import serialize

from .models import User, Topic, Message

def index(request):
    users = User.objects.all();
    topics = Topic.objects.all();
    messages = Message.objects.all();

    output = 'Users: ' + ', '.join([str(u) for u in users])
    output += '<br>\n';
    output += 'Topics: ' + ', '.join([str(t) for t in topics])
    output += '<br>\n';
    output += 'Messages: ' + ', '.join([m.text for m in messages])
    return HttpResponse(output)

def user(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        raise Http404("User does not exist")
    return JsonResponse( { 'id': user.id, 'user_name': user.user_name } )

def topic(request, topic_id):
    try:
        topic = Topic.objects.get(pk=topic_id)
    except Topic.DoesNotExist:
        raise Http404("Topic does not exist")
    return JsonResponse( { 'id': topic.id, 'topic_name': topic.topic_name } )

def message(request, message_id):
    try:
        message = Message.objects.get(pk=message_id)
    except Message.DoesNotExist:
        raise Http404("Message does not exist")
    return JsonResponse({ 
        'id': message.id, 
        # 'user': serialize('json', [message.user]), 
        # 'topic': serialize('json', [message.topic]),
        'user': str(message.user), 
        'topic': str(message.topic),
        'text': message.text,
        'created_at': message.created_at
    })