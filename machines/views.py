from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):  # HttpRequest
    return HttpResponse('''<!DOCTYPE html>
    <html>
    <head>
             <title>СТРАНИЧКА</title>
    </head>
    <body>
            <h1 style="color:Red;">Слишком много кода</h1>
            <h2 style="color:Red;">Слишком много кода</h2>
            <h3 style="color:Red;">Слишком много кода</h3>
            <h4 style="color:Red;">Слишком много кода</h4>
            <h4 style="color:Red;">Слишком много кода</h4>
            <h3 style="color:Red;">Слишком много кода</h3>
            <h2 style="color:Red;">Слишком много кода</h2>
            <h1 style="color:Red;">Слишком много кода</h1>
            <h1 style="color:Red;">Слишком много кода</h1>
            <h2 style="color:Red;">Слишком много кода</h2>
            <h3 style="color:Red;">Слишком много кода</h3>
            <h4 style="color:Red;">Слишком много кода</h4>
            <h4 style="color:Red;">Слишком много кода</h4>
            <h3 style="color:Red;">Слишком много кода</h3>
            <h2 style="color:Red;">Слишком много кода</h2>
            <h1 style="color:Red;">Слишком много кода</h1>
            <h1 style="color:Red;">Слишком много кода</h1>
            <h2 style="color:Red;">Слишком много кода</h2>
            <h3 style="color:Red;">Слишком много кода</h3>
            <h4 style="color:Red;">Слишком много кода</h4>
            
    </body>
    </html>''')
#def index(request):  # HttpRequest
#    return HttpResponse("Страница приложения Machines.")
def indexe(request):  # HttpRequest
    return HttpResponse("Главное меню.")