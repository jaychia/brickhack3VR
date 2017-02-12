from django.http import HttpResponse
from django.http import JsonResponse

from .models import Professor
from .models import Question
from .models import Option
from .models import Student


def receiveName (request):
	# take request

	requestedProfName=request.Get.get('profName')
	# requestedClassName=request.Get.get('className')
	# requestedText=request.Get.get('text')

	if Professor.objects.filter(profName=requestedProfName.exists()):
		new_prof = false
	else:
		new_prof = true
        prof = Professor(profName = requestedProfName)
        prof.save()

	 # return JsonResponse({"new_prof": new_prof, "prof_name": requestedProfName, "questions": requestedQuestion}
	 # {"id": int, "text": String})

	return JsonResponse({'new_prof': new_prof, 'prof_name': requestedProfName, 'id':prof.id})


def receiveQuestion (request):
	requestedProfName=request.Get.get('profName')
	prof = Professor.object.get(profName=requestedProfName)
	requestedClassName=request.Post.get('className')
	requestedText = request.Post.get('text')
	requestedOptions = request.Post.get('options')
	correctNumber = int(request.Post.get('correct'))

	requestedQuestion = Question(className = requestedClassName, professor=prof, text=requestedText,active=true)
	requestedQuestion.save()

	for index in range(len(requestedOptions)):
        requestedOption = Option(question= requestedQuestion,sequence=index, text=requestedOptions[index], correct =false)
        if index==correctNumber:
        	requestedOption.correct = true
        requestedOption.save()

    return JsonResponse({'prof_name': requestedProfName, 'prof':prof, 'question_name'=requestedQuestion.profName, 'question'=requestedQuestion})

