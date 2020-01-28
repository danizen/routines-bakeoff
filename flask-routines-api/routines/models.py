import os
from pynamodb.models import Model
from pynamodb.attributes import ListAttribute, MapAttribute, UnicodeAttribute

DYNAMO_PREFIX = os.environ.get('DYNAMO_PREFIX', 'routines_')
DYNAMO_REGION = os.environ.get('DYANMO_REGION', 'us-east-1')


class Item(MapAttribute):
    name = UnicodeAttribute()
    description = UnicodeAttribute()


class Routine(Model):
    class Meta:
        table_name = DYNAMO_PREFIX + 'routines'
        region = DYNAMO_REGION

    user_id = UnicodeAttribute(hash_key=True)
    name = UnicodeAttribute(range_key=True)
    items = ListAttribute(null=True, of=Item)
