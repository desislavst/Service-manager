from django.db import models

from service_manager.customers.managers import ActiveManager


class BaseAuditEntity(models.Model):
    created_on = models.DateTimeField(
        auto_now_add=True,
    )

    updated_on = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        abstract = True


class ActiveModel(models.Model):
    active = models.BooleanField(default=True, )
    objects = ActiveManager()

    class Meta:
        abstract = True

    def delete(self):
        self.active = False
        self.save()
