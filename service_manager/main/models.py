from django.core.validators import EmailValidator
from django.db import models


class BaseAuditEntity(models.Model):
    created_on = models.DateTimeField(
        auto_now_add=True,
    )

    updated_on = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        abstract = True


class CustomerType(BaseAuditEntity):
    NAME_MAX_LENGTH = 50

    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'main_customer_type'


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
        )
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
        return self.name

    class Meta:
        db_table = 'main_customer_department'


class Brand(BaseAuditEntity):
    NAME_MAX_LENGTH = 100

    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
    )

    def __str__(self):
        return self.name


class AssetCategory(BaseAuditEntity):
    NAME_MAX_LENGTH = 100

    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'main_asset_category'


class Asset(BaseAuditEntity):
    MODEL_NUMBER_MAX_LENGTH = 20
    MODEL_NAME_MAX_LENGTH = 100

    model_number = models.CharField(
        max_length=MODEL_NUMBER_MAX_LENGTH,
    )

    model_name = models.CharField(
        max_length=MODEL_NAME_MAX_LENGTH,
    )

    brand = models.ForeignKey(
        Brand,
        on_delete=models.CASCADE,
    )

    category = models.ForeignKey(
        AssetCategory,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'{self.brand.name}---{self.model_number}---{self.model_name}'


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

    class Meta:
        db_table = 'main_customer_asset'


class Role(BaseAuditEntity):
    NAME_MAX_LENGTH = 20

    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
    )

    def __str__(self):
        return self.name


class Employee(BaseAuditEntity):
    FIRST_NAME_MAX_LENGTH = 20
    LAST_NAME_MAX_LENGTH = 20
    EMAIL_ADDRESS_MAX_LENGTH = 254

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
    )

    email_address = models.EmailField(
        max_length=EMAIL_ADDRESS_MAX_LENGTH,
        validators=(
            EmailValidator,
        )
    )

    role = models.ManyToManyField(
        Role,
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class MaterialCategory(BaseAuditEntity):
    NAME_MAX_LENGTH = 20

    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
    )

    def __str__(self):
        return self.name


class Material(BaseAuditEntity):
    NAME_MAX_LENGTH = 100

    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
    )

    price = models.FloatField()

    category = models.ForeignKey(
        MaterialCategory,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'{self.name} ({str(self.category)})'


class ServiceOrderHeader(BaseAuditEntity):
    is_completed = models.BooleanField(
        default=False,
    )

    serviced_on = models.DateTimeField(
        null=True,
        blank=True,
    )

    completed_on = models.DateTimeField(
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

    accepted_by = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        related_name='accepted_by',
    )

    serviced_by = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        related_name='serviced_by',
        null=True,
        blank=True
    )

    completed_by = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        related_name='completed_by',
        null=True,
        blank=True,
    )

    department = models.ForeignKey(
        CustomerDepartment,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    def __str__(self):
        return f'{str(self.customer)}--{str(self.asset)}'

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

    class Meta:
        db_table = 'main_service_order_detail'


class ServiceOrderNode(BaseAuditEntity):
    note = models.TextField()

    created_by = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
    )

    service_order = models.ForeignKey(
        ServiceOrderHeader,
        on_delete=models.CASCADE,
    )