from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render

from .models import *

from django.views.decorators.csrf import csrf_exempt

import json

def receiveName (request, professorName, class_label):
	# take request

	if Professor.objects.filter(profName=professorName).exists():
		prof = Professor.objects.get(profName=professorName)

		if Question.objects.filter(professor=prof).exists():
			profquestions = Question.objects.filter(professor=prof)

			question_texts = []
			question_ids = []
			for profques in profquestions:
				question_texts.append(profques.text)
				question_ids.append(profques.id)
			return JsonResponse({"new_prof": False, "questions": question_texts, "question_ids": question_ids})
		
		return JsonResponse({"questions": [], "question_ids": []})

	prof = Professor(profName = professorName)
	prof.save()


	room, create = Room.objects.get_or_create(label=class_label)

	return JsonResponse({'new_prof': new_prof, 'prof_name': professorName, 'id':prof.id})

@csrf_exempt
def receiveQuestion (request, professorName, question):
	# requestedProfName=request.Get.get('profName')
	prof = Professor.objects.get(profName=professorName)
	requestbody = json.loads(request.body)

	requestedClassName=requestbody['className']
	requestedText = requestbody['text']
	requestedOptions = requestbody['options']
	correctNumber = requestbody['correct']

	requestedQuestion = Question(className=requestedClassName,
								 professor=prof,
								 text=requestedText,
								 active=False)
	requestedQuestion.save()

	# fill each option from requestedOptions list text
	for index in range(len(requestedOptions)):
		requestedOption = Option(question=requestedQuestion, 
        	sequence=index, 
        	text=requestedOptions[index], 
        	correct=False)
        if index==correctNumber:
        	requestedOption.correct = True
        requestedOption.save()

	return JsonResponse({
		"prof_name": professorName, 
		"question_text": requestedQuestion.text,
		"options_text": requestedOptions})


def index(request):
	ctd = {}
	return render(request, 'index.html', context=ctd)

def prof(request):
	ctd = {}
	return render(request, 'prof.html', context=ctd)

def student(request):
	ctd = {}
	return render(request, 'student.html', context=ctd)

def get_room(request):
	label = request.POST.get('room')
    # If the room with the given label doesn't exist, automatically create it
    # upon first visit (a la etherpad).
	room, created = Room.objects.get_or_create(label=label)

    # We want to show the last 10 questions, ordered most-recent-last
	questions = reversed(room.questions[:30])

	return render(request, "room.html", {
	    'class': room,
	    'questions': questions,
	})
