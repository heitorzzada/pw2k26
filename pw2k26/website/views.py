from django.views.generic import TemplateView
from django.shortcuts import redirect
from .models import Agendamento
from django.contrib import messages
from datetime import time, datetime, timedelta
from django.contrib import messages

class Index(TemplateView):
    template_name = "website/inicio.html"


class Servico(TemplateView):
    template_name = "website/servico.html"


class Contato(TemplateView):
    template_name = "website/contato.html"


class Agendar(TemplateView):
    template_name = "website/agendar.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        horarios = []
        inicio = datetime.strptime("09:00", "%H:%M")
        fim = datetime.strptime("20:00", "%H:%M")

        while inicio <= fim:
            horarios.append(inicio.strftime("%H:%M"))
            inicio += timedelta(minutes=30)

        context['horarios'] = horarios
        return context
    def post(self, request, *args, **kwargs):
        nome = request.POST.get('nome')
        servico = request.POST.get('servico')
        data = request.POST.get('data')
        hora = request.POST.get('hora')

        data_hora = f"{data} {hora}"

        data_final = datetime.strptime(data_hora, "%Y-%m-%d %H:%M")

        if Agendamento.objects.filter(data=data_final).exists():
            from django.contrib import messages
            messages.error(request, "Horário já ocupado ❌")
            return redirect('agendar')

        Agendamento.objects.create(
            nome=nome,
            servico=servico,
            data=data_final
    )

        messages.success(request, "Agendado com sucesso ✅")
        return redirect('agendar')


class Barbeiro(TemplateView):
    template_name = "website/barbeiro.html"