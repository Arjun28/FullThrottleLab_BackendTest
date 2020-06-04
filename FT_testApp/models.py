from django.db import models

class Members(models.Model):
	text_id = models.CharField(max_length=10)
	real_name = models.CharField(max_length=30)
	tz = models.CharField(max_length=30)#Continent/State 

class Sessions(models.Model):
	text_id = models.ForeignKey(Members, on_delete=models.CASCADE)
	start_date = models.DateTimeField()
	end_date = models.DateTimeField()