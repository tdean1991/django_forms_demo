from enum import Enum
from django.utils.translation import gettext_lazy as _
from django.db.models import TextChoices

class Size(TextChoices):
    #NONE = '', _('Please select a size')
    SMALL = 'S', _('Small'),
    MEDIUM = 'M',_('Medium')
    LARGE = 'L', _('Large')


class CoffeeType(TextChoices):
    #NONE = None, _('Please select a drink type')
    AMERICANO = 'A', _('Americano')
    CAPPUCCINO = 'C', _('Cappuccino')
    COLD = 'CB', _('Cold Brew Coffee')

class QuantityChoices(TextChoices):
    ONE = '1', '1'
    TWO = '2', '2'
    THREE = '3', '3'
