from datetime import datetime
from django.http import HttpResponse


#primer vista
def saludo(request):
    return HttpResponse("hola weon")
def edadEnAnios(request, edad, anio):
    cantDeAnios=anio-2022
    edadFutura=edad+cantDeAnios
    vista="""<h1>
    en el año %s tendras %s años
    </h1>
    """ %(anio, edadFutura)
    return HttpResponse(vista)

def localFecha(request):
    fechaActual=datetime.now()
    formis="""
    <h1>
    La fecha es %s
    </h1>
    """ % fechaActual

    return HttpResponse(formis)