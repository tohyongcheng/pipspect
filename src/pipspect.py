#!/usr/bin/env python

from __future__ import print_function
import inspect
import os
import sys
import pkgutil

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
        print("\t" * INDENT_LEVEL, end='')
    for arg in args:
        print(arg, end='')
    print()


def print_docstr(obj):
    if hasattr(obj, '__doc__') and obj.__doc__:
        docstr = obj.__doc__
        for line in docstr.split('\n'):
            print_with_indent(line)


def inspect_class(obj):
    """Inspects a class object"""

    print_with_indent("+Class: %s" % obj.__name__)
    indent()

    for name in obj.__dict__:
        node = getattr(obj, name, None)
        if node is not None and inspect.ismethod(node):
            inspect_method(node)

    dedent()


def inspect_builtin(obj):
    """Inspects a builtin function"""

    print_with_indent("+Builtin Function: %s" % obj.__name__)
    indent()
    print_docstr(obj)
    dedent()
    print()


def get_arguments(func):
    try:
        parameters = inspect.signature(func).parameters.values()
        args = []
        varargs = []
        kwargs = []
        defaults = []
        for param in parameters:
            if param.kind == param.POSITIONAL_OR_KEYWORD:
                args.append(param.name)
                if param.default:
                    defaults.append(param.default)
            elif param.kind == param.VAR_POSITIONAL:
                varargs.append(param.name)
            elif param.kind == param.VAR_KEYWORD:
                kwargs.append(param.name)
        return args, varargs, kwargs, defaults
    except AttributeError:
        return inspect.getargspec(func)


def inspect_function(obj):
    """Inspects the function and displays arguments"""

    print_with_indent("+Function %s" % obj.__name__)
    print_docstr(obj)
    try:
        args, varargs, kwargs, defaults = get_arguments(obj)
    except TypeError:
        print()
        return

    if args:
        if args[0] == 'self':
            print_with_indent('\t%s is an instance method' % obj.__name__)
            args.pop()

        print_with_indent('\t-Function Arguments: ', args)

        if defaults:
            default_args = args[len(args) - len(defaults)]
            print_with_indent('\t-Default Values:',
                              zip(default_args, defaults))

    if varargs:
        print_with_indent('\t-Positional Arguments:', varargs)
    if kwargs:
        print_with_indent('\t-Keyword Arguments:', kwargs)

    print()


def inspect_method(obj):
    """Inspects the function and displays arguments"""

    print_with_indent("+Method %s" % obj.__name__)
    print_docstr(obj)
    try:
        args, varargs, kwargs, defaults = get_arguments(obj)
    except TypeError:
        print()
        return

    if args:
        if args[0] == 'self':
            print_with_indent('\t%s is an instance method' % obj.__name__)
            args.pop()

        print_with_indent('\t-Method Arguments: ', args)

        if defaults:
            default_args = args[len(args) - len(defaults)]
            print_with_indent('\t-Default Values:',
                              zip(default_args, defaults))

    if varargs:
        print_with_indent('\t-Positional Arguments:', varargs)
    if kwargs:
        print_with_indent('\t-Keyword Arguments:', kwargs)

    print()


def inspect_module(module, depth=2):
    """Inspects the module object including its classes and functions"""
    if depth < 1: return
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
        elif inspect.ismodule(obj):
            count += 1
            inspect_module(obj, depth - 1)

    if '__path__' in dir(module):
        for importer, modname, ispkg in pkgutil.iter_modules(module.__path__):
            try:
                m = importer.find_module(modname).load_module(modname)
                if modname != '__main__':
                    inspect_module(m, depth - 1)
                count += 1
            except ImportError:
                continue

    if count == 0:
        print_with_indent('No members.')
        print()
    dedent()

    return True


def main():
    if len(sys.argv) < 2:
        sys.exit('Usage: %s <module> <max_depth>' % sys.argv[0])

    module = sys.argv[1].replace('.py', '')
    mod = __import__(module)

    if len(sys.argv) > 2:
        try:
            depth = int(sys.argv[2])
        except:
            sys.exit('<max_depth> must be an integer')
        inspect_module(mod, depth)
    else:
        inspect_module(mod)


if __name__ == "__main__":
    main()
