from django import forms
from .models import Comment, Contact


class CommentForm(forms.ModelForm):
    """
    Class used for allowing the user to comment in a post via form.
    """
    class Meta:
        """
        Body of the form
        """
        model = Comment
        fields = ('body',)


class ContactForm(forms.ModelForm):
    """
    Class form to contact the admin-
    """
    class Meta:
        """
        Body of the form
        """
        model = Contact
        fields = '__all__'
