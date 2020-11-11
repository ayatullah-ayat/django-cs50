import datetime
from django.shortcuts import render

# Create your views here.
def index(request):
    now = datetime.datetime.now()
    return render(request, 'newyear/index.html', {
        "is_new_year": now.day == 1 and now.month == 1
    })