import os
from pynamodb.models import Model
from pynamodb.attributes import ListAttribute, UnicodeAttribute

DYNAMO_PREFIX = os.environ.get('DYNAMO_PREFIX', 'routines_')
DYNAMO_REGION = os.environ.get('DYANMO_REGION', 'us-east-1')


class Routine(Model):
    class Meta:
        table_name = DYNAMO_PREFIX + 'routines'
        region = DYNAMO_REGION

    user = UnicodeAttribute(hash_key=True)
    name = UnicodeAttribute(range_key=True)
    description = UnicodeAttribute()
    items = ListAttribute()

    def __init__(self, *args, **kwargs):
        if kwargs.get('_user_instantiated', True):
            if 'description' not in kwargs:
                kwargs['description'] = ''
            if 'items' not in kwargs:
                kwargs['items'] = []
        super().__init__(*args, **kwargs)


tables = [
    Routine
]


def create_tables(read_capacity=4, write_capacity=2):
    for table_class in tables:
        if table_class.exists():
            print('table %s exists.' % table_class.Meta.table_name)
        else:
            print('Creating table "%s"...' % table_class.Meta.table_name)
            table_class.create_table(
                read_capacity_units=read_capacity,
                write_capacity_units=write_capacity,
                wait=True
            )
            print('Done.')


def delete_tables():
    for table_class in tables:
        if table_class.exists():
            print('Deleting table "%s"...' % table_class.Meta.table_name)
            table_class.delete_table()
            print('Done.')
