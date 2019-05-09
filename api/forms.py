from django import forms
from material import Layout, Row, Column

from .models import Data, Locality, Region


# class ScrapyardForm(forms.ModelForm):
#
#     class Meta:
#         model = Request
#         fields = ('phone', 'discount', 'locality', 'address', 'scrapyard', 'distantce', 'transport', 'cost', 'tonn',
#             'price', 'data', 'comment', 'loader', 'cutter', 'calculatedInPlace', 'createdDate')

class RequestForm(forms.Form):
    objects = Data.objects.all()
    context = objects.get(pk=1)

    phone = forms.CharField(max_length=17, label='Телефон', error_messages={
        'required': 'Необходимо ввести номер телефона!'
    })

    regions = [(x, x) for x in Region.objects.order_by('uid')]
    region = forms.ChoiceField(choices=regions, label='Регион')

    localitys = Locality.objects

    localitys_amur = [(x, x) for x in localitys.filter(region=1).order_by('name')]
    locality_amur = forms.ChoiceField(choices=localitys_amur, label='Населенный пункт')

    localitys_kh = [(x, x) for x in localitys.filter(region=2).order_by('name')]
    locality_kh = forms.ChoiceField(choices=localitys_kh, label='Населенный пункт')

    localitys_ev = [(x, x) for x in localitys.filter(region=3).order_by('name')]
    locality_ev = forms.ChoiceField(choices=localitys_ev, label='Населенный пункт')

    localitys_pr = [(x, x) for x in localitys.filter(region=4).order_by('name')]
    locality_pr = forms.ChoiceField(choices=localitys_pr, label='Населенный пункт')

    address = forms.CharField(max_length=50, label='Точный адрес вывоза', required=False)

    scrapyards = context.scrapyards.all().order_by('uid')

    transports_bel = [(x, "{} (до {} тонн)".format(x.name, x.tonn, x.price)) for x in
                      scrapyards[0].transports.order_by('name')]
    transport_bel = forms.ChoiceField(choices=transports_bel, label='Вид траспорта')

    transports_tyg = [(x, "{} (до {} тонн)".format(x.name, x.tonn, x.price)) for x in
                      scrapyards[1].transports.order_by('name')]

    transport_tyg = forms.ChoiceField(choices=transports_tyg, label='Вид траспорта')

    transports_sk = [(x, "{} (до {} тонн)".format(x.name, x.tonn, x.price)) for x in
                     scrapyards[2].transports.order_by('name')]
    transport_sk = forms.ChoiceField(choices=transports_sk, label='Вид траспорта')

    transports_kh = [(x, "{} (до {} тонн)".format(x.name, x.tonn, x.price)) for x in
                     scrapyards[3].transports.order_by('name')]
    transport_kh = forms.ChoiceField(choices=transports_kh, label='Вид траспорта')

    transports_nah = [(x, "{} (до {} тонн)".format(x.name, x.tonn, x.price)) for x in
                      scrapyards[4].transports.order_by('name')]
    transport_nah = forms.ChoiceField(choices=transports_nah, label='Вид траспорта')

    scrapyards_label = [(x, x) for x in scrapyards]
    scrapyard = forms.ChoiceField(choices=scrapyards_label, label='Приёмный пункт')

    tonn = forms.CharField(max_length=17, label='Объем лома (тонны)', required=False)

    data = forms.CharField(max_length=10, label='Желаемая дата вывоза', required=False)

    # # if (context.cutter):
    # cutter = forms.BooleanField(label='Резчики', required=False)
    # # if (context.loader):
    # loader = forms.BooleanField(label='Грузчики', required=False)
    # # if (context.calculatedInPlace):
    # calculatedInPlace = forms.BooleanField(label='Рассчёт на месте', required=False)

    comment = forms.CharField(widget=forms.Textarea, label='Комментарий к заказу', required=False)

    layout = Layout('phone', 'region', 'locality_amur', 'locality_kh', 'locality_ev', 'locality_pr', 'address',
                    Row(Column('transport_bel', 'transport_tyg', 'transport_sk', 'transport_kh', 'transport_nah'), 'scrapyard'),
                    'tonn', 'data',
                    # Row('cutter', 'loader', 'calculatedInPlace'),
                    'comment'
                    )

# def clean_phone(self):
#     message = self.cleaned_data['phone']
#     num_words = len(message.split())
#     if num_words < 4:
#         raise forms.ValidationError("Not enough words!")
#     return message
