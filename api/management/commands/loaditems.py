from random import randrange

from django.core.management import BaseCommand
from django.db import IntegrityError

from api.models import Item


class Command(BaseCommand):
    help = "Команда для загрузки 'мусорных' данных в БД"

    def handle(self, *args, **options):
        count = options.get("count")
        items = []
        try:
            for i in range(count):
                item = Item(name=f"test_item {i}",
                            description=f"test_description {i}",
                            price=randrange(1000, 100000))
                items.append(item)
                Item.objects.bulk_create(items)
        except IntegrityError:
            print("В вашей базе данных уже есть записи")
        print("Записи загружены")

    def add_arguments(self, parser):
        parser.add_argument("count", nargs='?', default=20, type=int, help="Введите число записей")
