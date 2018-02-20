from django import forms
from django.conf import settings
from django.forms import inlineformset_factory
from django.utils.translation import ugettext_lazy as _

from adhocracy4.categories import models as category_models
from adhocracy4.dashboard.components.forms import ModuleDashboardFormSet
from adhocracy4.modules import models as module_models


class CategorizableFieldMixin:
    category_field_name = 'category'

    def __init__(self, *args, **kwargs):
        module = kwargs.pop('module')
        super().__init__(*args, **kwargs)

        field = self.fields[self.category_field_name]
        field.queryset = category_models.Category.objects.filter(module=module)

        required = field.queryset.exists()
        field.empty_label = None
        field.required = required
        field.widget.is_required = required

    def show_categories(self):
        field = self.fields[self.category_field_name]
        module_has_categories = field.queryset.exists()
        return module_has_categories


class CategoryForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': _('Category')}
    ))

    if hasattr(settings, 'A4_CATEGORY_ICONS'):
        icon = forms.ChoiceField(choices=settings.A4_CATEGORY_ICONS)

    class Media:
        js = ('js/formset.js',)

    class Meta:
        model = category_models.Category
        if hasattr(settings, 'A4_CATEGORY_ICONS'):
            fields = ['name', 'icon']
        else:
            fields = ['name']


CategoryFormSet = inlineformset_factory(module_models.Module,
                                        category_models.Category,
                                        form=CategoryForm,
                                        formset=ModuleDashboardFormSet,
                                        extra=0,
                                        )
