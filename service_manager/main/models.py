from django.contrib.auth.models import User
from django.core.validators import EmailValidator
from django.db import models

from service_manager.accounts.models import Profile
from service_manager.core.models import BaseAuditEntity
from service_manager.master_data.models import CustomerType, Asset, Material


class Customer(BaseAuditEntity):
    NAME_MAX_LENGTH = 100
    VAT_MAX_LENGTH = 20
    EMAIL_MAX_LENGTH = 254
    PHONE_NUMBER_MAX_LENGTH = 20

    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
    )

    vat = models.CharField(
        max_length=VAT_MAX_LENGTH,
        null=True,
        blank=True,
    )

    email_address = models.EmailField(
        max_length=EMAIL_MAX_LENGTH,
        validators=(
            EmailValidator,
        )
    )

    phone_number = models.CharField(
        max_length=PHONE_NUMBER_MAX_LENGTH,
    )

    type = models.ForeignKey(
        CustomerType,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name


class CustomerRepresentative(BaseAuditEntity):
    FIRST_NAME_MAX_LENGTH = 20
    LAST_NAME_MAX_LENGTH = 20
    EMAIL_ADDRESS_MAX_LENGTH = 254
    PHONE_NUMBER_MAX_LENGTH = 20

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
    )

    email_address = models.CharField(
        max_length=EMAIL_ADDRESS_MAX_LENGTH,
        validators=(
            EmailValidator,
        ),
        null=True,
        blank=True,
    )

    phone_number = models.CharField(
        max_length=PHONE_NUMBER_MAX_LENGTH,
    )

    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        db_table = 'main_customer_representative'
        ordering = ('first_name', 'last_name',)


class CustomerDepartment(BaseAuditEntity):
    NAME_MAX_LENGTH = 100

    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
    )

    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'{str(self.customer)} {self.name}'

    class Meta:
        db_table = 'main_customer_department'
        ordering = ('name',)


class CustomerAsset(BaseAuditEntity):
    SERIAL_NUMBER_MAX_LENGTH = 20
    PRODUCT_NUMBER_MAX_LENGTH = 20

    serial_number = models.CharField(
        max_length=SERIAL_NUMBER_MAX_LENGTH,
        null=True,
        blank=True,
    )

    product_number = models.CharField(
        max_length=PRODUCT_NUMBER_MAX_LENGTH,
        null=True,
        blank=True,
    )

    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
    )

    asset = models.ForeignKey(
        Asset,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'{str(self.customer)}---{str(self.asset)}--{self.serial_number}---{self.product_number}'

    class Meta:
        db_table = 'main_customer_asset'
        ordering = ('asset__category__name', 'asset__brand__name', 'asset__model_name', 'serial_number',)


class ServiceOrderHeader(BaseAuditEntity):
    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
    )

    customer_asset = models.ForeignKey(
        CustomerAsset,
        on_delete=models.CASCADE,
    )

    handed_over_by = models.ForeignKey(
        CustomerRepresentative,
        on_delete=models.CASCADE,
        related_name='handed_by_customer_representative',
    )

    department = models.ForeignKey(
        CustomerDepartment,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    is_serviced = models.BooleanField(
        default=False,
    )

    is_completed = models.BooleanField(
        default=False,
    )

    serviced_by = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='serviced_by',
        null=True,
        blank=True
    )

    serviced_on = models.DateTimeField(
        null=True,
        blank=True,
    )

    completed_on = models.DateTimeField(
        null=True,
        blank=True,
    )

    completed_by = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='completed_by',
        null=True,
        blank=True,
    )

    handed_over_to = models.ForeignKey(
        CustomerRepresentative,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='handed_to_customer_representative',
    )

    @property
    def total_amount_due(self):
        return f'{sum([x.total_amount for x in self.serviceorderdetail_set.all()]):.2f}'

    def __str__(self):
        return f'{str(self.customer)}--{str(self.customer_asset)}'

    class Meta:
        db_table = 'main_service_order_header'


class ServiceOrderDetail(BaseAuditEntity):
    quantity = models.FloatField()
    discount = models.FloatField()

    service_order = models.ForeignKey(
        ServiceOrderHeader,
        on_delete=models.CASCADE,
    )

    material = models.ForeignKey(
        Material,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'{str(self.service_order)}---{str(self.material)}'

    @property
    def discount_percentage(self):
        pct = 0
        if self.discount > 0:
            pct = self.discount / 100
        return pct

    @property
    def discounted_price(self):
        price = self.material.price
        if self.discount_percentage > 0:
            price = price * (1 - self.discount_percentage)
        return price

    @property
    def total_amount(self):
        return self.discounted_price * self.quantity

    class Meta:
        db_table = 'main_service_order_detail'


class ServiceOrderNote(BaseAuditEntity):
    note = models.TextField()

    created_by = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
    )

    service_order = models.ForeignKey(
        ServiceOrderHeader,
        on_delete=models.CASCADE,
    )

    class Meta:
        ordering = ('-created_on',)
