from .models import ConversationMessage
from django import forms

class ConversationMessageForm(forms.ModelForm):
    class Meta:
        model = ConversationMessage
        fields = ('content',)
        widgets = {
            'content':forms.Textarea(attrs={
                'class':'w-full py-4 px-6 rounded-xl border'
            })
        }