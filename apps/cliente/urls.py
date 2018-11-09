from django.conf.urls import url

from apps.cliente.views import index_cliente, formulario_view
urlpatterns = [
    url(r'^index$', index_cliente),
    url(r'^nuevo$', formulario_view),


]