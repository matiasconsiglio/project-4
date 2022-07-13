from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    """
    Class used for allowing the user to comment in a post via form

    Parameters:
    Model form
    """
    class Meta:
        """
        Body of the form
        """
        model = Comment
        fields = ('body',)
