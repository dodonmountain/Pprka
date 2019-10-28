from django import forms
from .models import Product, Comment
from products.choices import *
from likert_field.forms import LikertFormField

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'image', 'package', 'width', 'height', 'length', 'diameter', 'weight', 'feature', 'construction', 'safty', 'care', 'designer', 'material', 'environment', 'document', )

class CommentForm(forms.ModelForm):
    # score = LikertFormField(
    #     # type='text',
    #     # class=likert-field
    # )
    score = forms.ChoiceField(
        choices=STATUS_CHOICES,
        widget=forms.Select(),
        required=True
    )
    recommend = forms.ChoiceField(
        choices=RELEVANCE_CHOICES,
    )
    class Meta:
        model = Comment
        fields = ('score', 'title', 'content', 'recommend', 'value_for_money', 'quality', 'design', 'furnish', 'function', )
