from django.http import Http404
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Desfibrilador

def index(request):
	latest_desfibrilador_list = Desfibrilador.objects.order_by('-id')[:10]
	template = loader.get_template('control/index.html')
	context = {'latest_desfibrilador_list': latest_desfibrilador_list,}
	return HttpResponse(template.render(context, request))

def detail(request, id_desfibrilador):
	try:
		desfibrilador = Desfibrilador.objects.get(pk=id_desfibrilador)
	except Desfibrilador.DoesNotExist:
		raise Http404("No existe ese desfibrilador")
	return render(request, 'control/detail.html', {'desfibrilador': desfibrilador})

def results(request, id_desfibrilador):
	return HttpResponse("Estos son los resultados del desfibrilador %s." % id_desfibrilador)

def login(request):
        return HttpResponse("Esto es la página de logueo.")
