from django import forms
from .models import Account, Student, Owner, Car, Book, Borrow, Author

# from betterforms.multiform import MultiModelForm
# class MyMultiForm(MultiModelForm):
#     form_classes = {"client": ClientForm, "client_custom": ClientCustomFieldsForm}

class AccountForm(forms.ModelForm):
    class Meta:
        model=Account
        fields=['id', 'password', 'email']
        exclude=['student']

class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'
        exclude=['idStudent']

class OwnerForm(forms.ModelForm):
    class Meta:
        model=Owner
        fields='__all__'

class CarForm(forms.ModelForm):
    class Meta:
        model=Car
        fields='__all__'
        exclude=['owner']

class BookForm(forms.ModelForm):
    class Meta:
        model=Book
        fields='__all__'
        exclude=['author']

class AuthorForm(forms.ModelForm):
    class Meta:
        model=Author
        fields='__all__'

class BorrowForm(forms.ModelForm):
    class Meta:
        model=Borrow
        fields='__all__'
        exclude=['author','book']