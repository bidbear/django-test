from django.shortcuts import render
# from django.http import HttpResponse
from .models import Question
from django.http import Http404
# Create your views here.
def index(request):
	latest_question_list = Question.objects.order_by('pub_date')[:5] 
	context = {'latest_question_list':latest_question_list}
	return render(request,'polls/index.html',context)

def detail(request,question_id):
	# return HttpResponse('you looking at question %s'%(question_id,))
	try:
		question = Question.objects.get(pk=question_id)
	except Question.DoesNotExist:
		raise Http404('404')
	return render(request,'polls/detail.html',{'question':question})

def results(request,question_id):
	response = 'you looking at result question %s'
	return HttpResponse(response % question_id)

def vote(request,question_id):
	return HttpResponse('you voting on questuon %s' % question_id)
