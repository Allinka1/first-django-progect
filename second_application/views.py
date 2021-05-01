from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def first_second_func(response):
    return HttpResponse("Hello, from first_second_func")


def second_second_func(response):
    return HttpResponse("Hello, from second_second_func")


def third_second_func(response):
    return HttpResponse("Hello, from third_second_func")
