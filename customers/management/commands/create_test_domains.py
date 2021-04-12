from django.core.management.base import BaseCommand

from customers.models import Client, Domain


class Command(BaseCommand):
    help = 'Test command to automatically generate Customers & Domains'

    def add_arguments(self, parser):
        # Named (optional) arguments
        parser.add_argument(
            '--domain-name',
            action='store_true',
            help='Define the domain name. Default: calpax.local',
        )

    def handle(self, *args, **options):
        # create your public tenant
        tenant = Client(schema_name='public',
                        name='DCU Inc.',
                        paid_until='2022-12-05',
                        on_trial=False)
        tenant.save()

        # create your public tenant
        tenant = Client(schema_name='sandbox_cameronballoons',
                        name='Sandbox Cameron Balloons France',
                        paid_until='2016-12-05',
                        on_trial=False)
        tenant.save()

        # create your public tenant
        tenant1 = Client(schema_name='cameronballoons',
                        name='Cameron Balloons France',
                        paid_until='2016-12-05',
                        on_trial=False)
        tenant1.save()

        domain_name = 'calpax.local'
        if options['domain-name']:
            domain_name = options['domain-name']

        # Add one or more domains for the tenant
        domain = Domain()
        domain.domain = 'sandbox-cameronballoons.' + domain_name  # don't add your port or www here! on a local server you'll want to use localhost here
        domain.tenant = tenant
        domain.is_primary = True
        domain.save()

        # Add one or more domains for the tenant
        domain = Domain()
        domain.domain = 'cameronballoons.' + domain_name  # don't add your port or www here! on a local server you'll want to use localhost here
        domain.tenant = tenant1
        domain.is_primary = True
        domain.save()
