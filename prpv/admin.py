from django.contrib import admin
from demo.prpv.models import GPays, TStatutOrg, TCommonTypes, TOrganismeTaxo, OObservation, OOrganismeObserve

class TOrganismeTaxoAdmin(admin.ModelAdmin):
    list_display = ('id_org_pk', 'nom_scientifique', 'provisory_name', 'referent_synonyme', 'date_saisie_org', 'id_statut_fk', 'code_sp2000')
    search_fields = ('nom_scientifique', 'id_org_pk')
    list_filter = ('date_saisie_org','id_statut_fk',)

admin.site.register(GPays)
admin.site.register(TStatutOrg)
admin.site.register(TCommonTypes)
admin.site.register(TOrganismeTaxo, TOrganismeTaxoAdmin)
admin.site.register(OObservation)
admin.site.register(OOrganismeObserve)
#admin.site.register(Book)
