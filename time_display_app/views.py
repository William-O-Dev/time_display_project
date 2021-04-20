from django.shortcuts import render

from time import gmtime, strftime
    
def index(request):
    context = {
        "date_long": strftime("%A, %B %d, %Y", gmtime()),
        "date": strftime("%m.%d.%Y", gmtime()),
        "date_europe": strftime("%d.%m.%Y", gmtime()),
        "time": strftime("%I:%M %p %Z", gmtime()),
        "military_time": strftime("%H:%M %p", gmtime()),

    }
    return render(request,'index.html', context)

