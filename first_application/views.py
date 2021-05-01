from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def first_func(response, first='first'):
    return HttpResponse(f"Hello, from {first} func")


def second_func(response, second='second'):
    return HttpResponse(f"Hello, from {second} func")


def third_func(response, third='third'):
    return HttpResponse(f"Hello, from {third} func")
    

def new_func(response, new='new'):
    return HttpResponse(f"Hello, from {new} func")
