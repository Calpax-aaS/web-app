import os

django_secret = os.getenv('DJANGO_SECRET_KEY', 'l0cAl-t3st*')
django_is_debug_activated = os.getenv('DJANGO_DEBUG', 'False').lower() == 'true'
django_relative_path_for_static_file = os.getenv('DJANGO_STATIC_PATH', './public/static')

# POSTGRESQL_ADDON -> env variables in CleverCloud
database = {
    'name': os.getenv('POSTGRESQL_ADDON_DB', os.getenv('PG_DB', '')),
    'user': os.getenv('POSTGRESQL_ADDON_USER', os.getenv('PG_USER', '')),
    'password': os.getenv('POSTGRESQL_ADDON_PASSWORD', os.getenv('PG_PWD', '')),
    'host': os.getenv('POSTGRESQL_ADDON_HOST', os.getenv('PG_HOST', '')),
    'port': os.getenv('POSTGRESQL_ADDON_PORT', os.getenv('PG_PORT', '')),
}