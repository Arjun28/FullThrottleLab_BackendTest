from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
import pprint
from collections import OrderedDict 
from .models import Sessions, Members

def index(request):
   return HttpResponse('<h3>Hello FT LAB.</h3><br/><p>USE LINK : <a href = "http://127.0.0.1:8000/getall/">http://127.0.0.1:8000/getall/</a></p>') 

def FetchJSON(request):
	members = Members.objects.all()
	membersDict = OrderedDict()
	membersDict['ok']=True
	membersList=[]
	for member in members:
		sessionPairs = []
		membersList.append({'id' : member.text_id, 'real_name' : member.real_name, 'tz' : member.tz, 'activity_periods':sessionPairs})
		for sess in Members.objects.get(id = member.id).sessions_set.all():
			sessionPairs.append({'start_time' : str(sess.start_date).replace('z',''), 'end_time' : str(sess.end_date).replace('z','')})
		membersDict['members'] = membersList
	pprint.pprint(membersDict)
	return JsonResponse(membersDict)