from django.forms import ModelForm
from django import forms
from portal.models import Review, Comment, User
from pagedown.widgets import PagedownWidget

"""
This form is derived from 'Review', since that model has all the fields
this one really needs.
"""
class ReviewForm(ModelForm):
    #body = forms.CharField(label="")
    class Meta:
        model = Review
        #Title is a simple, small form, body is the whole md widget.
        fields = ['title', 'body']
        widgets = {'body': PagedownWidget()}
"""
A form derived from Comment. Will represent both a textbox for the user
to input data as well as the test from saved comments.
"""
class CommentForm(ModelForm):
    #This assignment is for specifying the dimensions of the input form.
    #It also clears the dumb default 'Body' label.
    body = forms.CharField(widget=forms.Textarea(attrs={'rows':2}), label='')
    class Meta:
        model = Comment
        fields = ['body']

"""
Derives from User. Utilized for changing 'about me' info.
"""
class AboutForm(ModelForm):
    #Label nullified to allow for customized labelling.
    about = forms.CharField(widget=forms.Textarea(attrs={'rows': 2}), label='')
    class Meta:
        model = User
        fields = ['about'] #TODO: Just specify single form elements with bootstrapform.
"""
Yet another modelform derived from User. This one handles images.
"""
class PhotoForm(ModelForm):
    class Meta:
        model = User
        fields = ['image']
