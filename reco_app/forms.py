from django import forms
from .models import User_input


## this is the code from the tutorial that does not seem to be working

"""
# Create your views here.
import rest_framework
from rest_framework import fields, serializers
from reco_app.models import location_choices, service_size_choices, organization_size_choices, role_choices

class userinput_form(serializers.HyperlinkedModelSerializer):
    # ...
    my_field = fields.MultipleChoiceField(choices=location_choices)
    my_field2 = fields.MultipleChoiceField(choices=service_size_choices)
    my_field3 = fields.MultipleChoiceField(choices=organization_size_choices)
    my_field4 = fields.MultipleChoiceField(choices=role_choices)
    # ...
"""

## this is another attempt at a model form --  this one works

from django import forms
from reco_app.models import location_choices, service_size_choices, organization_size_choices, role_choices

class userinput_form(forms.Form):
    locations = forms.CharField(label='Select a desired location', widget=forms.Select(choices=location_choices))
    services = forms.CharField(label='Select service choices', widget=forms.Select(choices=service_size_choices))
    organizations = forms.CharField(label='Select organization size choices', widget=forms.Select(choices=organization_size_choices))
    roles = forms.CharField(label='Select desired roles', widget=forms.Select(choices=role_choices))

