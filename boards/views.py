from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from scipy import stats

import csv
import pandas as pd


def home(request):
    print('Home')
    return render(request, 'templates/home.html')


def about(request):
    print('About')
    return render(request, 'templates/about.html')


def contact(request):
    print('Contact')
    return render(request, 'templates/contact.html')

def timeline(request):
    print('Timeline')
    return render(request, 'templates/contact.html')

