from custom.ucasal2.endpoints import titulos

app_name = 'ucasal2'

urlpatterns = [
    *titulos.routes,
]
