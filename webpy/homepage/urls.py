from django.urls import path
from . import views

#django app, part 3
#Sets the application namespace so we can use the {% url %} template tag. 
app_name = 'homepage'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
]