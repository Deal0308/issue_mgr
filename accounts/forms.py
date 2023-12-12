from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django import forms
from .models import Issue

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields =UserCreationForm.Meta.fields + ('email','role', 'team',)

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = CustomUser
        fields =UserChangeForm.Meta.fields

# class IssueForm(forms.ModelForm):
#     class Meta:
#         model = Issue
#         fields = ('summary', 'description', 'status', 'assignee',)

# class IssueFormAssign(forms.ModelForm):
#     class Meta:
#         model = Issue
#         fields = ('assignee',)

# class IssueFormStatus(forms.ModelForm):
#     class Meta:
#         model = Issue
#         fields = ('status',)

# class IssueFormArchive(forms.ModelForm):
#     class Meta:
#         model = Issue
#         fields = ('is_archived',)

# class IssueFormUnArchive(forms.ModelForm):
#     class Meta:
#         model = Issue
#         fields = ('is_archived',)

# class IssueFormDelete(forms.ModelForm):
#     class Meta:
#         model = Issue
#         fields = ('is_archived',)

# class IssueFormUnDelete(forms.ModelForm):
#     class Meta:
#         model = Issue
#         fields = ('is_archived',)

# class IssueFormUnAssign(forms.ModelForm):
#     class Meta:
#         model = Issue
#         fields = ('assignee',)

# class IssueFormUnStatus(forms.ModelForm):
#     class Meta:
#         model = Issue
#         fields = ('status',)

# class IssueFormUnArchive(forms.ModelForm):

#     class Meta:
#         model = Issue
#         fields = ('is_archived',)

