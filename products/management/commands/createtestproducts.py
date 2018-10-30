from django.core.management.base import BaseCommand, CommandError
from products.models import Product


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('--range', type=int, required=False, default=11)

    def handle(self, *arg, **option):

        try:
            for idx in range(1, option.get('range') + 1):
                product_name = '[test]-product-%s' % idx
                Product.objects.create(
                    title=product_name
                )
                self.stdout.write(
                    self.style.SUCCESS(product_name)
                )
        except Exception as err:
            raise CommandError(err)
