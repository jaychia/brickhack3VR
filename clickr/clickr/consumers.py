from django.http import JsonResponse
from channels import Group
from channels.sessions import channel_session
from .models import Room

@channel_session
def ws_connect(message):
	prefix, label = message['path'].strip('/').split('/')
	room = Room.objects.get(label=label)
	Group('chat-' + label).add(message.reply_channel)
	message.channel_session['room'] = room.label
	message.reply_channel.send({"accept": True})


@channel_session
def ws_receive(message):
    label = message.channel_session['room']
    room = Room.objects.get(label=label)
    qn = json.loads(message['question'])
    qn = Question.objects.get(pk=qn)
    student = Student.objects.get(name=message['name'])
    options = student.options.all()

    for option in options:
    	if option.question.id == qn.id:
    		#Repeat answer
    		option.delete()

    newoption = student.options.create(id=message['option'])

    # m = room..create(handle=data['handle'], message=data['message'])
    # Group('chat-'+label).send({'text': json.dumps(m.as_dict())})

@channel_session
def ws_disconnect(message):
    label = message.channel_session['room']
    Group('chat-'+label).discard(message.reply_channel)