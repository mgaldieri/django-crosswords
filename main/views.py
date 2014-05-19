from django.shortcuts import render
from utils.crosswordsgen import Crossword
import gspread


def index(request):
    render(request, 'index.html', {})