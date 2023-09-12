from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.db import connection

from catalog.models import Category, Product


class Command(BaseCommand):
    help = 'Populates the database with sample data'

    def _load_fixtures(self):
        call_command('loaddata', 'categories_fixture.json')
        call_command('loaddata', 'products_fixture.json')

    def _truncate_table_restart_id(self, tablename):
        with connection.cursor() as cursor:
            cursor.execute(f'TRUNCATE TABLE {tablename} RESTART IDENTITY CASCADE')

    def handle(self, *args, **options):
        self._truncate_table_restart_id(Category._meta.db_table)
        self._truncate_table_restart_id(Product._meta.db_table)
        self._load_fixtures()
        self.stdout.write(self.style.SUCCESS('Database populated with sample data'))
