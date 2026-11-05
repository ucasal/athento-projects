from custom.ucasal2.endpoints import programas, titulos

app_name = 'ucasal2'

urlpatterns = [
    *titulos.routes,
]
