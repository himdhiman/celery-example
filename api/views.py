from django.shortcuts import render
from django.http import request
from rest_framework.response import Response
from rest_framework.decorators import api_view
from api import tasks
from django.views.generic import DetailView


def index(request, id):
    tasks.showNumbers.delay(id)
    return render(request, 'index.html', context = {"text" : "Click to Start"})
