from django.shortcuts import render
import pycountry
import pandas as pd
import plotly.express as px


def home(request):
    return render(request, 'Dashboard.html')
