from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.http import HttpResponseRedirect
from django.db.models import Q

from .models import Action, Result, Case
from .forms import TodoForm

# Create your views here.
def index(request):
   case_list = Case.objects.all()
   result = Result.objects.all()
   action_list = Action.objects.all()

   form = TodoForm()

   return render(request = request,
   template_name = 'todo/index.html',
   context = {'action_list': action_list,
   'result': result,
   'case_list': case_list,
   'form': form})


@require_POST
def addCase(request):
   try:
      form = TodoForm(request.POST)

      if form.is_valid():
         new_case = Case(case_text = request.POST['text'])
         new_case.save()

      return redirect('index')
   except Exception as e:
      print(str(e))

@require_POST
def addAction(request, text):
   form = TodoForm(request.POST)
   case = Case.objects.get(case_text = text)

   if form.is_valid():
      new_action = Action(act_text = request.POST['text'], case = case)
      new_action.save()

      return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@require_POST
def addResult(request, text):
   form = TodoForm(request.POST)
   case = Case.objects.get(case_text = text)

   if form.is_valid():
      new_result= Result(res_text = request.POST['text'], case = case)
      new_result.save()

      return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def Cases(request, text):
   sprawy = [s.case_text for s in Case.objects.all()]#tworze listę spraw (tekst)
   form = TodoForm()
   if text in sprawy:#jeśli text - zmienna pochodząca z index.html (sprawa) jest w zminnej sprawy
      match_case = Case.objects.filter(case_text=text)
      match_result = Result.objects.filter(case__case_text=text)#zwroc obiekty z modelu Result dla których zmienna case jest rowna tekstowi w klucuz obcym w Cases
      match_action = Action.objects.filter(case__case_text=text)

      return render(request,
      "todo/result.html",
      {"match_case": match_case,
      "match_result": match_result,
      "match_action": match_action,
      "form": form})




def completeCase(request, case_id):
   case = Case.objects.get(pk=case_id)
   if case.comp_case:
      case.comp_case = False
      case.save()
   else:
      case.comp_case = True
      case.save()

   return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def completeResult(request, res_id):
   result = Result.objects.get(pk=res_id)
   if result.res_comp:
      result.res_comp = False
      result.save()
   else:
      result.res_comp = True
      result.save()

   return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def completeAction(request, act_id):
   action = Action.objects.get(pk=act_id)
   if action.act_comp:
      action.act_comp = False
      action.save()
   else:
      action.act_comp = True
      action.save()

   return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def deleteCompCase(request):
   if request.method == 'POST':
      Case.objects.filter(comp_case = True).delete()
      return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def deleteCompResults(request, text):
   if request.method == 'POST':
      Result.objects.filter(case__case_text = text, res_comp = True).delete()
      return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def deleteCompActions(request, text):
   if request.method == 'POST':
      Action.objects.filter(case__case_text = text, act_comp = True).delete()
      return HttpResponseRedirect(request.META.get('HTTP_REFERER'))





