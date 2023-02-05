from django import forms
from .models import Application


# Create your forms here.
class AppForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ('school', 'year', 'major', 'phone_number', 'birthday', 'q1', 'q2', 'first_hackathon',
                  'team_member_1', 'team_member_2', 'team_member_3', 'applicant', 'status')
