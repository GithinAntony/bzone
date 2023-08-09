from django.db import models
from django import forms
from .models import *
from django.core.validators import FileExtensionValidator


class CLoginForm(forms.Form):
    username = forms.RegexField(regex=r'^[a-zA-Z0-9]+$', max_length=100,
                                error_messages={'invalid': ("This value may contain only letters, numbers.")},
                                widget=forms.TextInput(
                                    attrs={'autocomplete': 'off', 'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(max_length=100, widget=forms.PasswordInput(
        attrs={'autocomplete': 'off', 'class': 'form-control', 'placeholder': 'Password'}))


class CRegisterForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'autocomplete': 'off', 'class': 'form-control', 'placeholder': 'Full Name'}))
    email = forms.EmailField(max_length=254, widget=forms.TextInput(
        attrs={'autocomplete': 'off', 'class': 'form-control', 'placeholder': 'Email'}))
    username = forms.RegexField(regex=r'^[a-zA-Z0-9]+$', max_length=100,
                                error_messages={'invalid': ("This value may contain only letters, numbers.")},
                                widget=forms.TextInput(
                                    attrs={'autocomplete': 'off', 'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(max_length=100, widget=forms.PasswordInput(
        attrs={'autocomplete': 'off', 'class': 'form-control', 'placeholder': 'Password'}))
    conpassword = forms.CharField(max_length=100, widget=forms.PasswordInput(
        attrs={'autocomplete': 'off', 'class': 'form-control', 'placeholder': 'Confirm Password'}))
    phone = forms.RegexField(regex=r'^[0-9]+$', max_length=10,
                             error_messages={'invalid': ("This value may contain only numbers.")},
                             widget=forms.TextInput(
                                 attrs={'autocomplete': 'off', 'class': 'form-control', 'placeholder': 'Phone number'}))
    institution_name = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'autocomplete': 'off', 'class': 'form-control', 'placeholder': 'Institution Name'}))
    address = forms.CharField(max_length=600, widget=forms.Textarea(
        attrs={'autocomplete': 'off', 'class': 'form-control', 'placeholder': 'Address', 'rows': '3'}))
    profile_image = forms.FileField(validators=[FileExtensionValidator(['jpg', 'png', 'jpeg'])])

    def clean_email(self):
        """
        Validate that the username is alphanumeric and is not already
        in use.
        """
        existing = Candidates.objects.filter(email=self.cleaned_data['email'])
        if existing.exists():
            raise forms.ValidationError(("An user with that email already exists."))
        else:
            return self.cleaned_data['email']

    def clean_username(self):
        """
        Validate that the username is alphanumeric and is not already
        in use.
        """
        existing = Candidates.objects.filter(username=self.cleaned_data['username'])
        if existing.exists():
            raise forms.ValidationError(("A user with that username already exists."))
        else:
            return self.cleaned_data['username']

    def clean(self):
        """
        Verifiy that the values entered into the two password fields
        match. Note that an error here will end up in
        ``non_field_errors()`` because it doesn't apply to a single
        field.

        """
        if 'password' in self.cleaned_data and 'conpassword' in self.cleaned_data:
            if self.cleaned_data['password'] != self.cleaned_data['conpassword']:
                raise forms.ValidationError(("The two password fields didn't match."))
        return self.cleaned_data

