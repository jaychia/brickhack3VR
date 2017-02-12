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
	requestedClassName=request.Get.get('className')
	requestedProfName=request.Get.get('profName')
	requestedText = request.Get.get('text')
	requestedOptions = request.Get.get('options')