import os
import random

from django import template

"""
" This was downloaded from django snippets.
"""

#Register the template library.
register = template.Library()

#Register the tag name into the templates.
@register.tag(name="randomgen")
#This is a random number/hash generator.
def randomgen(parser, token):
    items = []
    bits =  token.split_contents()
    for item in bits:
        items.append(item)

    return RandomgenNode(items[1:])

class RandomgenNode(template.Node):
    def __init__(self, items):
        self.items = []
        for item in items:
            self.items.append(item)
    
    def render(self, context):
        if len(self.items) == 2:
            arg1 = self.items[0]
            arg2 = self.items[1]

        if "hash" in self.items:
            result = os.urandom(16).encode('hex')
        elif "float" in self.items:
            result = random.uniform(int(arg1), int(arg2))
        elif not self.items:
            result = random.randrange(1,300000000)
        else:
            result = random.randint(int(arg1), int(arg2))
        return result