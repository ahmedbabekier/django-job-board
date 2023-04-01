from django import forms
from .models import Apply


# class ApplyForm(forms.ModelForm):
#     class Mate:
#         model = Apply
#         fields = '__all__'

# fields = ['name', 'email', 'website', 'upload_cv', 'cover_letter']

class ApplyForm(forms.ModelForm):
    class Meta:
        model = Apply
        fields = "__all__"
