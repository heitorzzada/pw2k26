from django.urls import path
from website.views import Index, Servico, Contato, Agendar, Barbeiro

urlpatterns = [
    path('', Index.as_view(), name='home'),
    path('servico/', Servico.as_view(), name='servico'),
    path('contato/', Contato.as_view(), name='contato'),
    path('agendar/', Agendar.as_view(), name='agendar'),
    path('barbeiro/', Barbeiro.as_view(), name='barbeiro'),
]