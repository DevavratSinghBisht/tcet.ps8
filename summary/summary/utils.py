from django import forms
from transformers import pipeline

class SummaryForm(forms.Form): 
    text = forms.CharField(widget=forms.Textarea)

class Summarizer:

    def __init__(self) -> None:
        self.summarizer = pipeline("summarization")

    def summarize(self, article:str, max_length:int = 130, min_length:int = 30) -> str:
        '''
        Function for summarizing an article
        :param article: article to be summarized
        :param max_length: maximum length of the summary
        :param min_length: minimum length of the summary  
        :return: summary text
        '''
        summary = self.summarizer(article, max_length=max_length, min_length=min_length, do_sample=False)
        return summary[0]['summary_text']