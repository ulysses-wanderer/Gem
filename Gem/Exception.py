#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Gem.Exception')
def gem():
    require_gem('Gem.Import')


    PythonException = (import_module('exceptions')   if is_python_2 else  PythonBuiltIn)


    BaseException = PythonException.BaseException
    RuntimeError  = PythonException.RuntimeError
    StopIteration = PythonException.StopIteration
    ValueError    = PythonException.ValueError


    exception_information = PythonSystem.exc_info
    stop_iteration        = StopIteration()


    if is_python_3:
        class CaughtExceptionContext(Object):
            __slots__ = ((
                'e',
            ))


            def __init__(t, e):
                assert is_instance(e, BaseException)

                t.e = e

            def __enter__(t):
                return t.e

            
            def __exit__(t, e_type, e, e_traceback):
                pass
    else:
        class CaughtExceptionContext(Object):
            __slots__ = ((
                'e',                        #   BaseException+
                'exception_stack',          #   List of BaseException+
            ))


            def __init__(t, e):
                assert is_instance(e, BaseException)

                t.e               = e
                t.exception_stack = thread_context.exception_stack


            def __enter__(t):
                e = t.e

                t.exception_stack.append(e)
                thread_context.exception_context = e

                return e


            def __exit__(t, e_type, e, e_traceback):
                last_exception = t.e

                if e is not none:
                    if '__cause__' in e.__dict__:
                        assert '__context__'          in e.__dict__
                        assert '__suppress_context__' in e.__dict__
                        assert '__traceback__'        in e.__dict__
                    else:
                        assert '__context__'          not in e.__dict__
                        assert '__suppress_context__' not in e.__dict__
                        assert '__traceback__'        not in e.__dict__
                
                        e.__cause__            = none
                        e.__context__          = (none   if e is last_exception else   last_exception)
                        e.__suppress_context__ = false
                        e.__traceback__        = none

                exception_stack = t.exception_stack

                e = exception_stack.pop()

                assert e is last_exception

                thread_context.exception_context = (none   if length(exception_stack) is 0 else   exception_stack[-1])


    #
    #   NOTE:
    #       Do not use 'hasattr' or 'getattr' here for multiple reasons:
    #
    #       1.  Mainly 'hasattr' is defective (in that it can hide underlying errors in user functions);
    #       2.  Don't want to call user functions; and
    #       3.  Don't want to handle the complexity of extra exceptions here.
    #
    #   THUS:
    #
    #       The Python 2.0 implementation of __cause__, __context__, __suppress_context__, __traceback__
    #       is limited to members in __dict__ (i.e.: no __slots__ or other implementation via __getattr__
    #       or __getattribute__).
    #
    if is_python_3:
        if __debug__:
            @export
            def caught_any_exception():
                [e_type, e, e_traceback] = exception_information()

                assert type(e) is e_type

                assert is_instance(e, BaseException)
                assert (e.__cause__   is none) or is_instance(e.__cause__,   BaseException)
                assert (e.__context__ is none) or is_instance(e.__context__, BaseException)
                assert type(e.__suppress_context__) is Boolean
                assert type(e.__traceback__)        is Traceback

                assert type(e_traceback) is Traceback

                return CaughtExceptionContext(e)
        else:
            @export
            def caught_any_exception():
                return CaughtExceptionContext(exception_information()[0])


        if __debug__:
            @export
            def caught_exception(e):
                assert is_instance(e, BaseException)

                assert (e.__cause__   is none) or is_instance(e.__cause__,   BaseException)
                assert (e.__context__ is none) or is_instance(e.__context__, BaseException)
                assert type(e.__suppress_context__) is Boolean
                assert type(e.__traceback__)        is Traceback

                return CaughtExceptionContext(e)
        else:
            @export
            def caught_exception(e):
                return CaughtExceptionContext(e)


        @export
        def handled_exception(e):
            pass
    else:
        def fixup_caught_exception(e):
            assert is_instance(e, BaseException)

            contains = e.__dict__.__contains__

            if contains('__cause__'):
                assert (e.__cause__ is none) or is_instance(e.__cause__, BaseException)
            else:
                e.__cause__ = none

            if contains('__context__'):
                assert (e.__context__ is none) or is_instance(e.__context__, BaseException)
            else:
                e.__context__ = none

            if contains('__suppress_context__'):
                assert type(e.__suppress_context__) is Boolean
            else:
                e.__suppress_context__ = false
                
            if contains('__traceback__'):
                if e.__traceback__ is none:
                    return true

                assert type(e.__traceback__) is Traceback

                return false

            return true


        @export
        def caught_any_exception():
            [e_type, e, e_traceback] = exception_information()

            assert type(e) is e_type

            if fixup_caught_exception(e):
                e.__traceback__ = e_traceback

            assert type(e_traceback) is Traceback

            return CaughtExceptionContext(e)


        @export
        def caught_exception(e):
            if fixup_caught_exception(e):
                e.__traceback__ = exception_information()[2]

            return CaughtExceptionContext(e)


        @export
        def handled_exception(e):
            if main_context.exception_context is e:
                main_context.exception_context = none


    #
    #   NOTE:
    #       Lines with 'raise' will appear in stack traces, so make them look prettier by using
    #       a precalculated variable like 'runtime_error' (to make the line shorter & more readable)
    #       instead of doing the calculation on the line with 'raise'.
    #


    #
    #   raise_runtime_error
    #
    @built_in
    def raise_runtime_error(format, *arguments):
        runtime_error = RuntimeError(format   % arguments   if arguments else   format)

        raising_exception(runtime_error)
        
        raise runtime_error


    #
    #   raise_value_error
    #
    @built_in
    def raise_value_error(format, *arguments):
        value_error = ValueError(format % arguments)

        raising_exception(value_error)

        raise value_error


    if is_python_2:
        EnvironmentError           = PythonException.EnvironmentError
        construct_EnvironmentError = EnvironmentError.__init__


        class FileNotFoundError(EnvironmentError):
            __slots__ = ((
                'filename2',                #   None | String
            ))


            def __init__(t, error_number, message, path = none, path2 = none):
                construct_EnvironmentError(t, error_number, message, path)

                t.filename2 = path2

                #
                #  Stored in __dict__[*]
                #
                t.__traceback__        = t.__context__ = t.__cause__ = none
                t.__suppress_context__ = false


            def __str__(t):
                if t.filename2 is none:
                    return arrange('[Errno %d] %s: %r', t.args[0], t.args[1], t.filename)

                return arrange('[Errno %d] %s: %r -> %r', t.args[0], t.args[1], t.filename, t.filename2)


        class PermissionError(EnvironmentError):
            pass
    else:
        FileNotFoundError = PythonBuiltIn.FileNotFoundError
        PermissionError   = PythonBuiltIn.PermissionError


    export(
        #
        #   Exception Types
        #
        'BaseException',        BaseException,
        'Exception',            PythonException.Exception,
        'FileNotFoundError',    FileNotFoundError,
        'ImportError',          PythonException.ImportError,
        'OSError',              PythonException.OSError,
        'PermissionError',      PermissionError,
        'StopIteration',        StopIteration,

        #
        #   Functions
        #
        'caught_any_exception',     caught_any_exception,

        #
        #   'values'
        #
        'stop_iteration',       stop_iteration,
    )
