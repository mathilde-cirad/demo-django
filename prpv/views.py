# -*- coding: utf-8 -*- 

# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from django.db import connection
from demo.prpv.forms import SearchObservationsForm, AddObservationsForm
from demo.prpv.models import ObservationsTable, TOrganismeTaxo
from django.core import serializers
# csrf unactivation
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt 
def searchObservations(request):
    if request.method == 'GET':
        form = SearchObservationsForm(request.GET)
        if form.is_valid():
            #clean data
            cd = form.cleaned_data
            common_type = int(cd['types'])
            country = int(cd['countries'])
            valid = int(cd['valid'])
            #request
            cursor= connection.cursor()
            cursor.execute('select * from "observation".display_info_pests(%d, %d, %d) AS (observation int, host character varying(500),nom_scientifique character varying, commentaire_organisme character varying, date_observation date, nom_pays character varying(50), label_validation_state character varying(100))' %(common_type, country, valid)) 
            
            #create a dictionary, so we can call label in the template
            desc = cursor.description #get column names & types
            data = [
                dict(zip([col[0] for col in desc], row))
                for row in cursor.fetchall()
            ]
            #Nb of observation calculation
            nb= len(data)            
            table = ObservationsTable(data, order_by=request.GET.get('sort'))
            table.paginate(page=request.GET.get('page', 1), per_page=25)
                    
            return render_to_response('search_observations_form.html', {'form': form, 'nb':nb, 'table': table}, context_instance = RequestContext(request))
    else:
        form = SearchObservationsForm()
    return render_to_response('search_observations_form.html', {'form': form}, context_instance = RequestContext(request))

def addObservation(request):
    scientific_names = []
    for org in TOrganismeTaxo.objects.raw('Select id_org_pk, nom_scientifique from t_organisme_taxo where referent_synonyme!=0 order by nom_scientifique limit 20'):
        scientific_names += (str(org.nom_scientifique)),
    
    if request.method == 'POST':
        form = AddObservationsForm(request.GET)
        return render_to_response('add_observation_form.html', {'form': form, 'names': scientific_names},  context_instance = RequestContext(request))
    else:
        form = AddObservationsForm()
        return render_to_response('add_observation_form.html', {'form': form, 'names': scientific_names},  context_instance = RequestContext(request))

###########################  VIEWS FOR TESTS   ########################################################################
def testAutocomplete(request):
    scientific_names = []
    for org in TOrganismeTaxo.objects.raw('Select id_org_pk, nom_scientifique from t_organisme_taxo where referent_synonyme!=0 order by nom_scientifique limit 20'):
        scientific_names += (str(org.nom_scientifique)),
        #scientific_names.append(str(org.nom_scientifique))
         
    return render_to_response('fruit.html',  {'names': scientific_names},)
            
def consultation(request):
    return HttpResponse('Consultation page')
    
def testTable(request):
    cursor= connection.cursor()
    cursor.execute('select * from "observation".display_info_bacteria() AS (observation int, host character varying(500),nom_scientifique character varying, commentaire_organisme character varying, date_observation date, nom_pays character varying(50), label_validation_state character varying(100))')
    #create a dictionary, so we can call label in the template
    desc = cursor.description
    data = [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]
    return render_to_response('test_table.html', {'data': data})
    
def testTable2(request):
    cursor= connection.cursor()
    cursor.execute('select * from "observation".display_info_bacteria() AS (observation int, host character varying(500),nom_scientifique character varying, commentaire_organisme character varying, date_observation date, nom_pays character varying(50), label_validation_state character varying(100))')
    
    #create a dictionary, so we can call label in the template
    desc = cursor.description #get column names & types
    data = [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]
    #create filter
    data_filter=[]
    for d in data:
        if d['nom_pays']=='Comoros':
            data_filter.append(d)
    
    table = ObservationsTable(data_filter, order_by=request.GET.get('sort'))
    table.paginate(page=request.GET.get('page', 1), per_page=25)
    return render_to_response('test_table2.html', {'table': table},
                              context_instance=RequestContext(request))


