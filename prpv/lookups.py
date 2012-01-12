from selectable.base import ModelLookup
from selectable.registry import registry

from demo.prpv.models import TOrganismeTaxo, Fruit

class ScientificNameLookup(ModelLookup):
    model = TOrganismeTaxo
    search_field = 'nom_scientifique__icontains'

class FruitLookup(ModelLookup):
    model = Fruit
    search_field = 'name__icontains'

registry.register(FruitLookup)

#registry.register(ScientificNameLookup)

