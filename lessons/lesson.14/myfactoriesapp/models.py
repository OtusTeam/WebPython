from django.db import models


class AbstractModel(models.Model):
    class Meta:
        abstract = True

    def __str__(self):
        data = [f'{k}={v!r}' for k, v in self.__dict__.items() if not k.startswith('_')]
        return f'{self.__class__.__name__}({", ".join(data)})'

    def __repr__(self):
        return str(self)


class Group(AbstractModel):
    name = models.CharField(max_length=50)


class User(AbstractModel):
    lang = models.CharField(max_length=2)
    username = models.CharField(max_length=40)
    nickname = models.CharField(max_length=40)
    group = models.ForeignKey(Group, on_delete=models.PROTECT)
    birth_dt = models.DateField()
    birth_month = models.IntegerField()


class Employee(User):
    internal_id = models.IntegerField()
    internal_email = models.EmailField()


class Order(AbstractModel):
    PENDING = 'pending'
    AWAITING_SHIPMENT = 'awaiting_shipment'
    SHIPPED = 'shipped'
    DELIVERED = 'delivered'

    STATES = (
        (PENDING, 'Pending'),
        (AWAITING_SHIPMENT, 'Awaiting Shipment'),
        (SHIPPED, 'Shipped'),
        (DELIVERED, 'Delivered'),
    )
    state = models.CharField(max_length=30, choices=STATES)
    shipped_on = models.DateTimeField(null=True)
    shipped_by = models.ForeignKey(Employee, on_delete=models.PROTECT, null=True)
    delivered_on = models.DateTimeField(null=True)
