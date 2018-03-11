from django.shortcuts import render
from .models import Registrado
from .forms import ContactForm,RegModelForm
# Create your views here.
def inicio(request):
    titulo = "HOLA"
    if request.user.is_authenticated():
        titulo = "Bienvenido %s" %(request.user)
    #print(dir(form)) Checar todos los metodos
    #print(dir(request))
    form = RegModelForm(request.POST or None)
    context = {
        "titulo":titulo,
        "el_form":form,
    }

    if form.is_valid():
        instance = form.save(commit=False)
        nombre = form.cleaned_data.get("nombre")
        email = form.cleaned_data.get("email")
        # print("Hola")
        # print (instance)
        if not instance.nombre:
            instance.nombre = "PERSONA"
        instance.save()

        context = {
            "titulo" : "Gracias %s!" %(nombre)
        }

        if not instance.nombre:
            context={
                "titulo": "Gracias %s" %(email)
            }

            # form_data = form.cleaned_data
            # abc = form_data.get("email")
            # abc2 = form_data.get("nombre")
            # obj = Registrado.objects.create(email=abc,nombre=abc2)
    return render(request,"inicio.html",context)


def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        for key,value in form.cleaned_data.iteritems():
            print key,value
        # for key in form.cleaned_data:
        #     print key
        #     print form.cleaned_data(key)
    context = {
        "form":form,
    }
    return render(request,"forms.html",context)
