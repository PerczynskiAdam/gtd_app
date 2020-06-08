from django.db import models
from datetime import datetime
# Create your models here.
class Case(models.Model):
   case_text = models.CharField(max_length = 200, verbose_name = "Case")
   comp_case = models.BooleanField('complete case', default=False)

   def __str__(self):
      return self.case_text

class Result(models.Model):
   res_text = models.CharField(max_length = 200, verbose_name = "Result")
   res_comp = models.BooleanField('complete result', default=False)
   case = models.ForeignKey(Case, on_delete = models.CASCADE, default = 1)
   def __str__(self):
      return self.res_text

class Action(models.Model):
   act_text = models.TextField(verbose_name = "Action")
   act_comp =models.BooleanField('complete action', default=False)
   case = models.ForeignKey(Case, on_delete = models.CASCADE, default = 1)

   def __str__(self):
      return self.act_text