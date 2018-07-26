
Use case
========

    - Python 3.6
    - Django 2.0.7
    - django admin customized for Bootstrap3 (with django-bootstrap-admin)
    - django-admin-sortable2 applied to a M2M relation
    - test the new autocomplete_fields ModelAdmin option

Screenshots
-----------

Panel editing: buttons inlines are sortable

.. image:: etc/buttons_inline.png

Button editing: panels inlines are not

.. image:: etc/panels_inline.png



References
==========

    - `django-admin-sortable2 <https://django-admin-sortable2.readthedocs.io/en/latest/index.html>`_


**Excerpt from django-admin-sortable2 docs:**

Sortable Many to Many Relations with Sortable Tabular Inlines
=================================================================
Sortable many to many relations can be achieved by creating a model to act as a juction table and adding an ordering field. This model can be specified on the ``models.ManyToManyField`` ``through`` parameter that tells the Django ORM to use your juction table instead of creating a default one. Otherwise, the process is conceptually similar to the above examples.

For example if you wished to have buttons added to control panel able to be sorted into order via the Django Admin interface you could do the following. A key feature of this approach is the ability for the same button to be used on more than one panel.

Specify a junction model and assign it to the ManyToManyField
-------------------------------------------------------------

``models.py``

.. code:: python

    from django.db.import models

    class Button(models.Model):
        """A button"""
        name = models.CharField(max_length=64)
        button_text = models.CharField(max_length=64)

    class Panel(models.Model):
        """A Panel of Buttons - this represents a control panel."""
        name = models.CharField(max_length=64)
        buttons = models.ManyToManyField(Button, through='PanelButtons')

    class PanelButtons(models.Model):
        """This is a junction table model that also stores the button order for a panel."""
        panel = models.ForeignKey(Panel)
        button = models.ForeignKey(Button)
        button_order = models.PositiveIntegerField(default=0)

        class Meta:
            ordering = ('button_order',)

Setup the Tabular Inlines to enable Buttons to be sorted in Django Admin
------------------------------------------------------------------------

``admin.py``

.. code:: python

    from django.contrib import admin
    from adminsortable2.admin import SortableInlineAdminMixin
    from models import Panel

    class ButtonTabularInline(SortableInlineAdminMixin, admin.TabularInline):
        # We don't use the Button model but rather the juction model specified on Panel.
        model = Panel.buttons.through

    @admin.register(Panel)
    class PanelAdmin(admin.ModelAdmin)
        inlines = (ButtonTabularInline,)

