""" Configuration of post forms """
from django import forms

from blog.models import Comment


class SearchForm(forms.Form):
    """ The form of the post's search """
    query = forms.CharField()


class EmailPostForm(forms.Form):
    """ The form of the post's email """
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comment = forms.CharField(required=False, widget=forms.Textarea)


class CommentForm(forms.ModelForm):
    """ The form of the post's comment """
    class Meta:
        """ Meta form of the post's comment """
        model = Comment
        fields = ('name', 'email', 'body')
