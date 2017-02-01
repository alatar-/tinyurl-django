import string

# NOTE: changing SHORT_URL_LENGTH_BOUNDS may require executing
# database migration, see index/models.py -> Url:tiny_url
TINY_URL_LENGTH_BOUNDS = (3, 8)
TINY_URL_SYMBOLS = (string.ascii_uppercase + string.digits)
