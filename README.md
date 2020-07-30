### Zillow CSV Import & API

#### Setup and Running

It's a standard Django + DRF project; versions used:
- Python 3.8.2 (I use `pyenv` to manage local Python versions)
- Django 3.0.8
- see [requirements](./requirements) for more information

```
$ git clone https://github.com/jaddison/zillow-import-and-api.git
$ cd zillow-import-and-api
$ pyenv local 3.8.2
$ python -m venv .venv
$ source .venv/bin/activate
(.venv) $ pip install -r requirements/dev.txt 
(.venv) $ export DJANGO_SETTINGS_MODULE=bungalow.settings.dev 
(.venv) $ ./manage.py migrate 
(.venv) $ ./manage.py runserver 0.0.0.0:8500
```

To import the Zillow data file:
```
$ source .venv/bin/activate
(.venv) $ export DJANGO_SETTINGS_MODULE=bungalow.settings.dev
(.venv) $ ./manage.py import_zillow_csv <path to file>
```


#### API Documentation

Auto-generated documentation lives at [http://localhost:8500/docs](http://localhost:8500/docs), assuming you've 
switched the Django binding port to 8500.

Note that some basic property filtering is available with the `price_max` and `price_min` query parameters for 
the property listing endpoint.

#### Live API Testing

I've included an export of my [Insomnia](https://insomnia.rest/) workspace - you can 
[find it in the `extra` directory](./extra/Insomnia-endpoint-testing.json). It assumes port `8500`; it can be 
changed in the workspace environment (see `base_url`).

#### Assumptions

I inspected the data in the CSV file; where there were blanks in columns, I chose to convert blank strings to 
`None`, and used `null=True` on _those specific model fields_, not any others that had consistent data.