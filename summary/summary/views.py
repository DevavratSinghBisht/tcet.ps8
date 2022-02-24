from django.shortcuts import render
from django.http.response import HttpResponse
from django.contrib import messages
from .utils import SummaryForm
from .models import summarizer

def summary(request):
    if request.method == 'GET':
        
        context ={}
        context['form']= SummaryForm()
        return render(request, "index.html", context)

    elif request.method == 'POST':
        text = request.POST.get('text', False)
        messages.info(request, summarizer.summarize(text))
        return render(request, "summary.html")
