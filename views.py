from django.shortcuts import render
from django.http import HttpResponse

def ok(request):
    return render(request, 'index.html')  

def analyze(request):
    # Get the text from the request
    djtext = request.GET.get('text', 'default')
    removepun = request.GET.get('removepun', 'off')
    
    print("Input Text:", djtext)
    print("Remove Punctuation Option:", removepun) 
    punctuations = '''. , ; : ' " ! ? - – — ( ) [ ] { } / \ | @ # $ % ^ & * _ ~'''
    analyzed = ""
    for char in djtext:
            if char not in punctuations:
                analyzed += char

    params = {'purpose': 'Removed punctuation', 'analyzed_text': analyzed} 
    return render(request, 'analyze.html', params)  

  
