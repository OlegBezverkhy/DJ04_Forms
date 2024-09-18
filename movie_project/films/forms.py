from .models import Movie
from django.forms import ModelForm, TextInput, Textarea


class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = ['name', 'describe', 'comment']
        widgets={
            'name': TextInput(attrs={'class': 'form-control',
                                     'id' :'movieTitle',
                                     'placeholder': 'Введите название фильма',
                                     'required':'required'}),
            'describe': Textarea(attrs={'class':'form-control',
                                        'id':'movieDescription',
                                        'name':'movieDescription',
                                        'rows':'5',
                                        'placeholder':'Введите краткое описание фильма'}),
            'comment': Textarea(attrs={'class': 'form-control',
                                       'id': 'movieReview',
                                       'name': 'movieReview',
                                       'rows':'5',
                                       'placeholder': 'Введите Ваш отзыв',
                                       'required':'required'})
        }
