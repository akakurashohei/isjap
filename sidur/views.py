from django.shortcuts import render, redirect
from django.core.mail import EmailMessage, send_mail
from django.contrib import messages
from fletta.models import Fletta

# Create your views here.

def heima(request):
    return render(request, 'sidur/heima.html')


def um_isjap(request):
    return render(request, 'sidur/um_isjap.html')


def hafa_samband(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        reply_body = 'Titill - 件名：' + subject + '\nNafn - お名前：' + name + '\nNetfang - Eメールアドレス：' + email + '\nSkilaboð - お問い合わせ内容：\n' + message
        bcc = 'isjap.ordabok@gmail.com'

        email = EmailMessage(
            '【Ísjap】Skilaboðin hafa verið send. - お問い合わせ、ありがとうございます。',
            'Takk fyrir að hafa samband.\nSkilaboðin þín eru hér fyrir neðan.\n\n' + reply_body + '\n\nVið munum svara þér eins fljótt og auðið er.\n\n-------\n\nお問い合わせ、ありがとうございます。\nお送り頂いた内容は、以下の通りです。\n\n' + reply_body + '\n\nご返信まで、しばしお待ちください。\n\nÍsjap - Íslensk-japönsk veforðabók - 氷日オンライン辞典',
            'isjap.ordabok@gmail.com',
            [email],
            ['isjap.ordabok@gmail.com'],
        )
        email.send(fail_silently=False)

        messages.success(request, 'Takk fyrir að hafa samband. - お問い合わせ、ありがとうございます。')
        return redirect('hafa_samband')

    return render(request, 'sidur/hafa_samband.html')


def leit(request):
    return render(request, 'leit/nidurstada.html')
