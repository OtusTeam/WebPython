from datetime import timezone
from time import time
from django.core.management import BaseCommand
import factory
from factory.django import DjangoModelFactory
from faker import Faker

from myfactoriesapp.models import Group, User, Employee, Order

fake = Faker()


class GroupFactory(DjangoModelFactory):
    class Meta:
        model = Group

    name = factory.Faker("word")


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    lang = factory.Iterator(["en", "fr", "es", "ru"])
    username = factory.Faker("user_name")
    name = factory.Faker("name")
    group = factory.SubFactory(GroupFactory)
    birth_dt = factory.Faker("date_of_birth")
    birth_month = factory.SelfAttribute("birth_dt.month")


class EmployeeFactory(UserFactory):
    class Meta:
        model = Employee

    internal_id = factory.Sequence(int)
    # internal_email = factory.Faker('email')
    internal_email = factory.LazyAttribute(
        lambda o: '{username}.{internal_id:03d}@{domain}'.format(
            username=o.username,
            internal_id=o.internal_id,
            domain=fake.domain_name(),
        )
    )


class OrderFactory(DjangoModelFactory):
    class Meta:
        model = Order

    state = factory.Iterator(Order.STATES[:2], getter=lambda s: s[0])
    shipped_on = None
    shipped_by = None
    delivered_on = None

    class Params:
        shipped = factory.Trait(
            state=Order.SHIPPED,
            shipped_on=factory.Faker(
                "date_time_between",
                start_date="-3M",
                end_date="-1M",
                tzinfo=timezone.utc,
            ),
            shipped_by=factory.SubFactory(EmployeeFactory),
        )

        delivered = factory.Trait(
            state=Order.DELIVERED,
            shipped_on=factory.Faker(
                "date_time_between",
                start_date="-3M",
                end_date="-1M",
                tzinfo=timezone.utc,
            ),
            shipped_by=factory.SubFactory(EmployeeFactory),
            delivered_on=factory.Faker(
                "date_time_between",
                start_date="-25d",
                tzinfo=timezone.utc,
            ),
        )


def create_all():
    group = GroupFactory()
    print(group)

    group = GroupFactory.build()
    print(group)

    groups = GroupFactory.build_batch(3)
    print(groups)

    groups = GroupFactory.create_batch(3)
    print(groups)

    group = GroupFactory.build(name="username")
    print(group)

    group = GroupFactory.build(name=factory.Faker("user_name"))
    print(group)

    groups = GroupFactory.build_batch(3, name=factory.Faker("job"))
    print(groups)

    user = UserFactory()
    print(user, user.group)

    groups = Group.objects.all()
    UserFactory.lang.reset()
    users = UserFactory.create_batch(
        4,
        # just some function
        username=factory.LazyFunction(lambda: str(time()).split(".", 1)[1]),
        group=factory.Iterator(groups),
    )
    print(users)

    employee = EmployeeFactory()
    print(employee)

    employees = EmployeeFactory.build_batch(3)
    print(employees)

    new_order = OrderFactory()
    print(new_order)

    print("#" * 30)

    shipped_order = OrderFactory(shipped=True)
    # print(shipped_order, shipped_order.shipped_by)
    print(shipped_order)
    print(shipped_order.shipped_by)

    print("#" * 30)

    delivered_order = OrderFactory(delivered=True)
    print(delivered_order)
    print(delivered_order.shipped_by)


class Command(BaseCommand):
    help = "Create data using factory-boy"

    def handle(self, *args, **options):
        create_all()
