from django.core.management import BaseCommand, CommandError

from ...utils import CSVImporter


class Command(BaseCommand):
    help = 'Import Zillow Test CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str)

    def handle(self, *args, **options):
        importer = CSVImporter(options['csv_file'])
        try:
            created, updated = importer.perform_import()
        # TODO: some valid custom exceptions here rather than blank slate
        except Exception as e:
            raise CommandError(f"Import failed: {str(e)}")

        print(f"Zillow properties created: {created} / updated {updated}.")