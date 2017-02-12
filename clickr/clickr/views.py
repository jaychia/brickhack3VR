from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render

from .models import Professor
from .models import Question
from .models import Option
from .models import Student


def receiveName (request, professorName):
	# take request

	if Professor.objects.filter(profName=professorName).exists():
		new_prof = False
	else:
		new_prof = True
        prof = Professor(profName = professorName)
        prof.save()

	return JsonResponse({'new_prof': new_prof, 'prof_name': professorName, 'id':prof.id})


def receiveQuestion (request, professorName, question):
	# requestedProfName=request.Get.get('profName')
	prof = Professor.objects.get(profName=professorName)
	requestedClassName=request.POST.get('className')
	requestedText = request.POST.get('text')
	requestedOptions = request.POST.get('options')
	correctNumber = int(request.POST.get('correct'))

	requestedQuestion = Question(className = requestedClassName, professor=prof, text=requestedText,active=true)
	requestedQuestion.save()

	# fill each option from requestedOptions list text
	for index in range(len(requestedOptions)):
		requestedOption = Option(question=requestedQuestion, 
        	sequence=index, 
        	text=requestedOptions[index], 
        	correct=false)
        if index==correctNumber:
        	requestedOption.correct = True
        requestedOption.save()

	return JsonResponse({
		"prof_name": professorName, 
		"prof": prof, 
		"question": requestedQuestion})


def index(request):
	ctd = {}
	return render(request, 'index.html', context=ctd)

def prof(request):
	ctd = {}
	return render(request, 'prof.html', context=ctd)

def student(request):
	ctd = {}
	return render(request, 'student.html', context=ctd)
