from django.db import models

class Clients(models.Model):
	company = models.CharField(max_length = 100)
	address_01 = models.CharField("Suite, Building",max_length = 100)
	address_02 = models.CharField("Street 1", max_length = 100)
	address_03 = models.CharField("Street 2", max_length = 100,  null = 'True', blank ='True' )
	address_04 = models.CharField("City", max_length = 100, null = 'True', blank ='True')
	address_05 = models.CharField("PIN CODE", max_length = 50)
	Tel_No = models.CharField("Telephone Number", max_length = 12, null = 'True', blank ='True')