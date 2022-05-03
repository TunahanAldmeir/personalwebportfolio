
from django.shortcuts import render

from django.views.generic import ListView

from posts.models import user,about
from django.core.mail import send_mail


class File_kul(ListView):
    template_name = "index.html"
    model = user
    context_object_name = "users"

    def get_context_data(self, *, object_list=None, **kwargs):
        context=super(File_kul, self).get_context_data(**kwargs)
        return context

class aboutview(ListView):
    template_name = "about.html"
    model = about
    context_object_name = "users"

    def get_context_data(self, *, object_list=None, **kwargs):
        context=super(aboutview, self).get_context_data(**kwargs)
        return context

def contactview(request):
    if request.method=="POST":
        message_name=request.POST['message-name']
        message_phone=request.POST['message-phone']
        message_email=request.POST['message-email']
        message_abouts=request.POST['message-abouts']
        message=request.POST['message']
        email_body =("name:"+message_name ,"phone_number: "+message_phone ,"from_email: "+message_email ,"Subject: "+message_abouts)
        #Send Email
        send_mail(
            email_body,
            message,
            'tunahanaldemir46@gmail.com',
            [message_email]
            )

        return render(request, 'contact.html', {'message_name':message_name})
    else:
        return render(request, 'contact.html', {})







