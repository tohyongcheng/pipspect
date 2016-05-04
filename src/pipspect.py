#!/usr/bin/env python

import inspect
import os
import sys

INDENT_LEVEL = 0


def indent():
    global INDENT_LEVEL
    INDENT_LEVEL += 1


def dedent():
    global INDENT_LEVEL
    INDENT_LEVEL -= 1


def print_with_indent(*args):
    """Prints lines with indents"""
    if INDENT_LEVEL:
        print "\t"*INDENT_LEVEL,
    for arg in args:
        print arg,


def inspect_class(obj):
    """Inspects a class object"""

    print_with_indent("+Class: %s" % obj.__name__)
    indent()

    for name in obj.__dict__:
        node = getattr(obj, name)
        if inspect.ismethod(node):
            inspect_function(node)

    dedent()
    print


def inspect_builtin(obj):
    """Inspects a builtin function"""

    print_with_indent("+Builtin Function: %s" % obj.__name__)
    print

    docstr = obj.__doc__.split('\n')
    indent()
    if docstr:
        for line in docstr:
            print_with_indent(line)
            print
    dedent()
    print


def inspect_function(obj):
    """Inspects the function and displays arguments"""

    print_with_indent("+Function %s" % obj.__name__)
    print_with_indent("'''%s'''" % obj.__doc__)
    try:
        arginfo = inspect.getargspec(obj)
    except TypeError:
        print
        return

    args, varargs, kwargs, defaults = arginfo[0]

    if args:
        if args[0] == 'self':
            print_with_indent('\t%s is an instance method' % obj.__name__)
            args.pop()

        print_with_indent('\t-Function Arguments: ', args)

        if defaults:
            default_args = args[len(args) - len(defaults)]
            print_with_indent('\t-Default Values:', zip(default_args, defaults))

    if varargs:
        print_with_indent('\t-Positional Arguments:', varargs)
    if kwargs:
        print_with_indent('\t-Keyword Arguments:', kwargs)

    print


def pipspect(module):
    """Inspects the module object including its classes and functions"""
    print_with_indent("Module: %s\n" % module.__name__)
    indent()

    count = 0
    for name in dir(module):
        obj = getattr(module, name)

        if inspect.isclass(obj):
            count += 1
            inspect_class(obj)
        elif inspect.isfunction(obj) or inspect.ismethod(obj):
            count += 1
            inspect_function(obj)
        elif inspect.isbuiltin(obj):
            count += 1
            inspect_builtin(obj)

    if count == 0:
        print_with_indent('No members.')


def main():
    if len(sys.argv) < 2:
        sys.exit('Usage: %s <module>' % sys.argv[0])

    module = sys.argv[1].replace('.py', '')
    mod = __import__(module)
    pipspect(mod)


if __name__ == "__main__":
    main()
    