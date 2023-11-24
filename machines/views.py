from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):  # HttpRequest
    return HttpResponse('''<!DOCTYPE html>
    <html>
    <head>
             <title>МАШИНКИ</title>
    </head>
    <body style='background-color:Grey;'>
            <h1 style="color:Black;">МАШИНКА1<br>МАШИНКА2<br>МАШИНКА3</h1>
            <a href="../" style="color:red";>Главное Меню:</a>
            
    </body>
    </html>''')
#def index(request):  # HttpRequest
#    return HttpResponse("Страница приложения Machines.")
def mainmenu(request):  # HttpRequest
    return HttpResponse('''<!DOCTYPE html>
        <html>
        <head>
                 <title>Главная</title>
        </head>
        <body style='background-color:Black;'>
                <h1 style="color:Yellow;">ГЛАВНОЕ МЕНЮ</h1>
                <a href="/machines";>Раздел с машинами:</a>

        </body>
        </html>''')