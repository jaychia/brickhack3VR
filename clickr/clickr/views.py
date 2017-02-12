from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render

from models import *

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
			return JsonResponse({"new_prof": False, "prof_name": professorName,
				"id":prof.id, "class" : class_label,"questions": question_texts, "question_ids": question_ids})
		
		return JsonResponse({"new_prof": False, "prof_name": professorName, "id":prof.id,
			"class": class_label, "questions": [], "question_ids": []})

	prof = Professor(profName = professorName)
	prof.save()


	# room, create = Room.objects.get_or_create(label=class_label)

	return JsonResponse({"new_prof": True, "prof_name": professorName,
		"id":prof.id,"class": class_label,"questions": [], "question_ids": []})

def receiveStudentName (request, studentName, class_label):
	student, created = Student.objects.get_or_create(name=studentName)
	room, created = Room.objects.get_or_create(label=class_label)
	questions = room.questions.all()
	questions_list = [(question.id, question.text, question.options.all()) for question in questions]


	return JsonResponse({
			"questions": questions_list,
			"class_label": room.label,
			"student_name": student.name,
		})

@csrf_exempt
def receiveQuestion (request, professorName, class_label, question):
	# requestedProfName=request.Get.get('profName')
	prof = Professor.objects.get(profName=professorName)
	requestbody = json.loads(request.body)

	requestedClassName=requestbody['className']
	requestedText = requestbody['text']
	requestedOptions = requestbody['options']
	correctNumber = requestbody['correct']

	qroom = Room(label=class_label)
	qroom.save()

	requestedQuestion = Question(room = qroom,
								className=requestedClassName,
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
		"prof_id": prof.id,
		"question_text": requestedQuestion.text,
		"question_id": requestedQuestion.id,
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
