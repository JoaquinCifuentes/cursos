from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages


def index(request):
    
    if request.method == "GET":
        
        context={
            "cursos" : Cursos.objects.all(),
            "descripciones":Descripciones.objects.all()
        }
        return render(request, "index.html", context)
    elif request.method =="POST":
        errors=Cursos.objects.basic_validator(request.POST)
        if len(errors)>0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect("index")
        else:
            name = request.POST["name"]
            desc = request.POST["desc"]



            Descripciones.objects.create(
                desc = desc
            )
            print(Cursos.objects.last().__dict__)
            Cursos.objects.create(
                name = name,
                desc = Descripciones.objects.last()
            )
            return redirect("index")

def confirm(request, id, name):
    desc = Descripciones.objects.get(id=id)
    name = name
    context={
            "descripcion": Descripciones.objects.get(id=id),
            "name":name,
            "id":id
        }
    return render(request, "destroy.html", context)
def destroy(request, id):
    Descripciones.objects.get(id=id).delete()
    return redirect("index")
# Create your views here.
