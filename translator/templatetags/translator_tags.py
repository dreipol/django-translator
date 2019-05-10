# -*- coding: utf-8 -*-
from django import template
from django.template import Template
from translator.util import get_translation_for_key

register = template.Library()


class VariableRenderingNode(template.Node):

    def __init__(self, some_key):
        self.translation_key = template.Variable(some_key)

    def render(self, context):
        translation_for_key = get_translation_for_key(self.translation_key.resolve(context))
        return Template(translation_for_key).render(context)


def render_variable(parser, token):
    tag_name, variable_value = token.split_contents()

    # except ValueError:
    #     pass
    return VariableRenderingNode(variable_value)


register.tag('render_translation', render_variable)
