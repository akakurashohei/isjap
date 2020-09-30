from django.shortcuts import render, redirect
from django.contrib import messages
from .models import HafaSamband
from django.core.mail import send_mail
from django.contrib.auth.models import User

# Create your views here.
def inquiry(request):
    if request.method == 'POST':
        lemma_id = request.POST['lemma_id']
        lemma = request.POST['lemma']
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        contact = HafaSamband(lemma_id=lemma_id, lemma=lemma,
        name=name, email=email, subject=subject, message=message)

        send_mail(
            '【Ísjap】 ' + lemma + ' についてのお問い合わせ、ありがとうございます。',
            name + '様\n\n見出し語「' + lemma + '」についてのお問い合わせ、ありがとうございます。\n\n件名：' + subject + '\nお問い合わせ内容：\n' + message +'\n\nご返信まで、しばしお待ちください。\n\nÍsjap - Íslensk-japönsk veforðabók - 氷日オンライン辞典',
            'shw6@hi.is',
            [email],
            fail_silently=False,
        )

        contact.save()
        messages.success(request, 'お問い合わせ、ありがとうございます。')
        return redirect('/fletta/'+lemma_id)
