from datetime import datetime
from json import JSONEncoder


class PynamoEncoder(JSONEncoder):
    def default(self, obj):
        if hasattr(obj, 'attribute_values'):
            return obj.attribute_values
        elif isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%dT%H:%M:%SZ')
        return JSONEncoder.default(self, obj)
