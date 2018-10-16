import json
import jinja2
from jinja2.ext import Extension


@jinja2.evalcontextfilter
def from_json(eval_ctx, value):
    return json.loads(value)


class FromJsonExtension(Extension):

    def __init__(self, environment):
        super(FromJsonExtension, self).__init__(environment)
        environment.filters['from_json'] = from_json
