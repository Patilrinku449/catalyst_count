from django.db import models
from django.shortcuts import get_list_or_404

# Create your models here.
class File(models.Model):
    existingPath = models.CharField(unique=True, max_length=100)
    name = models.CharField(max_length=50)
    eof = models.BooleanField()









# # class FILTER(models.Model):
#     """This Model represents a Patient class.
#
#     :type firstname: string
#     :param firstname: the firstname of the patient
#
#     :type lastname: string
#     :param lastname: the lastname of the patient
#
#     :type email: string
#     :param email: the email of the patient
#     """
#
#     # firstname = models.CharField(max_length=250)
#     # lastname = models.CharField(max_length=250)
#     # email = models.CharField(max_length=250)
#     # age = models.IntegerField(null=True, blank=True)
#     # location = models.CharField(max_length=250, null=True, blank=True)
#
#     # def __str__(self):
#     #     """Return firstname and last name."""
#     #     return " {}-{} ".format(self.firstname, self.lastname)
