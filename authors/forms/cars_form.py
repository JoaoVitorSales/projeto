from collections import defaultdict
from django import forms
from cars.models import Cars
from utils.django_forms import add_attr
from django.forms import ValidationError
from utils.positive_value import is_positive_number


class AuthorCarsEdit(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._my_errors = defaultdict(list)
        add_attr(self.fields.get('description'), 'class', 'span-2')

    class Meta:
        model = Cars
        fields = 'title', 'details', 'value_unit', 'shop', \
                 'description', 'cover' 
        widgets = {
            'cover': forms.FileInput(
                attrs={
                    'class': 'span-2'
                }
            ),
        }

    def clean(self, *args, **kwargs):
        super_clean = super().clean(*args, **kwargs)
        cleanedData = self.cleaned_data

        title = cleanedData.get('title')
        details = cleanedData.get('details')

        if title == details:
            self._my_errors['title'].append('Title cannot be equal to details')
            self._my_errors['details'].append('Details cannot be equal to title')
        
        if self._my_errors:
            raise ValidationError(self._my_errors)
        
        return super_clean

    def clean_value_unit(self):
        field_name = 'value_unit'
        field_value = self.cleaned_data.get(field_name)

        if not is_positive_number(field_value):
            self._my_errors[field_name].append('The value not is positive')

        return field_value