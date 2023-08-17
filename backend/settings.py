from os import environ, path

BOOL_TRUE = True
BOOL_FALSE = False
DB_CONFIG = {
    'dbname': environ.get("DB_NAME"),
    'user': environ.get("DB_USER"),
    'password': environ.get("DB_PASS"),
    'host': environ.get("DB_HOST")
}
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
GOOGLE_TOKEN = path.join(path.dirname(__file__), "token.json")
GOOGLE_CREDENTIALS = path.join(path.dirname(__file__), "123.json")

