from django.core import serializers
from django.shortcuts import render
from django.http import JsonResponse

from .constant import types


# Create your views here.

def categories(request):
	data = JsonResponse(types, safe=False)
	return data
	