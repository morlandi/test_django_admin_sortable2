from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin
from adminsortable2.admin import SortableInlineAdminMixin
from .models import Button
from .models import Panel


class ButtonTabularInline(SortableInlineAdminMixin, admin.TabularInline):
    # We don't use the Button model but rather the juction model specified on Panel.
    model = Panel.buttons.through
    extra = 0
    autocomplete_fields = ['button', ]


class PanelTabularInline(admin.TabularInline):
    # We don't use the Button model but rather the juction model specified on Panel.
    model = Panel.buttons.through
    exclude = ['button_order', ]
    extra = 0
    autocomplete_fields = ['panel', ]


@admin.register(Panel)
class PanelAdmin(SortableAdminMixin, admin.ModelAdmin):
    inlines = (ButtonTabularInline,)
    search_fields = ['name', ]

    # make sure all panels are in one page, for easier sorting
    list_per_page = 1000


@admin.register(Button)
class ButtonAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'button_text', )
    inlines = (PanelTabularInline,)
    search_fields = ['name', 'button_text', ]
