from django.utils import timezone
from faker import Faker
from django.core.management import BaseCommand
import factory
from factory.django import DjangoModelFactory
from myfactoriesapp.models import Group, User, Employee, Order

fake = Faker()


class GroupFactory(DjangoModelFactory):
    class Meta:
        model = Group

    name = factory.Faker('word')


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    lang = factory.Iterator(['en', 'fr', 'es'])
    username = factory.Faker('user_name')
    nickname = factory.Sequence(lambda c: f'user{c:03}')
    group = factory.SubFactory(GroupFactory)
    birth_dt = factory.Faker('date_of_birth')
    birth_month = factory.SelfAttribute('birth_dt.month')


class EmployeeFactory(UserFactory):
    class Meta:
        model = Employee

    internal_id = factory.Sequence(int)
    internal_email = factory.LazyAttribute(
        lambda o: '{username}.{internal_id}@{domain}'.format(
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
                'date_time_between',
                start_date='-3m',
                end_date='-1m',
                tzinfo=timezone.utc,
            ),
            shipped_by=factory.SubFactory(EmployeeFactory),
        )
        delivered = factory.Trait(
            state=Order.DELIVERED,
            shipped_on=factory.Faker(
                'date_time_between',
                start_date='-3m',
                end_date='-1m',
                tzinfo=timezone.utc,
            ),
            shipped_by=factory.SubFactory(EmployeeFactory),
            delivered_on=factory.Faker(
                'date_time_between',
                start_date='-20d',
                tzinfo=timezone.utc,
            ),
        )


def create_all():
    # group = GroupFactory()
    # print(group)

    # group = GroupFactory.build()
    # print(group)

    # groups = GroupFactory.build_batch(3)
    # print(groups)

    # groups = GroupFactory.create_batch(3)
    # print(groups)

    # group = GroupFactory(name='test')
    # print(group)

    user = UserFactory()
    print(user, user.group)

    groups = Group.objects.all()
    UserFactory.lang.reset()
    users = UserFactory.create_batch(
        4,
        username=factory.LazyFunction(fake.sentence),
        group=factory.Iterator(groups),
    )
    print(users)

    employee = EmployeeFactory()
    print(employee)

    groups = Group.objects.all()
    employees = EmployeeFactory.build_batch(3, group=factory.Iterator(groups))
    print(employees)

    order = OrderFactory()
    print(order)

    orders = OrderFactory.create_batch(3)
    print(orders)

    shipped_order = OrderFactory(shipped=True)
    print(shipped_order, 'by', shipped_order.shipped_by)

    delivered_order = OrderFactory(delivered=True)
    print(delivered_order, delivered_order.shipped_by)


class Command(BaseCommand):
    def handle(self, *args, **options):
        create_all()
        self.stdout.write(self.style.SUCCESS("Done"))
