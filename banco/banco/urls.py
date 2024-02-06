from django.contrib import admin
from django.urls import path
from cuenta.views import CuentaList, CuentaDeposito, CuentaRetiro, CuentaTransferencia

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', CuentaList.as_view()),
    path('depositar', CuentaDeposito),
    path('retirar', CuentaRetiro),
    path('transferir', CuentaTransferencia),
]
