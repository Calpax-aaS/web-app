import psycopg2
from django.core.management.base import BaseCommand
from django.db import IntegrityError

from customers.models import Client, Domain


class Command(BaseCommand):
    help = 'Test command to automatically generate Customers & Domains'

    def add_arguments(self, parser):
        # Named (optional) arguments
        parser.add_argument(
            '--domain-name',
            type=str,
            help='Define the domain name. Default: calpax.local',
        )

    def handle(self, *args, **options):
        # create your public tenant
        try:
            tenant = Client(schema_name='public',
                            name='DCU Inc.',
                            paid_until='2022-12-05',
                            on_trial=False)
            tenant.save()
        except IntegrityError:
            print('--> Public schema already exists')

        # create your public tenant
        try:
            tenant = Client(schema_name='sandbox_cameronballoons',
                            name='Sandbox Cameron Balloons France',
                            paid_until='2016-12-05',
                            on_trial=False)
            tenant.save()
        except IntegrityError:
            print('--> sandbox_cameronballoons schema already exists')

        # create your public tenant
        try:
            tenant1 = Client(schema_name='cameronballoons',
                             name='Cameron Balloons France',
                             paid_until='2016-12-05',
                             on_trial=False)
            tenant1.save()
        except IntegrityError:
            print('--> sandbox_cameronballoons schema already exists')

        domain_name = 'calpax.local'
        if options['domain_name']:
            domain_name = options['domain_name']

        # Add one or more domains for the tenant
        try:
            domain = Domain()
            domain.domain = 'sandbox-cameronballoons.' + domain_name  # don't add your port or www here! on a local server you'll want to use localhost here
            domain.tenant = Client.objects.get(schema_name='sandbox_cameronballoons')
            domain.is_primary = True
            domain.save()
        except IntegrityError:
            print('--> sandbox_cameronballoons domain already exists')

        # Add one or more domains for the tenant
        try:
            domain = Domain()
            domain.domain = 'cameronballoons.' + domain_name  # don't add your port or www here! on a local server you'll want to use localhost here
            domain.tenant = Client.objects.get(schema_name='cameronballoons')
            domain.is_primary = True
            domain.save()
        except IntegrityError:
            print('--> cameronballoons domain already exists')
