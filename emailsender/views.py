from django.shortcuts import render, redirect
from django.http import HttpResponse
from emailsender.models import EmailForm
from django.core.mail import EmailMessage
# Create your views here.


def email_body(request):
    if request.method == 'POST':
        email_from = request.POST.get('form-email')
        to_email = request.POST.get('to-email')
        subject = request.POST.get('subject')
        email_body = request.POST.get('email-body')
        email_date = request.POST.get('email-date')
        email_from_save = EmailForm.objects.create(form_email=email_from, to_email=to_email, subject=subject, body=email_body, date=email_date)
        email_from_save.save()
        email = EmailMessage('Hello', 'Body goes here', 'abir.hasan@divine-it.net',
                             ['abirhasan.raj.bd@gmail.com', '17103272@iubat.edu'], ['bcc@example.com'],
                             reply_to=['another@example.com'], headers={'Message-ID': 'foo'})
        email.send()
        return redirect('email-list')
    return render(request, 'email_body.html')


def email_list(request):
    obj = EmailForm.objects.all()
    context = {
        'obj': obj
    }
    return render(request, 'email_list.html', context=context)


def delete_email(request, pk):
    obj = EmailForm.objects.get(id=pk)
    obj.delete()
    return redirect('email-list',)
