from django.shortcuts import render,redirect,render_to_response,HttpResponse
from django.http import JsonResponse

import json
from django.views.decorators.csrf import csrf_protect

from .models import User,Room,Message
from django.http import HttpResponseRedirect
from .forms import UserForm
from django.core import serializers




def get_login(request):
	form = UserForm(request.POST)
	if form.is_valid():
		form.save(commit =False)
		print(request.POST['login'])

		if not (User.objects.filter(login = request.POST['login']).exists()):
			user = form.save(commit =False)
			user.login = form.cleaned_data['login']
			user.password = form.cleaned_data['password']
			user.IdRoom = Room.objects.get(index = 1)
			user.save()
		else:
			user = User.objects.get(login = request.POST['login'])

			if user.password == form.cleaned_data['password']:
				user.IdRoom = form.cleaned_data['IdRoom']
				
				user.save()
			else:
				return render(request,'register.html', {'form': form})

		form = UserForm()
		request.session['user_data'].update({user.id: request.POST['login']})
		request.session.modified = True
		return redirect('./general_page/'+str(user.id)+'/')
	else:
		form = UserForm()
		return render(request, 'register.html', {'form': form})



def send_message(request):
	if request.session['user_data']:
		sender = User.objects.get(login = request.session['user_data'].get(url_id(request.get_full_path())))
		Messages = Message.objects.filter(RoomId = sender.IdRoom)
	else:
		return redirect('/Step1/')
		
	if request.method == 'POST' and request.POST.get('msgbox') and request.is_ajax():
		message = str(request.POST.get('msgbox',None))
		print(message)
		status = False
		RoomId = sender.IdRoom
		message_exp = Message.create(message,sender,status,RoomId)
		message_exp.save()
		return JsonResponse({'msg':message})

	else:
		return render(request,'message.html',{'form':['Your account:',sender.login,'Your Room:',sender.IdRoom],'id':sender.id})
	
def CreateRoom(request):
	if request.POST:
		try:
			if request.POST['NewRoom']:
				new_room = Room.create(request.POST['NewRoom'])
				new_room.save()
				return redirect('/logout/')
		except:
			return render(request,'message.html',{'errors':['invalid input or size']})

def Messages(request):

	url = request.get_full_path()
	url = url[10:len(url)-1]
	sender = User.objects.get(login = request.session['user_data'].get(url))
	m = list(Message.objects.filter(RoomId = sender.IdRoom))

	return render(request,'allmes.html',{'messages':m})

def logout(request):
	if request.GET:

		user = User.objects.get(id = request.GET['user_id'])
		Message.objects.filter(user_name = user).filter(RoomId = user.IdRoom).delete()
		del request.session['user_data'][request.GET['user_id']]

	return redirect('/Step1/')

def url_id(url):
	url = url[20:len(url)-1] 
	print(url)

	return url
			
			



			

		
		


	



	


		
	