from django import forms


class FormularioTeste(forms.Form):
    nome = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Nome', 'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'form-control'}))
    mensagem = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Mensagem', 'class': 'form-control'}))