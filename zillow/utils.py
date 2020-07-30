import csv
import re
from datetime import datetime
from decimal import Decimal

from .models import Property


class CSVImporter:
    magnitude_mapping = {
        'K': 3,
        'M': 6,
        'B': 9
    }
    re_price = re.compile(r'[^\d]*([\d.]+)({})'.format("|".join(magnitude_mapping.keys())), re.I)

    def __init__(self, filename):
        self.filename = filename

    def str_price_to_decimal(self, value):
        matches = self.re_price.match(value)
        if matches:
            # pull out the price and K,M,etc values
            price, magnitude = matches.groups()
            magnitude = self.magnitude_mapping.get(magnitude.upper(), 1)
            # convert to a proper number
            return Decimal(price) * 10 ** magnitude

    def perform_import(self):
        count_updated = count_created = 0
        with open(self.filename, 'r', encoding='utf8', newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # ensure we have None for any blank strings (for null=True fields)
                row = {k: (v if v else None) for k, v in row.items()}

                # convert the price string to an actual number
                row['price'] = self.str_price_to_decimal(row['price'])

                # parse the date strings to actual dates
                for field in ('last_sold_date', 'rentzestimate_last_updated', 'zestimate_last_updated'):
                    try:
                        row[field] = datetime.strptime(row[field], '%m/%d/%Y')
                    except TypeError:
                        row[field] = None

                # simplistic idempotency.
                _, created = Property.objects.update_or_create(
                    zillow_id=row['zillow_id'],
                    defaults=row
                )
                if created:
                    count_created += 1
                else:
                    count_updated += 1

        return count_created, count_updated
