


import requests
import json

from django.shortcuts import render,redirect
from django.http.response import HttpResponse
from django.conf import settings


def calculate_anual_salary(employee):
    employee['calculatedAnnualSalary'] = 120*12*employee['hourlySalary']
    return employee

def employees(request,id=None):
    status = 200
    end_point = settings.BASE_API+'Employees'
    response = requests.get(end_point)

    result = json.loads(response.text)
    if id is  not None:
        result = (employee for employee in result if employee['id']==id)
        try:
            result = next(result)
            calculate_anual_salary(result)
        except StopIteration:
            result = None
            status = 404
    else:
        result = list(map(calculate_anual_salary,result))
    return HttpResponse(json.dumps(result),status=status)

