from django.forms import ModelForm
from portal.models import Review
from pagedown.widgets import PageDownWidget

"""
This form is derived from 'Review', since that model has all the fields
this one really needs.
"""
class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['title', 'body']
        widgets = {'body': PageDownWidget()}
