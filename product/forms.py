from django import forms
from django.forms import Form, ModelForm

from .models import Comment


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['subject', 'comment', 'rate']


class SearchForm(Form):
    query = forms.CharField(max_length=100)