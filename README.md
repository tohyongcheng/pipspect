# Pipspect

A simple command-line tool to find out what builtin functions, classes and methods are in your Python module.

## Install

Run

```
pip install pipspect
```

## Usage
Simply run

```
$ pipspect <module>

# For example:
$ pipspect module.py
$ pipspect sys
$ pipspect os

```

Output:

```
Module: sys
  +Builtin Function: displayhook
    displayhook(object) -> None

    Print an object to sys.stdout and also save it in __builtin__._


  +Builtin Function: excepthook
    excepthook(exctype, value, traceback) -> None

    Handle an exception by displaying it with a traceback on sys.stderr.


  +Builtin Function: _clear_type_cache
    _clear_type_cache() -> None
    Clear the internal type lookup cache.

  +Builtin Function: _current_frames
    _current_frames() -> dictionary

    Return a dictionary mapping each current thread T's thread id to T's
    current stack frame.

    This function should be used for specialized purposes only.

  +Builtin Function: _getframe
    _getframe([depth]) -> frameobject

    Return a frame object from the call stack.  If optional integer depth is
    given, return the frame object that many calls below the top of the stack.
    If that is deeper than the call stack, ValueError is raised.  The default
    for depth is zero, returning the frame at the top of the call stack.

    This function should be used for internal and specialized
    purposes only.

  +Builtin Function: call_tracing
    call_tracing(func, args) -> object

    Call func(*args), while tracing is enabled.  The tracing state is
    saved, and restored afterwards.  This is intended to be called from
    a debugger from a checkpoint, to recursively debug some other code.

  +Builtin Function: callstats
    callstats() -> tuple of integers

    Return a tuple of function call statistics, if CALL_PROFILE was defined
    when Python was built.  Otherwise, return None.

    When enabled, this function returns detailed, implementation-specific
    details about the number of function calls executed. The return value is
    a 11-tuple where the entries in the tuple are counts of:
    0. all function calls
    1. calls to PyFunction_Type objects
    2. PyFunction calls that do not create an argument tuple
    3. PyFunction calls that do not create an argument tuple
       and bypass PyEval_EvalCodeEx()
    4. PyMethod calls
    5. PyMethod calls on bound methods
    6. PyType calls
    7. PyCFunction calls
    8. generator calls
    9. All other calls
    10. Number of stack pops performed by call_function()

  +Builtin Function: displayhook
    displayhook(object) -> None

    Print an object to sys.stdout and also save it in __builtin__._


  +Builtin Function: exc_clear
    exc_clear() -> None

    Clear global information on the current exception.  Subsequent calls to
    exc_info() will return (None,None,None) until another exception is raised
    in the current thread or the execution stack returns to a frame where
    another exception is being handled.

  +Builtin Function: exc_info
    exc_info() -> (type, value, traceback)

    Return information about the most recent exception caught by an except
    clause in the current stack frame or in an older stack frame.

  +Builtin Function: excepthook
    excepthook(exctype, value, traceback) -> None

    Handle an exception by displaying it with a traceback on sys.stderr.


  +Builtin Function: exit
    exit([status])

    Exit the interpreter by raising SystemExit(status).
    If the status is omitted or None, it defaults to zero (i.e., success).
    If the status is an integer, it will be used as the system exit status.
    If it is another kind of object, it will be printed and the system
    exit status will be one (i.e., failure).

  +Builtin Function: getcheckinterval
    getcheckinterval() -> current check interval; see setcheckinterval().

  +Builtin Function: getdefaultencoding
    getdefaultencoding() -> string

    Return the current default string encoding used by the Unicode
    implementation.

  +Builtin Function: getdlopenflags
    getdlopenflags() -> int

    Return the current value of the flags that are used for dlopen calls.
    The flag constants are defined in the ctypes and DLFCN modules.

  +Builtin Function: getfilesystemencoding
    getfilesystemencoding() -> string

    Return the encoding used to convert Unicode filenames in
    operating system filenames.

  +Builtin Function: getprofile
    getprofile()

    Return the profiling function set with sys.setprofile.
    See the profiler chapter in the library manual.

  +Builtin Function: getrecursionlimit
    getrecursionlimit()

    Return the current value of the recursion limit, the maximum depth
    of the Python interpreter stack.  This limit prevents infinite
    recursion from causing an overflow of the C stack and crashing Python.

  +Builtin Function: getrefcount
    getrefcount(object) -> integer

    Return the reference count of object.  The count returned is generally
    one higher than you might expect, because it includes the (temporary)
    reference as an argument to getrefcount().

  +Builtin Function: getsizeof
    getsizeof(object, default) -> int

    Return the size of object in bytes.

  +Builtin Function: gettrace
    gettrace()

    Return the global debug tracing function set with sys.settrace.
    See the debugger chapter in the library manual.

  +Builtin Function: setcheckinterval
    setcheckinterval(n)

    Tell the Python interpreter to check for asynchronous events every
    n instructions.  This also affects how often thread switches occur.

  +Builtin Function: setdlopenflags
    setdlopenflags(n) -> None

    Set the flags used by the interpreter for dlopen calls, such as when the
    interpreter loads extension modules.  Among other things, this will enable
    a lazy resolving of symbols when importing a module, if called as
    sys.setdlopenflags(0).  To share symbols across extension modules, call as
    sys.setdlopenflags(ctypes.RTLD_GLOBAL).  Symbolic names for the flag modules
    can be either found in the ctypes module, or in the DLFCN module. If DLFCN
    is not available, it can be generated from /usr/include/dlfcn.h using the
    h2py script.

  +Builtin Function: setprofile
    setprofile(function)

    Set the profiling function.  It will be called on each function call
    and return.  See the profiler chapter in the library manual.

  +Builtin Function: setrecursionlimit
    setrecursionlimit(n)

    Set the maximum depth of the Python interpreter stack to n.  This
    limit prevents infinite recursion from causing an overflow of the C
    stack and crashing Python.  The highest possible limit is platform-
    dependent.

  +Builtin Function: settrace
    settrace(function)

    Set the global debug tracing function.  It will be called on each
    function call.  See the debugger chapter in the library manual.

```
