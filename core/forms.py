from django import forms
from django.utils import timezone

from .models import Stock, StockHistory, Cash, CashHistory


class StockCreateForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['category', 'item_name', 'item_description', 'quantity', 'unit_purchase_price',
                  'unit_sale_price', 'reorder_level']

    def clean_category(self):
        category = self.cleaned_data.get('category')
        if not category:
            raise forms.ValidationError('This field is required')
        # for instance in Stock.objects.all():
        #     if instance.category == category:
        #         raise forms.ValidationError(f'{category} is already created')
        return category

    def clean_item_name(self):
        item_name = self.cleaned_data.get('item_name')
        if not item_name:
            raise forms.ValidationError('This field is required')
        for instance in Stock.objects.all():
            if instance.item_name == item_name:
                raise forms.ValidationError(str(item_name) + ' is already created')
        return item_name


class StockSearchForm(forms.ModelForm):
    export_to_CSV = forms.BooleanField(required=False)

    class Meta:
        model = Stock
        fields = ['category', 'item_name', 'export_to_CSV']


class StockUpdateForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['category', 'item_name', 'unit_sale_price']


class IssueForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['receipt_no', 'sale_to', 'sale_quantity', 'unit_sale_price', 'payment_status',
                  'waybill_number', 'delivery_quantity', 'phone_number']


class ReceiveForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['purchased_quantity', 'purchased_from', 'unit_purchase_price', 'phone_number']


class StockHistorySearchForm(forms.ModelForm):
    export_to_CSV = forms.BooleanField(required=False)
    start_date = forms.DateTimeField(widget=forms.widgets.DateInput(attrs={'type': 'date'}),
                                     required=False, initial=timezone.now)
    end_date = forms.DateTimeField(widget=forms.widgets.DateInput(attrs={'type': 'date'}),
                                   required=False, initial=timezone.now)

    class Meta:
        model = StockHistory
        fields = ['category', 'item_name', 'export_to_CSV', 'start_date', 'end_date']


class IssueCashForm(forms.ModelForm):
    class Meta:
        model = Cash
        fields =["recipient", "detail", "amount_out"]


class ReceiveCashForm(forms.ModelForm):
    class Meta:
        model = Cash
        fields = ["issue_by", "detail", "amount_in"]


class CashSearchForm(forms.ModelForm):
    class Meta:
        model = Cash
        fields = ["detail"]


class ImpriestLevelForm(forms.ModelForm):
    class Meta:
        model = Cash
        fields = ['impriest_level']


class CashHistorySearchForm(forms.ModelForm):
    export_to_CSV = forms.BooleanField(required=False)
    start_date = forms.DateTimeField(widget=forms.widgets.DateInput(attrs={'type': 'date'}),
                                     required=False, initial=timezone.now)
    end_date = forms.DateTimeField(widget=forms.widgets.DateInput(attrs={'type': 'date'}),
                                   required=False, initial=timezone.now)

    class Meta:
        model = Cash
        fields = ['category', 'export_to_CSV', 'start_date', 'end_date']


class CashHistorySearchForm(forms.ModelForm):
    export_to_CSV = forms.BooleanField(required=False)
    start_date = forms.DateTimeField(widget=forms.widgets.DateInput(attrs={'type': 'date'}),
                                     required=False, initial=timezone.now)
    end_date = forms.DateTimeField(widget=forms.widgets.DateInput(attrs={'type': 'date'}),
                                   required=False, initial=timezone.now)

    class Meta:
        model = Cash
        fields = ['category', 'export_to_CSV', 'start_date', 'end_date']