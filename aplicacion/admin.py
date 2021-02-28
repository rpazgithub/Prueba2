from django.contrib import admin
from .models import EtapaProyecto, ActividadEconomica, ProyectoEmpresarial, TamanoEmpresa, TipoSociedad, Empresa, InformacionContactoEmpresa, Integrante, ModeloNegocio


admin.site.register(EtapaProyecto)
admin.site.register(TipoSociedad)
admin.site.register(ModeloNegocio)


class ActividadEconomicaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

class ProyectoEmpresarialAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha_inicio', 'persona_contacto')

class TamanoEmpresaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('nit', 'razon_social')

class InformacionContactoEmpresaAdmin(admin.ModelAdmin):
    list_display = ('celular', 'correo_electronico')

class IntegranteAdmin(admin.ModelAdmin):
    list_display = ('nombre_completo', 'cargo', 'profesion')





admin.site.register(ActividadEconomica, ActividadEconomicaAdmin)
admin.site.register(ProyectoEmpresarial, ProyectoEmpresarialAdmin)
admin.site.register(TamanoEmpresa, TamanoEmpresaAdmin)
admin.site.register(Empresa, EmpresaAdmin)
admin.site.register(InformacionContactoEmpresa, InformacionContactoEmpresaAdmin)
admin.site.register(Integrante, IntegranteAdmin)

