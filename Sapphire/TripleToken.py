#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.TripleToken')
def gem():
    class BaseTripleOperator(KeywordAndOperatorBase):
        __slots__ = ((
            'first',         #   Operator+
            'second',        #   Operator+
            'third',         #   Operator+
        ))


        ends_in_python_newline = false
        newlines               = 0
        MetaWithNewline        = 0


        def __init__(t, s, first, second, third):
            assert '\n' not in s
            assert s == first.s + second.s + third.s

            t.s      = s
            t.first  = first
            t.second = second
            t.third  = third


        def __repr__(t):
            return arrange('<%s %r %r %r>', t.__class__.__name__, t.first, t.second, t.third)


        def display_full_token(t):
            display_name = t.display_name
            first_s      = t.first.s
            second_s     = t.second.s

            return arrange('<%s <%s> <%s>>',
                           display_name,
                           portray_string(first_s)    if '\n' in first_s  else   first_s,
                           portray_string(second_s)   if '\n' in second_s else   second_s)


        def display_token(t):
            display_name = t.display_name

            if display_name == t.s:
                return display_name

            first_s  = t.first .s
            second_s = t.second.s
            third_s  = t.third .s

            return arrange('<%s <%s> <%s> <%s>>',
                           display_name,
                           portray_string(first_s)    if '\n' in first_s  else   first_s,
                           portray_string(second_s)   if '\n' in second_s else   second_s,
                           portray_string(third_s)    if '\n' in third_s  else   third_s)


        def write(t, w):
            w(t.first.s + t.second.s + t.third.s)


    class AllIndex(BaseTripleOperator):
        __slots__    = (())
        display_name = '[:]'


    class Comma_RightParenthesis_Colon_PythonNewline(BaseTripleOperator):
        __slots__                                  = (())
        display_name                               = r',):\n'
        is__any__right_parenthesis__colon__newline = true
        Meta_Many                                  = 0
        newlines                                   = 1


    class Parameter_0__Colon__Newline(BaseTripleOperator):
        display_name                 = r'():\n'
        is_any_parameter_colon_0     = true
        is_parameter_colon_0_newline = true
        Meta_Many                    = 0
        newlines                     = 1


        def __init__(t, s, first, second, third):
            assert s.count('\n') is 1
            assert s == first.s + second.s + third.s
            assert third.s[-1] is '\n'

            t.s      = s
            t.first  = first
            t.second = second
            t.third  = third


    def construct_triple_token_with_newlines(t, s, first, second, third, newlines, ends_in_newline):
        assert newlines >= 1
        assert ends_in_newline is (s[-1] == '\n')

        t.s               = s
        t.first           = first
        t.second          = second
        t.third           = third
        t.newlines        = newlines
        t.ends_in_newline = ends_in_newline


    def construct_triple_token_with_python_newline(t, s, first, second, third, newlines):
        assert newlines >= 1
        assert s[-1] == '\n'

        t.s        = s
        t.first    = first
        t.second   = second
        t.third    = third
        t.newlines = newlines


    def create_triple_token_with_newline(Meta, first, second, third):
        s = intern_string(first.s + second.s + third.s)

        newlines = s.count('\n')

        if newlines is 0:
            return Meta(s, first, second, third)

        MetaWithNewline = Meta.MetaWithNewline

        if MetaWithNewline is 0:
            MetaWithNewline = Meta.MetaWithNewline = create_MetaWithNewline(Meta, construct_triple_token_with_newlines)

        return MetaWithNewline(s, first, second, third, newlines, s[-1] == '\n')


    def create_triple_token_with_python_newline(Meta, first, second, third):
        s = intern_string(first.s + second.s + third.s)

        newlines = s.count('\n')

        if newlines is 1:
            return Meta(s, first, second, third)

        Meta_Many = Meta.Meta_Many

        if Meta_Many is 0:
            Meta_Many = Meta.Meta_Many = create_Meta_Many(Meta, construct_triple_token_with_python_newline)

        return Meta_Many(s, first, second, third, newlines)


    @privileged
    def produce_conjure_triple_token(name, Meta, ends_in_python_newline = false):
        assert type(ends_in_python_newline) is Boolean

        cache     = {}
        provide_1 = cache.setdefault
        lookup_1  = cache.get
        store_1   = cache.__setitem__

        create_triple_token = (
                create_triple_token_with_python_newline   if ends_in_python_newline else  
                create_triple_token_with_newline
            )


        def conjure_triple_token(first, second, third):
            v = lookup_1(first)

            if v is none:
                return provide_1(first, create_triple_token(Meta, first, second, third))

            if type(v) is Map:
                w = v.get(second)

                if w is none:
                    return v.setdefault(second, create_triple_token(Meta, first, second, third))

                if type(w) is Map:
                    return (w.get(third)) or (w.setdefault(third, create_triple_token(Meta, first, second, third)))

                if w.third is third:
                    return w

                r = create_triple_token(Meta, first, second, third)

                v[second] = { w.third : v, third : r }

                return r

            if v.second is second:
                if v.third is third:
                    return v

                r = create_triple_token(Meta, first, second, third)

                store_1(first, { second : { third : v, third: r } })

                return r

            r = create_triple_token(Meta, first, second, third)

            store_1(first, { v.second : v , second : r })

            return r


        if __debug__:
            conjure_triple_token.__name__ = intern_arrange('conjure_%s', name)


        return conjure_triple_token


    conjure_all_index = produce_conjure_triple_token('all_index', AllIndex)

    conjure__comma__right_parenthesis__colon__python_newline = produce_conjure_triple_token(
            'comma__right_parenthesis__colon__python_newline',
            Comma_RightParenthesis_Colon_PythonNewline,
            true,
        )

    conjure__parameter_0__colon_newline = produce_conjure_triple_token(
            'parameter_0__colon_newline',
            Parameter_0__Colon__Newline,
        )

    share(
        'conjure_all_index',    conjure_all_index,

        'conjure__comma__right_parenthesis__colon__python_newline',
            conjure__comma__right_parenthesis__colon__python_newline,

        'conjure__parameter_0__colon_newline',  conjure__parameter_0__colon_newline,
    )
