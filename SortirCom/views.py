from django.shortcuts import render
from django.http import  HttpResponse
# Create your views here.


def workspace(request, varTest):
    return HttpResponse("Variable passez en get : {0}".format(varTest))
