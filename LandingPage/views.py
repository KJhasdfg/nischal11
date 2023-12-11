from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import AnalyzedTextForm
from .models import AnalyzedText

def LandingPage(request):
    return render(request, 'landingpage.html')
def signin(request):
    return render(request, 'signin.html')
def signup(request):
    return render(request, 'signup.html')



def analyze_text(request):
    if request.method == 'POST':
        form = AnalyzedTextForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            AnalyzedText.objects.create(text=text)
            return redirect('result')
    else:
        form = AnalyzedTextForm()

    return render(request, 'analyze_text.html', {'form': form})

def result(request):
    texts = AnalyzedText.objects.all()
    data = []
    for text in texts:
        if(text.sentiment<=-0.5):
            data.append({"sentimentDescription":"Depressed","sentiment":text.text,"score":text.sentiment})

        elif(text.sentiment<=0):
             data.append({"sentimentDescription":"Sad","sentiment":text.text,"score":text.sentiment})
        elif(text.sentiment<=0.5):
            data.append({"sentimentDescription":"Happy","sentiment":text.text,"score":text.sentiment})
        elif(text.sentiment<=0.2):
            data.append({"sentimentDescription":"psychopath","sentiment":text.text,"score":text.sentiment})
        else:
            data.append({"sentimentDescription":"Very Happy","sentiment":text.text,"score":text.sentiment})

    
    return render(request, 'result.html', {'texts': data})


