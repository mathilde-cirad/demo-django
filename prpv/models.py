# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models
import django_tables2 as tables

class Fruit(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name

#class used by django_tables2
class ObservationsTable(tables.Table):
    observation = tables.Column(verbose_name='Observations id')
    host = tables.Column(verbose_name='Plantes hotes')
    nom_scientifique = tables.Column(verbose_name='Bacteries')
    commentaire_organisme = tables.Column(verbose_name='Commentaires')
    date_observation = tables.Column(verbose_name="Dates d'observation")
    nom_pays = tables.Column(verbose_name="Pays")
    label_validation_state = tables.Column(verbose_name="Etats de validation")
    class Meta:
        attrs = {'class': 'paleblue'}

#GEOGRAPHIC
class GLocalite(models.Model):
    id_localite_pk = models.IntegerField(primary_key=True)
    nom_localite = models.CharField(max_length=50)
    id_pays_fk = models.IntegerField()
    id_region_fk = models.IntegerField()
    class Meta:
        db_table = u'g_localite'

class GPays(models.Model):
    id_pays_pk = models.IntegerField(primary_key=True, verbose_name='identifiant')
    nom_pays = models.CharField(unique=True, max_length=50, verbose_name='nom du pays')
    class Meta:
        db_table = u'g_pays'
    def __unicode__(self):
        return self.nom_pays

class GRegion(models.Model):
    id_region_pk = models.IntegerField(primary_key=True)
    nom_region = models.CharField(unique=True, max_length=50)
    id_pays_fk = models.IntegerField()
    class Meta:
        db_table = u'g_region'
        
class GLangue(models.Model):
    id_langue_pk = models.IntegerField(primary_key=True)
    nom_langue = models.CharField(unique=True, max_length=50)
    ref_langue = models.CharField(max_length=10)
    class Meta:
        db_table = u'g_langue'
               
#TAXONOMY
class TAssOrgVernaGeo(models.Model):
    id_org_fk = models.IntegerField()
    id_pays_fk = models.IntegerField()
    id_langue_fk = models.IntegerField()
    id_nom_verna_fk = models.IntegerField()
    id_region_fk = models.IntegerField()
    discriminant = models.IntegerField(unique=True)
    class Meta:
        db_table = u't_ass_org_verna_geo'

class TAssocTaxoEspOrg(models.Model):
    id_org_fk = models.IntegerField()
    id_genre_fk = models.IntegerField()
    id_espece_fk = models.IntegerField()
    id_auteur_espece_fk = models.IntegerField()
    class Meta:
        db_table = u't_assoc_taxo_esp_org'

class TAuteur(models.Model):
    nom_auteur = models.CharField(max_length=300)
    id_auteur_pk = models.IntegerField(primary_key=True)
    class Meta:
        db_table = u't_auteur'

class TChaineTaxo(models.Model):
    id_taxon = models.IntegerField(primary_key=True)
    nom_taxon = models.CharField(max_length=200)
    id_niveau_taxon = models.IntegerField()
    id_parent = models.IntegerField()
    old_id_taxon = models.IntegerField()
    old_id_parent = models.IntegerField()
    class Meta:
        db_table = u't_chaine_taxo'

class TCommonTypes(models.Model):
    id_common = models.IntegerField(primary_key=True)
    label = models.CharField(max_length=200, verbose_name = 'nom scientifique')
    #id_niveau_taxo = models.IntegerField()
    display_label = models.CharField(max_length=200, verbose_name = 'nom courrant' )
    class Meta:
        db_table = u't_common_types'
    def __unicode__(self):
        return self.display_label

class TEspeceInfra(models.Model):
    id_espinf_pk = models.IntegerField(primary_key=True)
    nom_espinf = models.CharField(max_length=300)
    old_id = models.IntegerField(unique=True)
    old_id_parent = models.IntegerField()
    name_code = models.CharField(max_length=100)
    class Meta:
        db_table = u't_espece_infra'

class TInfraExtension(models.Model):
    id_org_fk = models.IntegerField()
    id_genre_fk = models.IntegerField()
    id_espece_fk = models.IntegerField()
    id_auteur_espece_fk = models.IntegerField()
    id_type_infra1 = models.IntegerField()
    id_label_infra1 = models.IntegerField()
    id_author_infra1 = models.IntegerField()
    id_type_infra2 = models.IntegerField()
    id_label_infra2 = models.IntegerField()
    id_author_infra2 = models.IntegerField()
    id_infra_parent = models.IntegerField()
    class Meta:
        db_table = u't_infra_extension'

class TMaladie(models.Model):
    nom_maladie = models.CharField(max_length=300)
    abbrev_maladie = models.CharField(max_length=50)
    id_maladie_pk = models.IntegerField(primary_key=True)
    class Meta:
        db_table = u't_maladie'

class TMaladieTransmiseParMode(models.Model):
    id_maladie_fk = models.IntegerField()
    id_mode_transm_fk = models.IntegerField()
    class Meta:
        db_table = u't_maladie_transmise_par_mode'

class TModeTransmission(models.Model):
    nom_mode_transmission = models.CharField(max_length=100)
    id_mode_transmission_pk = models.IntegerField(unique=True)
    class Meta:
        db_table = u't_mode_transmission'

class TNiveauTaxonomique(models.Model):
    id_niveau_taxonomique = models.IntegerField(primary_key=True)
    nom_niveau_taxonomique = models.CharField(unique=True, max_length=100)
    class Meta:
        db_table = u't_niveau_taxonomique'

class TNomVerna(models.Model):
    nom_verna_org = models.CharField(max_length=300)
    id_nom_verna_pk = models.IntegerField(primary_key=True)
    class Meta:
        db_table = u't_nom_verna'

class TOrgInduitMaladie(models.Model):
    id_org_fk = models.IntegerField()
    id_maladie_fk = models.IntegerField()
    class Meta:
        db_table = u't_org_induit_maladie'

class TOrgPossedeOrgReferent(models.Model):
    id_org_synonyme_fk = models.IntegerField()
    id_org_referent_fk = models.IntegerField()
    class Meta:
        db_table = u't_org_possede_org_referent'

class TOrgSubitMaladie(models.Model):
    id_maladie_fk = models.IntegerField()
    id_org_fk = models.IntegerField()
    class Meta:
        db_table = u't_org_subit_maladie'

class TStatutOrg(models.Model):
    nom_statut_org = models.CharField(max_length=50, verbose_name='statut')
    id_statut_org_pk = models.IntegerField(primary_key=True, verbose_name='identifiant')
    class Meta:
        db_table = u't_statut_org'
    def __unicode__(self):
        return self.nom_statut_org

class TCommonTypes(models.Model):
    id_common = models.IntegerField(primary_key=True)
    label = models.CharField(max_length=200)
    #id_niveau_taxo = models.IntegerField()
    display_label = models.CharField(max_length=200)
    class Meta:
        db_table = u't_common_types'

class TOrganismeTaxo(models.Model):
    id_org_pk = models.IntegerField(primary_key=True, verbose_name='identifiant')
    code_oepp = models.CharField(max_length=10, blank=True, null=True)
    code_sp2000 = models.CharField(max_length=10, blank=True, null=True, verbose_name='identifiant catalogue of life')
    nom_scientifique = models.CharField(max_length=500)
    comm_org = models.TextField(blank=True, null=True, verbose_name='commentaires')
    date_saisie_org = models.DateField(verbose_name='date de saisie')
    #date_valid_saisie_org = models.DateField(verbose_name='date de validation')
    initiales_acro = models.CharField(max_length=10)
    orig_org = models.CharField(max_length=300, null=True)
    id_statut_fk = models.ForeignKey(TStatutOrg, db_column = 'id_statut_fk', verbose_name = 'statut')
    #id_user_saisie_fk = models.IntegerField()
    #id_user_validateur_fk = models.IntegerField()
    #nom_correcteur = models.CharField(max_length=300)
    referent_synonyme = models.IntegerField(verbose_name='synonyme referent')
    etat_valid_fiche = models.IntegerField()
    #nom_scientifique_upper = models.CharField(max_length=500)
    #cof_ws_id = models.IntegerField()
    provisory_name = models.BooleanField(verbose_name='nom provisoire')
    #nom_scientifique_html = models.CharField(max_length=512)
    common_types = models.ManyToManyField(TCommonTypes, verbose_name='type')
    class Meta:
        db_table = u't_organisme_taxo'  
    def __unicode__(self):
        return self.nom_scientifique

class TTypeNiv(models.Model):
    nom_type_niv = models.CharField(max_length=30)
    id_type_niv_pk = models.IntegerField(primary_key=True)
    class Meta:
        db_table = u't_type_niv'

#OBSERVATION
class OCompiledDate(models.Model):
    id_compiled_date = models.IntegerField(primary_key=True)
    id_pos_date = models.IntegerField()
    id_kindof_date = models.IntegerField()
    class Meta:
        db_table = u'o_compiled_date'

class OKindofDate(models.Model):
    id_kindof_date = models.IntegerField(primary_key=True)
    label = models.CharField(unique=True, max_length=50)
    class Meta:
        db_table = u'o_kindof_date'

class OObsStadDev(models.Model):
    id_stad_dev_fk = models.IntegerField()
    id_org_obs_fk = models.IntegerField()
    class Meta:
        db_table = u'o_obs_stad_dev'

class OValidationTable(models.Model):
    id_validation_state_pk = models.IntegerField(primary_key=True)
    label_validation_state = models.CharField(unique=True, max_length=100)
    class Meta:
        db_table = u'o_validation_table'
    def __unicode__(self):
        return self.label_validation_state
        
class OObservation(models.Model):
    id_obs_pk = models.IntegerField(primary_key=True)
    identifiant_observation = models.CharField(max_length=255, null=True)
    nature_observation = models.CharField(max_length=255)
    type_milieu = models.CharField(max_length=255)
    date_observation = models.DateField()
    position_date_obs = models.CharField(max_length=50)
    date_saisie_obs = models.DateField()
    id_pays_fk = models.ForeignKey(GPays, db_column='id_pays_fk')    
    date_valid_saisie_obs = models.DateField()
    #id_geo_ref_fk = models.IntegerField()
    #id_region_fk = models.IntegerField()
    #id_localite_fk = models.IntegerField()
    #id_user_recolteur_fk = models.IntegerField()
    #id_user_validateur_fk = models.IntegerField()
    #id_user_redacteur_fk = models.IntegerField()
    comment = models.TextField() #put widget textarea ---> non, seulement dans form
    niveau_conf = models.IntegerField()
    etat_valid_fiche_obs = models.ForeignKey(OValidationTable, db_column='etat_valid_fiche_obs')
    reference_terrain = models.CharField(max_length=500)
    reference_lot = models.CharField(max_length=500)
    is_interception_observation = models.BooleanField()
    class Meta:
        db_table = u'o_observation'
    def __unicode__(self):
        return u'%s %s %s' % (self.identifiant_observation, self.date_observation, self.etat_valid_fiche_obs)

class OObservationMetadata(models.Model):
    id_obs_fk = models.IntegerField()
    id_metadata = models.IntegerField()
    value = models.CharField(max_length=512)
    class Meta:
        db_table = u'o_observation_metadata'

class OOrganeObserve(models.Model):
    nom_organe = models.CharField(max_length=100)
    type_organe = models.CharField(max_length=100)
    id_organe_pk = models.IntegerField(primary_key=True)
    class Meta:
        db_table = u'o_organe_observe'
        
class OOrganismeObserve(models.Model):
    id_org_obs_pk = models.IntegerField(primary_key=True)
    id_org_taxo_fk = models.ForeignKey(TOrganismeTaxo, verbose_name='organisme', db_column='id_org_taxo_fk')
    date_ident_org = models.DateField(auto_now=False)
    #position_date_ident = models.CharField(max_length=50)
    commentaire_organisme = models.TextField(null=True)
    intensite_attaque_organisme = models.IntegerField()
    intensite_attaque_culture = models.IntegerField()
    #id_observation_fk = models.ForeignKey(OObservation, db_column = 'id_observation_fk')    
    #id_user_determ_fk = models.IntegerField()
    categorie = models.CharField(max_length=100)
    #id_m_determ_fk = models.IntegerField()
    id_statut_fk = models.ForeignKey(TStatutOrg, db_column ='id_statut_fk')
    class Meta:
        db_table = u'o_organisme_observe'
    def __unicode__(self):
        return u'%s %s %s' % (self.id_statut_fk, self.id_org_obs_pk, self.id_org_taxo_fk)

class OPosDate(models.Model):
    id_pos_date = models.IntegerField(primary_key=True)
    label_pos_date = models.CharField(unique=True, max_length=100)
    class Meta:
        db_table = u'o_pos_date'
        
class OGeoRef(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    altitude = models.FloatField()
    syst_ref = models.CharField(max_length=50)
    codage = models.CharField(max_length=50)
    id_geo_ref_pk = models.IntegerField(primary_key=True)
    class Meta:
        db_table = u'o_geo_ref'

class OMetadataCatalog(models.Model):
    id_metadata_pk = models.IntegerField(primary_key=True)
    label = models.CharField(max_length=512)
    class Meta:
        db_table = u'o_metadata_catalog'

class OOrganeObsSurOrganisme(models.Model):
    id_organe_obs_sur_organisme = models.IntegerField(primary_key=True)
    id_organe_fk = models.IntegerField()
    id_organisme_observe_fk = models.IntegerField()
    pres_attaque = models.BooleanField()
    degre_attaque = models.IntegerField()
    class Meta:
        db_table = u'o_organe_obs_sur_organisme'

class OStadeDev(models.Model):
    nom_stade_dev = models.CharField(max_length=50)
    id_stad_dev_pk = models.IntegerField(primary_key=True)
    class Meta:
        db_table = u'o_stade_dev'
        
#METHODE DETERMINATION
class MDetermination(models.Model):
    nom_m_ident = models.CharField(max_length=200)
    type_m_ident = models.CharField(max_length=100)
    comm_m_ident = models.CharField(max_length=700)
    date_saisie_m_ident = models.DateField()
    date_valid_saisie_m_ident = models.DateField()
    etat_valid_saisie_m_ident = models.BooleanField()
    id_m_ident_pk = models.IntegerField(primary_key=True)
    class Meta:
        db_table = u'm_determination'
    def __unicode__(self):
        return u'%s' % nom_m_ident




