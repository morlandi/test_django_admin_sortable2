from django.db import models


class Button(models.Model):
    """A button"""
    name = models.CharField(max_length=64)
    button_text = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Panel(models.Model):
    """A Panel of Buttons - this represents a control panel."""
    name = models.CharField(max_length=64)
    buttons = models.ManyToManyField(Button, through='PanelButtons')
    position = models.PositiveIntegerField(null=False, blank=False, default=0)

    class Meta(object):
        ordering = ['position', ]

    def __str__(self):
        return self.name


class PanelButtons(models.Model):
    """This is a junction table model that also stores the button order for a panel."""
    panel = models.ForeignKey(Panel, on_delete=models.CASCADE)
    button = models.ForeignKey(Button, on_delete=models.CASCADE)
    button_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ('button_order',)

    def __str__(self):
        return ''
