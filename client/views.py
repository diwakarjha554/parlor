from django.shortcuts import render

# Create your views here.
def index(request):

    context = {
        'title': 'Advance beauty'
    }

    return render(request, 'base.html', context=context)