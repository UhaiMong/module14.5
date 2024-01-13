from djangoForm.models import CollectionModel
from django import forms
from django.forms.widgets import NumberInput
import datetime


class practiceForms(forms.Form):
    name = forms.CharField(max_length=20)
    email = forms.EmailField(required=False)
    password = forms.PasswordInput()
    otp = forms.IntegerField(help_text="Enter 6 digit OTP number", label='OTP')
    dob = forms.DateField(widget=NumberInput(
        attrs={'type': 'date'}), label='DOB')
    BIRTH_YEAR_CHOICE = ['1999', '2000', '2001', '2002', '2003', '2004']
    birth_year = forms.DateField(
        widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICE), label='Birth Year')
    age = forms.DecimalField(label='Age')
    today = forms.DateField(
        initial=lambda: datetime.date.today(), label='Today', required=False)
    CHOICE_SIZE = [
        ('S', 'small'),
        ('M', 'medium'),
        ('L', 'large'),
        ('XL', 'Extra Large')
    ]
    tshirtSize = forms.ChoiceField(choices=CHOICE_SIZE, label='T-Shirt Size')
    t_shirt = forms.MultipleChoiceField(
        widget=forms.RadioSelect, choices=CHOICE_SIZE, required=False, label='Choice T-shirt in Radio select')
    FAVORITE_COLORS_CHOICES = [
        ('blue', 'Blue'),
        ('green', 'Green'),
        ('black', 'Black'),
        ('yellow', 'Yellow'),
        ('pink', 'Pink')
    ]
    favorite_colors = forms.MultipleChoiceField(
        choices=FAVORITE_COLORS_CHOICES)
    choice_color = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple, choices=FAVORITE_COLORS_CHOICES, label='Multiple Select in checkbox')
    file = forms.FileField()
    comment = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}))
    agree = forms.BooleanField(initial=True)


class CollectionForm(forms.ModelForm):
    class Meta:
        model = CollectionModel
        fields = '__all__'
        labels = {
            'name': 'username',
            'balance': 'Acount Balance'
        }
        error_messages = {
            'name': {'required': 'Name is required'}
        }
