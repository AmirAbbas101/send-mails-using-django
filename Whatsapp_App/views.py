from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, "Whatsapp_App/home.html")

def whatsappData(Ph, Message):
    from time import sleep
    import webbrowser as web
    import pyautogui as pg

    Phone = "+92" + Ph
    whatsapp_url = f'https://web.whatsapp.com/send?phone={Phone}&text={Message}'
    web.open(whatsapp_url)
    sleep(20)
    pg.press('enter')


def sendData(request):
    if request.method == 'POST':
        Ph = request.POST['Phone']
        Message = request.POST['Message']
        whatsappData(Ph, Message)
        msg = 'Message has successfully sent..'
        # print(f'phone: {Ph} message : {Message}')
        return render(request, "Whatsapp_App/home.html", {'msg':msg})

    else:
        return HttpResponse("<h1>404 - Not Found: </h1>")