from django.db import models

class Message(models.Model):
	text = models.TextField(max_length =1000)
	status = models.BooleanField(help_text = "Read/not",default = 0)
	user_name = models.ForeignKey('User')
	RoomId = models.ForeignKey('Room', default = 0)
	created = models.DateTimeField(auto_now_add =True,null = True,blank = True)
	updated = models.DateTimeField(auto_now = True)

	@classmethod
	def create(cls,text,user_name,status,RoomId):
		message = cls(text = text,user_name = user_name,status =status , RoomId = RoomId)
		return message

	def __str__(self):
		return self.text


class User(models.Model):
	login = models.CharField(max_length = 20)
	IdRoom = models.ForeignKey('Room',default = 0)
	password = models.CharField(max_length = 20 ,  default= None  , blank =True)
	def __str__(self):
		return self.login

class Room(models.Model):
	index = models.CharField(max_length = 3, default = 0)
	def __str__(self):
		return self.index
	@classmethod
	def create(cls,index):
		room = cls(index = index)
		return	room
	



	









# Create your models here.
