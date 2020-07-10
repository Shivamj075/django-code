from django.db import models

# Create your models here.

class Airport(models.Model):
	code = models.CharField(max_length=3)
	city = models.CharField(max_length=64)


	def __str__(self):
		return '{city} - {code} '.format(city=self.city,code=self.code)

class Flight(models.Model):
	# 1
	# origin = models.CharField(max_length = 64)
	# destination = models.CharField(max_length = 64)
	# duration = models.IntegerField()

	# # 2
	origin = models.ForeignKey(Airport,on_delete=models.CASCADE,related_name="departures")
	destination = models.ForeignKey(Airport,on_delete=models.CASCADE,related_name="arrivals")
	duration = models.IntegerField()



	def __str__(self):
		return '{id} - {origin} to {destination}'.format(id=self.id,origin=self.origin,destination=self.destination)

class Passenger(models.Model):
	first = models.CharField(max_length=64)
	last = models.CharField(max_length=64)
	flights = models.ManyToManyField(Flight,blank=True,related_name="passengers") #one pass might be asso. with many flight ad vice-versa & blank=true just allows tha may be passendger not in any flight

	def __str__(self):
		return '{first} {last}'.format(first=self.first,last=self.last)