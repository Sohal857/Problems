from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'country'



class State(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'state'

class Person(models.Model):
    name = models.CharField(max_length=124)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, blank=True, null=True)
    state = models.ForeignKey(State, on_delete=models.SET_NULL, blank=True, null=True)
    class Meta:
        db_table = 'enhanced_user'