class CMLoginForm(forms.Form):
    username = forms.RegexField(regex=r'^[a-zA-Z0-9]+$', max_length=100,
                                error_messages={'invalid': ("This value may contain only letters, numbers.")},
                                widget=forms.TextInput(
                                    attrs={'autocomplete': 'off', 'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(max_length=100, widget=forms.PasswordInput(
        attrs={'autocomplete': 'off', 'class': 'form-control', 'placeholder': 'Password'}))


class CMRegisterForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'autocomplete': 'off', 'class': 'form-control', 'placeholder': 'Full Name'}))
    email = forms.EmailField(max_length=254, widget=forms.TextInput(
        attrs={'autocomplete': 'off', 'class': 'form-control', 'placeholder': 'Email'}))
    username = forms.RegexField(regex=r'^[a-zA-Z0-9]+$', max_length=100,
                                error_messages={'invalid': ("This value may contain only letters, numbers.")},
                                widget=forms.TextInput(
                                    attrs={'autocomplete': 'off', 'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(max_length=100, widget=forms.PasswordInput(
        attrs={'autocomplete': 'off', 'class': 'form-control', 'placeholder': 'Password'}))
    conpassword = forms.CharField(max_length=100, widget=forms.PasswordInput(
        attrs={'autocomplete': 'off', 'class': 'form-control', 'placeholder': 'Confirm Password'}))
    phone = forms.RegexField(regex=r'^[0-9]+$', max_length=10,
                             error_messages={'invalid': ("This value may contain only numbers.")},
                             widget=forms.TextInput(
                                 attrs={'autocomplete': 'off', 'class': 'form-control', 'placeholder': 'Phone number'}))
    address = forms.CharField(max_length=600, widget=forms.Textarea(
        attrs={'autocomplete': 'off', 'class': 'form-control', 'placeholder': 'Address', 'rows': '3'}))

    def clean_email(self):
        """
        Validate that the username is alphanumeric and is not already
        in use.
        """
        existing = CommitteeMembers.objects.filter(email=self.cleaned_data['email'])
        if existing.exists():
            raise forms.ValidationError(("An user with that email already exists."))
        else:
            return self.cleaned_data['email']

    def clean_username(self):
        """
        Validate that the username is alphanumeric and is not already
        in use.
        """
        existing = CommitteeMembers.objects.filter(username=self.cleaned_data['username'])
        if existing.exists():
            raise forms.ValidationError(("A user with that username already exists."))
        else:
            return self.cleaned_data['username']

    def clean(self):
        """
        Verifiy that the values entered into the two password fields
        match. Note that an error here will end up in
        ``non_field_errors()`` because it doesn't apply to a single
        field.

        """
        if 'password' in self.cleaned_data and 'conpassword' in self.cleaned_data:
            if self.cleaned_data['password'] != self.cleaned_data['conpassword']:
                raise forms.ValidationError(("The two password fields didn't match."))
        return self.cleaned_data

class JLoginForm(forms.Form):
    username = forms.RegexField(regex=r'^[a-zA-Z0-9]+$', max_length=100,
                                error_messages={'invalid': ("This value may contain only letters, numbers.")},
                                widget=forms.TextInput(
                                    attrs={'autocomplete': 'off', 'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(max_length=100, widget=forms.PasswordInput(
        attrs={'autocomplete': 'off', 'class': 'form-control', 'placeholder': 'Password'}))


class JRegisterForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'autocomplete': 'off', 'class': 'form-control', 'placeholder': 'Full Name'}))
    email = forms.EmailField(max_length=254, widget=forms.TextInput(
        attrs={'autocomplete': 'off', 'class': 'form-control', 'placeholder': 'Email'}))
    username = forms.RegexField(regex=r'^[a-zA-Z0-9]+$', max_length=100,
                                error_messages={'invalid': ("This value may contain only letters, numbers.")},
                                widget=forms.TextInput(
                                    attrs={'autocomplete': 'off', 'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(max_length=100, widget=forms.PasswordInput(
        attrs={'autocomplete': 'off', 'class': 'form-control', 'placeholder': 'Password'}))
    conpassword = forms.CharField(max_length=100, widget=forms.PasswordInput(
        attrs={'autocomplete': 'off', 'class': 'form-control', 'placeholder': 'Confirm Password'}))
    phone = forms.RegexField(regex=r'^[0-9]+$', max_length=10,
                             error_messages={'invalid': ("This value may contain only numbers.")},
                             widget=forms.TextInput(
                                 attrs={'autocomplete': 'off', 'class': 'form-control', 'placeholder': 'Phone number'}))
    address = forms.CharField(max_length=600, widget=forms.Textarea(
        attrs={'autocomplete': 'off', 'class': 'form-control', 'placeholder': 'Address', 'rows': '3'}))

    def clean_email(self):
        """
        Validate that the username is alphanumeric and is not already
        in use.
        """
        existing = Judges.objects.filter(email=self.cleaned_data['email'])
        if existing.exists():
            raise forms.ValidationError(("An user with that email already exists."))
        else:
            return self.cleaned_data['email']

    def clean_username(self):
        """
        Validate that the username is alphanumeric and is not already
        in use.
        """
        existing = Judges.objects.filter(username=self.cleaned_data['username'])
        if existing.exists():
            raise forms.ValidationError(("A user with that username already exists."))
        else:
            return self.cleaned_data['username']

    def clean(self):
        """
        Verifiy that the values entered into the two password fields
        match. Note that an error here will end up in
        ``non_field_errors()`` because it doesn't apply to a single
        field.

        """
        if 'password' in self.cleaned_data and 'conpassword' in self.cleaned_data:
            if self.cleaned_data['password'] != self.cleaned_data['conpassword']:
                raise forms.ValidationError(("The two password fields didn't match."))
        return self.cleaned_data

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'autocomplete': 'off', 'class': 'form-control mb-30', 'placeholder': 'Name'}))
    email = forms.EmailField(max_length=254, widget=forms.TextInput(
        attrs={'autocomplete': 'off', 'class': 'form-control mb-30', 'placeholder': 'Email'}))
    message = forms.CharField(max_length=500, widget=forms.Textarea(
        attrs={'autocomplete': 'off', 'class': 'form-control mb-30', 'placeholder': 'Message'}))

class CMAddProgram(forms.Form):
    program_name = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'autocomplete': 'off', 'class': 'form-control', 'placeholder': 'Program Name'}))
    details = forms.CharField(max_length=600, widget=forms.Textarea(
        attrs={'autocomplete': 'off', 'class': 'form-control', 'placeholder': 'Details', 'rows': '3'}))
    date = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'autocomplete': 'off', 'class': 'form-control', 'placeholder': 'Date'}))
    time = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'autocomplete': 'off', 'class': 'form-control', 'placeholder': 'Time'}))
    venue = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'autocomplete': 'off', 'class': 'form-control', 'placeholder': 'Venue'}))
    judges = forms.ModelChoiceField(queryset=Judges.objects.all(), initial=0)