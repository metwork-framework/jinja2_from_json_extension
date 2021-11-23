import json
import jinja2
from jinja2.ext import Extension


try:
    from jinja2 import pass_eval_context as eval_context
except ImportError:
    from jinja2 import evalcontextfilter as eval_context

@eval_context
def from_json(eval_ctx, value):
    return json.loads(value)


class FromJsonExtension(Extension):

    def __init__(self, environment):
        super(FromJsonExtension, self).__init__(environment)
        environment.filters['from_json'] = from_json
