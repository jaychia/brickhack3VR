from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render

from .models import Professor
from .models import Question
from .models import Option
from .models import Student

from django.views.decorators.csrf import csrf_exempt

import json

def receiveName (request, professorName):
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
			return JsonResponse({"questions": question_texts, "question_ids": question_ids})
		
		return JsonResponse({"questions": [], "question_ids": []})

	prof = Professor(profName = professorName)
	prof.save()

	return JsonResponse({"questions": [], "question_ids": []})

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
