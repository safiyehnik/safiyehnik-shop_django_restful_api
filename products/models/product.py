from django.db import models
from django.utils.translation import ugettext_lazy as _


class Product(models.Model):
    category = models.ForeignKey(to='products.category', on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    off = models.PositiveIntegerField()
    stock = models.PositiveIntegerField()
    description = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name=_('Created at'))
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name=_('Updated at'))

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')

    def __str__(self):
        return self.name
