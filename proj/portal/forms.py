from django.forms import ModelForm
from django import forms
from portal.models import Review, Comment
from pagedown.widgets import PagedownWidget

"""
This form is derived from 'Review', since that model has all the fields
this one really needs.
"""
class ReviewForm(ModelForm):
    class Meta:
        model = Review
        #Title is a simple, small form, body is the whole md widget.
        fields = ['title', 'body']
        widgets = {'body': PagedownWidget()}
"""
A form derived from Comment. Will represent both a textbox for the user
to input data as well as the test from saved comments.
NOTE: Make "body" not display.
"""
class CommentForm(ModelForm):
    #This assignment is for specifying the dimensions of the input form.
    body = forms.CharField(widget=forms.Textarea(attrs={'cols': 400, 'rows': 2, 'title': "Post a comment"}))
    class Meta:
        model = Comment
        fields = ['body']
