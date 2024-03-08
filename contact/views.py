from django.shortcuts import render,redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm
# Create your views here.
def contact(request):
    contact_form = ContactForm()
    if request.method == 'POST':
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name','')
            mail = request.POST.get('mail','')
            content = request.POST.get('content','')
            
            # Creamos el correo 
            mail = EmailMessage(
                "Mensage desde el Portafolio",# Asunto
                f"De {name} \n y su correo es {mail} \n{content}",#Mensaje
                "portafolio.com",#Email de origen 
                ["alexanderzelarayan6@gmail.com"],# email de destino
                reply_to=[mail]
            )
            # lo enviamos y redireccionamos 
            try:
                mail.send()
                # si todo va bien enviamos y redireccionamos a OK
                return redirect(reverse('contact:contact')+"?ok")
            except:
                # si no salio bien redireccionamos al fail
                return redirect(reverse('contact:contact')+"?fail")
                
    return render(request,'contact/contact.html',{"form":contact_form})