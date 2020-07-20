from faker import Faker
import factory
from factory import DjangoModelFactory
from django.utils import timezone
from django.core.management import BaseCommand

from factoriesapp.models import Group, User, Employee, Order

fake = Faker()


class GroupFactory(DjangoModelFactory):
    class Meta:
        model = Group

    # name = 'name'
    name = factory.Faker('word')


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    lang = factory.Iterator(['EN', 'FR', 'RU', 'ES'])
    username = factory.Faker('user_name')
    nickname = factory.Sequence(lambda c: f'user{c:03}')
    email = factory.Faker('email')
    birth_date = factory.Faker('date_of_birth')
    birth_month = factory.SelfAttribute('birth_date.month')
    group = factory.SubFactory(GroupFactory)


class EmployeeFactory(UserFactory):
    class Meta:
        model = Employee

    internal_id = factory.Sequence(int)


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
                start_date='-30d',
                end_date='-10d',
                tzinfo=timezone.utc,
            ),
            shipped_by=factory.SubFactory(EmployeeFactory),
        )
        delivered = factory.Trait(
            state=Order.DELIVERED,
            shipped_on=factory.Faker(
                'date_time_between',
                start_date='-30d',
                end_date='-10d',
                tzinfo=timezone.utc,
            ),
            shipped_by=factory.SubFactory(EmployeeFactory),
            delivered_on=factory.Faker(
                'date_time_between',
                start_date='-9d',
                end_date='-1d',
                tzinfo=timezone.utc,
            ),
        )

def create_all():
    group = GroupFactory(name='admin')
    print(group)

    group = GroupFactory.create(name=factory.LazyFunction(fake.word))
    print(group)

    group = GroupFactory.build()
    print(group)

    groups = GroupFactory.build_batch(3, name=fake.word())
    print(groups)

    groups = GroupFactory.create_batch(3, name=factory.LazyFunction(fake.word))
    print(groups)

    user = UserFactory()
    print(user, user.group)

    UserFactory.lang.reset()
    groups = Group.objects.all()
    # group = Group.objects.first()
    users = UserFactory.create_batch(
        5,
        username=factory.LazyFunction(fake.sentence),
        # group=factory.Iterator(groups),
        # group=group,
        group=factory.Faker('random_element', elements=groups),
    )
    print(users)

    employee = EmployeeFactory()
    print(employee)

    employees = EmployeeFactory.create_batch(4, group=factory.Iterator(groups))
    print(employees)

    order = OrderFactory()
    print(order)

    order_shipped = OrderFactory(shipped=True)
    print(order_shipped)

    order_delivered = OrderFactory(delivered=True)
    print(order_delivered)


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Starting with factory boy!")
        create_all()
