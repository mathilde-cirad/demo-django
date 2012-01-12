from django.db import models

# Create your models here.

#GEOGRAPHIC
class GPays(models.Model):
    id_pays_pk = models.IntegerField(primary_key=True)
    nom_pays = models.CharField(unique=True, max_length=50)
    #code_pays = models.CharField(max_length=10)
    class Meta:
        db_table = '"geographic"."g_pays"'

        
#TAXONOMY

#these one should be on top of the TOrganismeTaxo class
class TStatutOrg(models.Model):
    nom_statut_org = models.CharField(max_length=50)
    id_statut_org_pk = models.IntegerField(primary_key=True)
    class Meta:
        db_table = u't_statut_org'

class TCommonTypes(models.Model):
    id_common = models.IntegerField(primary_key=True)
    label = models.CharField(max_length=200)
    #id_niveau_taxo = models.IntegerField()
    display_label = models.CharField(max_length=200)
    class Meta:
        db_table = u'taxonomy_common_types'

class TOrganismeTaxo(models.Model):
    id_org_pk = models.IntegerField(primary_key=True)
    code_oepp = models.TextField()
    code_sp2000 = models.TextField()
    nom_scientifique = models.CharField(max_length=500)
    comm_org = models.TextField()
    date_saisie_org = models.DateField()
    date_valid_saisie_org = models.DateField(null=True)
    initiales_acro = models.CharField(max_length=10)
    orig_org = models.CharField(max_length=300, null=True)
    id_statut_fk = models.ForeignKey(TStatutOrg)
    #id_user_saisie_fk = models.IntegerField()
    #id_user_validateur_fk = models.IntegerField()
    #nom_correcteur = models.CharField(max_length=300)
    referent_synonyme = models.IntegerField()
    etat_valid_fiche = models.IntegerField()
    nom_scientifique_upper = models.CharField(max_length=500)
    cof_ws_id = models.IntegerField()
    provisory_name = models.BooleanField()
    nom_scientifique_html = models.CharField(max_length=512)
    common_types = models.ManyToManyField(TCommonTypes)
    class Meta:
        db_table = u'taxonomy.t_organisme_taxo'   

#class TCommonTypesSlots(models.Model):
    #id_common_type = models.IntegerField()
    #id_org_fk = models.IntegerField()
    #class Meta:
        #db_table = u't_common_types_slots'

#OBSERVATION

class OValidationTable(models.Model):
    id_validation_state_pk = models.IntegerField(primary_key=True)
    label_validation_state = models.CharField(unique=True, max_length=100)
    class Meta:
        db_table = u'o_validation_table'
        
class OObservation(models.Model):
    id_obs_pk = models.IntegerField(primary_key=True)
    identifiant_observation = models.CharField(max_length=255, null=True)
    nature_observation = models.CharField(max_length=255)
    type_milieu = models.CharField(max_length=255)
    date_observation = models.DateField()
    position_date_obs = models.CharField(max_length=50)
    date_saisie_obs = models.DateField()
    id_pays_fk = models.ForeignKey(GPays)    
    date_valid_saisie_obs = models.DateField()
    #id_geo_ref_fk = models.IntegerField()
    #id_region_fk = models.IntegerField()
    #id_localite_fk = models.IntegerField()
    #id_user_recolteur_fk = models.IntegerField()
    #id_user_validateur_fk = models.IntegerField()
    #id_user_redacteur_fk = models.IntegerField()
    comment = models.TextField() #put widget textarea ---> non, seulement dans form
    niveau_conf = models.IntegerField()
    etat_valid_fiche_obs = models.ForeignKey(OValidationTable)
    reference_terrain = models.CharField(max_length=500)
    reference_lot = models.CharField(max_length=500)
    is_interception_observation = models.BooleanField()
    class Meta:
        db_table = u'o_observation'
        
        
class OOrganismeObserve(models.Model):
    id_org_taxo_fk = models.ForeignKey(TOrganismeTaxo)
    date_ident_org = models.DateField()
    position_date_ident = models.CharField(max_length=50)
    commentaire_organisme = models.TextField(null=True)
    intensite_attaque_organisme = models.IntegerField()
    intensite_attaque_culture = models.IntegerField()
    id_observation_fk = models.ForeignKey(OObservation)
    #id_org_obs_pk = models.IntegerField(primary_key=True)
    #id_user_determ_fk = models.IntegerField()
    categorie = models.CharField(max_length=100)
    #id_m_determ_fk = models.IntegerField()
    id_statut_fk = models.ForeignKey(TStatutOrg)
    class Meta:
        db_table = u'o_organisme_observe'
