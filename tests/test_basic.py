import json
from jinja2 import Template, Environment


def test_no_extension():
    template = Template('foo {{ bar }}')
    result = template.render(bar="foo")
    assert result == "foo foo"


def test_extension1():
    env = Environment(extensions=["jinja2_from_json_extension."
                                  "FromJsonExtension"])
    x = ["foo", "bar"]
    template = \
        env.from_string("test {% set y = '" + json.dumps(x) + "'|from_json %} "
                        "{{'bar' in y}}")
    result = template.render()
    assert result == "test  True"
    x = ["foo", "foo2"]
    template = \
        env.from_string("test {% set y = '" + json.dumps(x) + "'|from_json %} "
                        "{{'bar' in y}}")
    result = template.render()
    assert result == "test  False"
