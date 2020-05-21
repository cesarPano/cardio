from django.contrib import admin
from .models import Desfibrilador, Transmision, Revision, Tecnico, Tipo_Desfibrilador, Tipo_Revision

class DesfibriladorAdmin(admin.ModelAdmin):
	fields = ['tipo', 'localizacion', 'responsable', 'imagen']
admin.site.register(Desfibrilador, DesfibriladorAdmin)

class TransmisionAdmin(admin.ModelAdmin):
	fields = ['desfibrilador', 'trans_date', 'trans_text']
admin.site.register(Transmision, TransmisionAdmin)

class RevisionAdmin(admin.ModelAdmin):
	fields = ['desfibrilador', 'tecnico', 'rev_tipo', 'rev_date']
admin.site.register(Revision, RevisionAdmin)

class TecnicoAdmin(admin.ModelAdmin):
	fields = ['tecnico_nombre']
admin.site.register(Tecnico, TecnicoAdmin)

class Tipo_DesfibriladorAdmin(admin.ModelAdmin):
        fields = ['tipo_desfibrilador']
admin.site.register(Tipo_Desfibrilador, Tipo_DesfibriladorAdmin)

class Tipo_RevisionAdmin(admin.ModelAdmin):
        fields = ['tipo_revision']
admin.site.register(Tipo_Revision, Tipo_RevisionAdmin)

