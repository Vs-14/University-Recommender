from django.shortcuts import render

# Create your views here.
def survey_view(request):
    return render(request, 'survey.html')

def thanks_view(request):
    return render(request, 'thanks.html')