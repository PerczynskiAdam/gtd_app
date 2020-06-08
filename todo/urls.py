"""gtd URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views

urlpatterns = [
    path('cases/<str:text>', views.Cases, name = 'cases'),
    path('', views.index, name = 'index'),
    path('addcase', views.addCase, name = 'addcase'),
    path('completecase/<int:case_id>', views.completeCase, name = 'completecase'),
    path('completeaction/<int:act_id>', views.completeAction, name = 'completeaction'),
    path('completeresult/<int:res_id>', views.completeResult, name = 'completeresult'),
    path('deletecompcase', views.deleteCompCase, name = 'deletecompcase'),
    path('deletecompactions/<str:text>', views.deleteCompActions, name = 'deletecompactions'),
    path('deletecompresults/<str:text>', views.deleteCompResults, name = 'deletecompresults'),
    path('addaction/<text>', views.addAction, name = 'addaction'),
    path('addresult/<text>', views.addResult, name = 'addresult'),
]
