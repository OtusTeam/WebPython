import factory
from faker import Faker
from django.core.management import BaseCommand
from factoriesapp.models import Group, User, Employee, Order

fake = Faker()


class GroupFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Group

    name = factory.Faker('word')


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    lang = factory.Iterator(['en', 'fr', 'es', 'it', 'de'])
    username = factory.Sequence(lambda c: f'user{c:03}')
    nickname = factory.Faker('user_name')
    group = factory.SubFactory(GroupFactory)
    birth_dt = factory.Faker('date_of_birth')
    birth_month = factory.SelfAttribute('birth_dt.month')


class EmployeeFactory(UserFactory):
    class Meta:
        model = Employee

    internal_id = factory.Sequence(int)
    internal_email = factory.LazyAttribute(
        lambda o: '%s.%s@%s' % (o.username, o.internal_id, fake.domain_name())
    )


class OrderFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Order

    state = factory.Iterator(Order.STATES[:2], getter=lambda s: s[0])
    shipped_on = None
    shipped_by = None
    delivered_on = None

    class Params:
        shipped = factory.Trait(
            state='shipped',
            shipped_on=factory.Faker(
                'date_between',
                start_date='-3m',
                end_date='today',
            ),
            shipped_by=factory.SubFactory(EmployeeFactory),
        )
        delivered = factory.Trait(
            state='delivered',
            shipped_on=factory.Faker(
                'date_between',
                start_date='-5m',
                end_date='-1m',
            ),
            delivered_on=factory.Faker(
                'date_between',
                start_date='-20d',
                end_date='today',
            ),
            shipped_by=factory.SubFactory(EmployeeFactory),
        )

def create_all():
    group = GroupFactory()
    print(group)

    user = UserFactory()
    print(user)

    user = UserFactory()
    print(user, user.group)

    UserFactory.lang.reset()

    users = UserFactory.create_batch(4)
    print(users)

    employee = EmployeeFactory()
    print(employee)

    order = OrderFactory()
    print(order)

    orders = OrderFactory.create_batch(5)
    print(orders)

    order = OrderFactory(shipped=True)
    print(order)

    order = OrderFactory(delivered=True)
    print(order)


class Command(BaseCommand):

    def handle(self, *args, **options):
        create_all()
