from django import forms
from django.forms.widgets import RadioFieldRenderer
from django.utils.encoding import force_unicode
from django.utils.safestring import mark_safe

from django.forms.extras.widgets import SelectDateWidget

from demo.prpv.models import TCommonTypes, OValidationTable, TStatutOrg, OStadeDev, MDetermination

class MyCustomRenderer( RadioFieldRenderer ):
    def render( self ):
        """Outputs a series of <div></div> fields for this set of radio fields."""
        return( mark_safe( u''.join( [ u'<div id=%s>%s</div>' % (w.name,force_unicode(w.value)) for w in self] )))


class SearchObservationsForm(forms.Form):
    country_choices = (
        (214, 'Comoros'),
        (206, 'Madagascar'),
        (47, 'Mauritius'),
        (173, 'Reunion'),
        (62, 'Seychelles'),
    )
    validate_choices = ()
    for v in OValidationTable.objects.raw('SELECT * from o_validation_table'):
        validate_choices += (v.id_validation_state_pk, v.label_validation_state),
    
    types_choices = ()
    for t in TCommonTypes.objects.raw ('SELECT id_common, display_label from t_common_types'):
         types_choices += (t.id_common, t.display_label),
    
    countries = forms.ChoiceField(choices=country_choices, label='Pays', widget = forms.RadioSelect()) #renderer=MyCustomRenderer
    types = forms.ChoiceField(choices=types_choices, label="Type d'organismes")
    valid = forms.ChoiceField(choices=validate_choices, label="Etat de validation")

class JQueryUIDatepickerWidget(forms.DateInput):
    def __init__(self, **kwargs):
        super(forms.DateInput, self).__init__(attrs={"size":10, "class": "dateinput"}, **kwargs)

    class Media:
        css = {"all":("http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.6/themes/redmond/jquery-ui.css",)}
        js = ("http://ajax.googleapis.com/ajax/libs/jquery/1.4.3/jquery.min.js",
              "http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.6/jquery-ui.min.js",)
    
class AddObservationsForm(forms.Form):
    # choices building
    country_choices = (
        (214, 'Comoros'),
        (206, 'Madagascar'),
        (47, 'Mauritius'),
        (173, 'Reunion'),
        (62, 'Seychelles'),
    )
    
    statut_choices = ()
    for s in TStatutOrg.objects.raw('SELECT id_statut_org_pk, nom_statut_org FROM t_statut_org WHERE id_statut_org_pk NOT IN (1,4)'):
        statut_choices += (s.id_statut_org_pk, s.nom_statut_org, s.nom_statut_org.replace(' ', '-').lower() ),
    
    dvlpmt_choices = ()
    for d in OStadeDev.objects.raw('SELECT id_stad_dev_pk, nom_stade_dev FROM o_stade_dev'):
        dvlpmt_choices += (d.id_stad_dev_pk, d.nom_stade_dev),
    
    method_choices = ()
    for m in MDetermination.objects.raw('SELECT id_m_ident_pk, nom_m_ident FROM m_determination'):
        method_choices += (m.id_m_ident_pk, m.nom_m_ident), 
    
    ##########fields definition#############
    #context
    lot = forms.CharField(label="Reference lot") 
    date_obs = forms.DateField(label="Date de l'observation", widget = forms.DateInput(attrs={"class": "calendar"}))
    country = forms.ChoiceField(choices=country_choices, label='Pays', widget = forms.RadioSelect())
    region = forms.CharField(label="Region", required = False)
    city = forms.CharField(label="Localite", required = False)
    observer = forms.CharField(label="Observateur")
    obs_comments = forms.CharField(label="Commentaires", widget = forms.Textarea())
    #organism
    organism_name = forms.CharField(label="Nom scientifique de l'organisme observe")
    organism_type = forms.ChoiceField(choices=statut_choices, label='Organisme observe en tant que', widget = forms.RadioSelect())
    organism_dvlpmt = forms.ChoiceField(choices=dvlpmt_choices, label='Stade de developpement', widget = forms.RadioSelect())
    user_determination = forms.CharField(label="Determinateur")
    date_determination = forms.DateField(label="Date de determination",  widget = forms.DateInput(attrs={"class": "calendar"}))
    method_determination = forms.ChoiceField(choices=method_choices, label='methode de determination', widget = forms.Select())
    organism_comments = forms.CharField(label="Commentaires", widget = forms.Textarea())
    #interception
    interception = forms.BooleanField(label="Observation d'interception") 

    
