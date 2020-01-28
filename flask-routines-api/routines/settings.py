import os

SECRET_KEY = os.environ.setdefault('SECRET_KEY', b'd2c8\x92~8ak7A\xaek\xfa\t')
DYNAMO_PREFIX = os.environ.setdefault('DYNAMO_PREFIX', 'routines_')
