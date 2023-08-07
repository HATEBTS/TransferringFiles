from os import environ


BOOL_TRUE = True
BOOL_FALSE = False
DB_CONFIG = {
    'dbname': environ.get("DB_NAME"),
    'user': environ.get("DB_USER"),
    'password': environ.get("DB_PASS"),
    'host': environ.get("DB_HOST")
}

