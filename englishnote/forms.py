from django import forms
from .models import Note, Review

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['sentence','translation']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['comment', 'photo']