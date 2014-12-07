from django.shortcuts import render_to_response as render

def home_page(request):
    #variableDictionary = {'cssVariable' : '/home/swashy/Scripts/html/scootersite/static/css/styles.css'}
    return render('index.html')
