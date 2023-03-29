from django.urls import path
from app.views import *

app_name='virat'

urlpatterns=[
    path('virat/',virat,name='virat'),
]
