from django import forms
from material import Layout, Row

from .models import Data, Locality


# class ScrapyardForm(forms.ModelForm):
#
#     class Meta:
#         model = Request
#         fields = ('phone', 'discount', 'locality', 'address', 'scrapyard', 'distantce', 'transport', 'cost', 'tonn',
#             'price', 'data', 'comment', 'loader', 'cutter', 'calculatedInPlace', 'createdDate')

class RequestForm(forms.Form):
    objects = Data.objects.all()
    context = objects.get(pk=1)

    phone = forms.CharField(max_length=17, label='Телефон')

    localitys = [(x, x) for x in Locality.objects.order_by('name')]
    locality = forms.ChoiceField(choices=localitys, label='Населенный пункт')

    address = forms.CharField(max_length=50, label='Точный адрес вывоза', required = False)

    transports = [(x, "{} (до {} тонн) - {} руб\км".format(x.name, x.tonn, x.price)) for x in context.transports.all()]
    transport = forms.ChoiceField(choices=transports, label='Вид траспорта')

    scrapyards = [(x, x) for x in context.scrapyards.all()]
    scrapyard = forms.ChoiceField(choices=scrapyards, label='Приёмный пункт')

    tonn = forms.CharField(max_length=17, label='Объем ломма (тонны)', required = False)

    data = forms.CharField(max_length=10, label='Желаемая дата вывоза', required = False)

    if (context.cutter):
        cutter = forms.BooleanField(label='Резщики', required = False)
    if (context.loader):
        loader = forms.BooleanField(label='Грезщики', required = False)
    if (context.calculatedInPlace):
        calculatedInPlace = forms.BooleanField(label='Рассщет на месте', required = False)

    comment = forms.CharField(widget=forms.Textarea, label='Комментарий к заказу', required = False)

    layout = Layout('phone', 'locality', 'address',
                    Row('transport', 'scrapyard'),
                    'tonn', 'data',
                    Row('cutter', 'loader', 'calculatedInPlace'),
                    'comment'
                    )


    # def clean_phone(self):
    #     message = self.cleaned_data['phone']
    #     num_words = len(message.split())
    #     if num_words < 4:
    #         raise forms.ValidationError("Not enough words!")
    #     return message
