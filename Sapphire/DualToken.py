#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.DualToken')
def gem():
    require_gem('Sapphire.Elemental')
    require_gem('Sapphire.Whitespace')


    conjure_line_marker  = Shared.conjure_line_marker       #   Due to privileged
    lookup_adjusted_meta = Shared.lookup_adjusted_meta      #   Due to privileged
    lookup_line_marker   = Shared.lookup_line_marker        #   Due to privileged
    lookup_normal_token  = Shared.lookup_normal_token       #   Due to privileged
    provide_line_marker  = Shared.provide_line_marker       #   Due to privileged
    provide_normal_token = Shared.provide_normal_token      #   Due to privileged
    qi                   = Shared.qi                        #   Due to privileged
    qs                   = Shared.qs                        #   Due to privileged


    def construct_dual_token(t, s, a, b):
        assert (t.ends_in_newline is t.line_marker is false) and (t.newlines is 0)
        assert s == a.s + b.s
        assert '\n' not in s

        t.s = s
        t.a = a
        t.b = b


    def construct_dual_token__with_newlines(t, s, a, b, ends_in_newline, newlines):
        assert t.line_marker is false
        assert s == a.s + b.s
        assert ends_in_newline is (b.s[-1] == '\n')
        assert newlines >= 1

        t.s               = s
        t.a               = a
        t.b               = b
        t.ends_in_newline = ends_in_newline
        t.newlines        = newlines


    def construct_dual_operator__line_marker_1(t, s, a, b):
        assert (t.ends_in_newline is t.line_marker is true) and (t.newlines is 1)
        assert s == a.s + b.s
        assert s.count('\n') is 1
        assert b.s[-1] == '\n'

        t.s = s
        t.a = a
        t.b = b


    def construct_dual_token__line_marker__many(t, s, a, b, newlines):
        assert (t.ends_in_newline is t.line_marker is true) and (newlines >= 1)
        assert s == a.s + b.s
        assert s.count('\n') == newlines
        assert b.s[-1] == '\n'

        t.s        = s
        t.a        = a
        t.b        = b
        t.newlines = newlines


    class BaseDualOperator(KeywordAndOperatorBase):
        __slots__ = ((
            'a',                        #   Operator+
            'b',                        #   Operator+
        ))


        def __init__(t, s, a, b):
            assert (t.ends_in_newline is t.line_marker is false) and (t.newlines is 0)
            assert '\n' not in s
            assert s == a.s + b.s

            t.s = s
            t.a = a
            t.b = b


        def __repr__(t):
            return arrange('<%s %r %r>', t.__class__.__name__, t.a, t.b)


        def display_full_token(t):
            display_name = t.display_name
            a_s          = t.a.s
            b_s          = t.b.s

            return arrange('<%s <%s> <%s>>',
                           display_name,
                           portray_string(a_s)   if '\n' in a_s else   a_s,
                           portray_string(b_s)   if '\n' in b_s else   b_s)


        def display_token(t):
            display_name = t.display_name

            if display_name == t.s:
                return arrange('<%s>', display_name)

            a_s = t.a.s
            b_s = t.b.s

            return arrange('<%s <%s> <%s>>',
                           display_name,
                           portray_string(a_s)   if '\n' in a_s else   a_s,
                           portray_string(b_s)   if '\n' in b_s else   b_s)


    def create_dual_token__with_newlines(Meta, s, a, b):
        assert s == a.s + b.s

        newlines = s.count('\n')

        return (
                   Meta(s, a, b)
                       if newlines is 0 else
                           conjure_ActionWord_WithNewlines(
                                Meta, construct_dual_token__with_newlines,
                           )(s, a, b, s[-1] == '\n', newlines)
               )


    def create_dual_token__line_marker(Meta, s, a, b):
        assert (s == a.s + b.s) and (s[-1] == '\n')

        newlines = s.count('\n')

        return (
                   Meta(s, a, b)
                       if newlines is 1 else
                           conjure_ActionWord_LineMarker_Many(
                                Meta, construct_dual_token__line_marker__many
                           )(s, a, b, newlines)
               )


    @privileged
    def produce_conjure_dual_token(
            name, Meta,
            
            lookup      = lookup_normal_token,
            provide     = provide_normal_token,
            line_marker = false
    ):
        if line_marker:
            assert (lookup is lookup_normal_token) and (provide is provide_normal_token)

            create_dual_token = create_dual_token__line_marker
            lookup            = lookup_line_marker
            provide           = provide_line_marker
        else:
            create_dual_token = create_dual_token__with_newlines


        def conjure_dual_token(a, b):
            s = a.s + b.s

            r = lookup(s)

            if r is not none:
                if not ((r.a is a) and (r.b is b)):
                    my_line('s: %r; a: %r; b: %r; r: %r; T1: %r; T2: %r', s, a, b, r, r.a is a, r.b is b)

                assert (r.a is a) and (r.b is b)

                return r

            s = intern_string(s)

            return provide(s, create_dual_token__with_newlines(Meta, s, a, b))


        if __debug__:
            conjure_dual_token.__name__ = intern_arrange('conjure_%s', name)

        return conjure_dual_token


    @privileged
    def produce_evoke_dual_token(
            name, Meta, conjure_first,
            
            conjure_second                  = absent,
            conjure_second__ends_in_newline = absent,
            lookup                          = lookup_normal_token,
            provide                         = provide_normal_token,
            line_marker                     = false,
    ):
        assert type(line_marker) is Boolean

        if line_marker:
            assert (conjure_second is conjure_second__ends_in_newline is absent)
            assert (lookup is lookup_normal_token) and (provide is provide_normal_token)
        else:
            assert conjure_second is not absent

        if line_marker:
            def evoke_dual_token(a_end):
                assert qi() < a_end

                full_s = qs()[qi() : ]

                r = lookup_line_marker(full_s)
               
                if r is not none:
                    assert (type(r) is Meta) or (type(r) is lookup_adjusted_meta(Meta))

                    return r

                s      = qs()
                full_s = intern_string(full_s)

                return provide_line_marker(
                           full_s,
                           create_dual_token__line_marker(
                               Meta,
                               full_s,
                               conjure_first      (s[qi()  : a_end]),
                               conjure_line_marker(s[a_end :      ]),
                           ),
                       )
        elif conjure_second__ends_in_newline is absent:
            def evoke_dual_token(middle, end):
                assert qi() < middle < end

                full = qs()[qi() : end]

                r = lookup(full)
               
                if r is not none:
                    assert (type(r) is Meta) or (type(r) is lookup_adjusted_meta(Meta))

                    return r

                full = intern_string(full)
                s    = qs()

                return provide(
                           full,
                           create_dual_token__with_newlines(
                               Meta,
                               full,
                               conjure_first (s[qi()   : middle]),
                               conjure_second(s[middle : end   ]),
                           ),
                       )
        else:
            def evoke_dual_token(middle, end):
                if end is none:
                    assert qi() < middle
                else:
                    assert qi() < middle < end

                full = qs()[qi() : end]

                r = lookup(full)
               
                if r is not none:
                    assert (type(r) is Meta) or (type(r) is lookup_adjusted_meta(Meta))

                    return r

                full = intern_string(full)
                s    = qs()

                return provide(
                           full,
                           create_dual_token__with_newlines(
                               Meta,
                               full,
                               conjure_first(s[qi() : middle]),
                               (conjure_second__ends_in_newline   if end is none else   conjure_second)(s[middle : end]),
                           ),
                       )


        if __debug__:
            evoke_dual_token.__name__ = intern_arrange('evoke_%s', name)


        return evoke_dual_token


    class Arguments_0(BaseDualOperator):
        __slots__                             = (())
        display_name                          = '(0)'
        is__arguments_0__or__left_parenthesis = true
        is_arguments_0                        = true
        is_postfix_operator                   = true


    class Atom_Whitespace(BaseDualOperator):
        __slots__                      = (())
        display_name                   = 'atom+whitespace'
        is__atom__or__special_operator = true
        is_atom                        = true


    class Colon_RightSquareBracket(BaseDualOperator):
        __slots__                               = (())
        #   [
        display_name                            = ':]'
        is_colon__right_square_bracket          = true
        is_end_of_arithmetic_expression         = true
        is_end_of_boolean_and_expression        = true
        is_end_of_boolean_or_expression         = true
        is_end_of_compare_expression            = true
        is_end_of_comprehension_expression_list = true
        is_end_of_comprehension_expression      = true
        is_end_of_logical_and_expression        = true
        is_end_of_logical_or_expression         = true
        is_end_of_multiply_expression           = true
        is_end_of_normal_expression_list        = true
        is_end_of_normal_expression             = true
        is_end_of_ternary_expression_list       = true
        is_end_of_ternary_expression            = true
        is_end_of_unary_expression              = true


    class Comma_RightBrace(BaseDualOperator):
        __slots__    = (())
        #   {
        display_name = ',}'


    class Comma_RightParenthesis(BaseDualOperator):
        __slots__                             = (())
        #   (
        display_name                          = ',)'
        is_end_of_arithmetic_expression       = true
        is_end_of_boolean_and_expression      = true
        is_end_of_boolean_or_expression       = true
        is_end_of_compare_expression          = true
        is_end_of_comprehension_expression    = true
        is_end_of_logical_and_expression      = true
        is_end_of_logical_or_expression       = true
        is_end_of_multiply_expression         = true
        is_end_of_normal_expression           = true
        is_end_of_ternary_expression          = true
        is_end_of_unary_expression            = true
        is__optional_comma__right_parenthesis = true


    class Comma_RightSquareBracket(BaseDualOperator):
        __slots__                                = (())
        #   [
        display_name                             = ',]'
        is_end_of_arithmetic_expression          = true
        is_end_of_boolean_and_expression         = true
        is_end_of_boolean_or_expression          = true
        is_end_of_compare_expression             = true
        is_end_of_comprehension_expression       = true
        is_end_of_logical_and_expression         = true
        is_end_of_logical_or_expression          = true
        is_end_of_multiply_expression            = true
        is_end_of_normal_expression              = true
        is_end_of_ternary_expression             = true
        is_end_of_unary_expression               = true
        is__optional_comma__right_square_bracket = true


    class Dot_Name(BaseDualOperator):
        __slots__           = (())
        #   [
        display_name        = '.name'
        is_postfix_operator = true

    class DotNamePair(BaseDualOperator):
        __slots__           = (())
        #   [
        display_name        = '.name-pair'
        is_postfix_operator = true


    class EmptyList(BaseDualOperator):
        __slots__                      = (())
        display_name                   = '[,]'
        is__atom__or__special_operator = true
        is_atom                        = true


    class EmptyMap(BaseDualOperator):
        __slots__                      = (())
        display_name                   = '{:}'
        is__atom__or__special_operator = true
        is_atom                        = true


    class EmptyTuple(BaseDualOperator):
        __slots__                      = (())
        display_name                   = '{,}'
        is__atom__or__special_operator = true
        is_atom                        = true


    @share
    class Is_Not(BaseDualOperator):
        __slots__                        = (())
        display_name                     = 'is-not'
        is_compare_operator              = true
        is_end_of_arithmetic_expression  = true
        is_end_of_logical_and_expression = true
        is_end_of_logical_or_expression  = true
        is_end_of_normal_expression_list = true
        is_end_of_normal_expression      = true
        is_end_of_unary_expression       = true


    class LeftSquareBracket_Colon(BaseDualOperator):
        __slots__           = (())
        display_name        = '[:'                             #   ]
        is_postfix_operator = true
        is_tail_index       = true


    class Name_Whitespace(BaseDualOperator):
        __slots__                      = (())
        display_name                   = 'name+whitespace'
        is__atom__or__special_operator = true
        is_atom                        = true
        is_identifier                  = true


    @share
    class Not_In(BaseDualOperator):
        __slots__                        = (())
        display_name                     = 'not-in'
        is_compare_operator              = true
        is_end_of_arithmetic_expression  = true
        is_end_of_logical_and_expression = true
        is_end_of_logical_or_expression  = true
        is_end_of_normal_expression_list = true
        is_end_of_normal_expression      = true
        is_end_of_unary_expression       = true


    class RightParenthesis_Colon_LineMarker_1(BaseDualOperator):
        __slots__                                  = (())
        display_name                               = r'):\n'
        ends_in_newline                            = true
        is__any__right_parenthesis__colon__newline = true
        is__right_parenthesis__colon__newline      = true
        line_marker                                = true
        newlines                                   = 1


        __init__       = construct_dual_operator__line_marker_1
        count_newlines = count_newlines__line_marker


    class Whitespace_Atom(BaseDualOperator):
        __slots__                      = (())
        display_name                   = 'whitespace+atom'
        is__atom__or__special_operator = true
        is_atom                        = true


    class Whitespace_Name(BaseDualOperator):
        __slots__                      = (())
        display_name                   = 'whitespace+name'
        is__atom__or__special_operator = true
        is_atom                        = true
        is_identifier                  = true


    conjure_arguments_0 = produce_conjure_dual_token(
                              'arguments_0',
                              Arguments_0,

                              lookup  = lookup_arguments_0_token,
                              provide = provide_arguments_0_token,
                          )

    conjure__colon__right_square_bracket = produce_conjure_dual_token(
                                               'colon__right_square_bracket',
                                               Colon_RightSquareBracket,
                                           )

    conjure__comma__right_brace = produce_conjure_dual_token('comma__right_brace', Comma_RightBrace)

    conjure__comma__right_parenthesis = produce_conjure_dual_token(
                                            'comma__right_parenthesis',
                                            Comma_RightParenthesis,
                                        )

    conjure__comma__right_square_bracket = produce_conjure_dual_token(
                                               'comma__right_square_bracket',
                                               Comma_RightSquareBracket,
                                           )

    conjure_dot_name      = produce_conjure_dual_token('.name',      Dot_Name)
    conjure_dot_name_pair = produce_conjure_dual_token('.name-pair', DotNamePair)
    conjure_empty_list    = produce_conjure_dual_token('[]',         EmptyList)
    conjure_empty_map     = produce_conjure_dual_token('{}',         EmptyMap)
    conjure_is_not        = produce_conjure_dual_token('is-not',     Is_Not)

    conjure__left_square_bracket__colon = produce_conjure_dual_token(
                                              '[:',                           #   ]
                                              LeftSquareBracket_Colon,
                                          )

    conjure_not_in = produce_conjure_dual_token('not-in', Not_In)

    evoke_arguments_0 = produce_evoke_dual_token(
                            'arguments_0',
                            Arguments_0,
                            conjure_left_parenthesis,
                            conjure_right_parenthesis,
                            conjure_right_parenthesis__ends_in_newline,

                            lookup  = lookup_arguments_0_token,
                            provide = provide_arguments_0_token,
                        )

    evoke__colon__right_square_bracket = produce_evoke_dual_token(
                                             'colon__right_square_bracket',
                                             Colon_RightSquareBracket,
                                             conjure_colon,
                                             conjure_right_square_bracket,
                                             conjure_right_square_bracket__ends_in_newline,
                                         )

    evoke__comma__right_brace = produce_evoke_dual_token(
                                    'comma__right_brace',
                                    Comma_RightBrace,
                                    conjure_comma,
                                    conjure_right_brace,
                                    conjure_right_brace__ends_in_newline,
                                )

    evoke__comma__right_parenthesis = produce_evoke_dual_token(
                                          'comma__right_parenthesis',
                                          Comma_RightParenthesis,
                                          conjure_comma,
                                          conjure_right_parenthesis,
                                          conjure_right_parenthesis__ends_in_newline,
                                      )

    evoke__comma__right_square_bracket = produce_evoke_dual_token(
                                             'comma__right_square_bracket',
                                             Comma_RightSquareBracket,
                                             conjure_comma,
                                             conjure_right_square_bracket,
                                             conjure_right_square_bracket__ends_in_newline,
                                         )

    evoke__double_quote__whitespace = produce_evoke_dual_token(
                                          'double-quote+whitespace',
                                          Atom_Whitespace,
                                          conjure_double_quote,
                                          conjure_whitespace,
                                          conjure_whitespace__ends_in_newline,
                                      )

    evoke_empty_list = produce_evoke_dual_token(
                           '[]',
                           EmptyList,
                           conjure_left_square_bracket,
                           conjure_right_square_bracket,
                           conjure_right_square_bracket__ends_in_newline,
                       )

    evoke_empty_map = produce_evoke_dual_token(
                          '{}',
                          EmptyMap,
                          conjure_left_brace,
                          conjure_right_brace,
                          conjure_right_brace__ends_in_newline,
                      )

    evoke_empty_tuple = produce_evoke_dual_token(
                            '()',
                            EmptyTuple,
                            conjure_left_parenthesis,
                            conjure_right_parenthesis,
                            conjure_right_parenthesis__ends_in_newline,
                        )

    evoke_name_whitespace = produce_evoke_dual_token(
                                'name+whitespace',
                                Name_Whitespace,
                                conjure_name,
                                conjure_whitespace,
                                conjure_whitespace__ends_in_newline,
                            )

    evoke_number_whitespace = produce_evoke_dual_token(
                                  'number+whitespace',
                                  Atom_Whitespace,
                                  conjure_number,
                                  conjure_whitespace,
                                  conjure_whitespace__ends_in_newline,
                              )

    evoke_is_not = produce_evoke_dual_token(
                       'is_not',
                       Is_Not,
                       conjure_keyword_is,
                       conjure_keyword_not,
                       conjure_keyword_not__ends_in_newline,
                   )

    evoke__left_square_bracket__colon = produce_evoke_dual_token(
                                            '[:',                           #   ]
                                            LeftSquareBracket_Colon,
                                            conjure_left_square_bracket,
                                            conjure_colon,
                                            conjure_colon__ends_in_newline,
                                        )

    evoke_not_in = produce_evoke_dual_token(
                       'not_in',
                       Not_In,
                       conjure_keyword_not,
                       conjure_keyword_in,
                       conjure_keyword_in__ends_in_newline,
                   )

    evoke__single_quote__whitespace = produce_evoke_dual_token(
                                          'single-quote+whitespace',
                                          Atom_Whitespace,
                                          conjure_single_quote,
                                          conjure_whitespace,
                                          conjure_whitespace__ends_in_newline,
                                      )

    evoke_whitespace__double_quote = produce_evoke_dual_token(
                                         'whitespace+double-quote',
                                         Whitespace_Atom,
                                         conjure_whitespace,
                                         conjure_double_quote,
                                         none,
                                     )

    evoke_whitespace_name = produce_evoke_dual_token(
                                'whitespace+name',
                                Whitespace_Name,
                                conjure_whitespace,
                                conjure_name,
                                none,
                            )

    evoke_whitespace_number = produce_evoke_dual_token(
                                  'whitespace+number',
                                  Whitespace_Atom,
                                  conjure_whitespace,
                                  conjure_number,
                                  none,
                              )

    evoke_whitespace__single_quote = produce_evoke_dual_token(
                                         'whitespace+single-quote',
                                         Whitespace_Atom,
                                         conjure_whitespace,
                                         conjure_single_quote,
                                         none,
                                     )

    find_evoke_comma_something = {
                                     #   (
                                     ')' : evoke__comma__right_parenthesis,

                                     #   [
                                     ']' : evoke__comma__right_square_bracket,
                                 }.__getitem__

    find_evoke_atom_whitespace = {
            '"' : evoke__double_quote__whitespace,
            "'" : evoke__single_quote__whitespace,

            '.' : evoke_number_whitespace,
            '0' : evoke_number_whitespace, '1' : evoke_number_whitespace, '2' : evoke_number_whitespace,
            '3' : evoke_number_whitespace, '4' : evoke_number_whitespace, '5' : evoke_number_whitespace,
            '6' : evoke_number_whitespace, '7' : evoke_number_whitespace, '8' : evoke_number_whitespace,
            '9' : evoke_number_whitespace,

            'A' : evoke_name_whitespace, 'B' : evoke_name_whitespace, 'C' : evoke_name_whitespace,
            'D' : evoke_name_whitespace, 'E' : evoke_name_whitespace, 'F' : evoke_name_whitespace,
            'G' : evoke_name_whitespace, 'H' : evoke_name_whitespace, 'I' : evoke_name_whitespace,
            'J' : evoke_name_whitespace, 'K' : evoke_name_whitespace, 'L' : evoke_name_whitespace,
            'M' : evoke_name_whitespace, 'N' : evoke_name_whitespace, 'O' : evoke_name_whitespace,
            'P' : evoke_name_whitespace, 'Q' : evoke_name_whitespace, 'R' : evoke_name_whitespace,
            'S' : evoke_name_whitespace, 'T' : evoke_name_whitespace, 'U' : evoke_name_whitespace,
            'V' : evoke_name_whitespace, 'W' : evoke_name_whitespace, 'X' : evoke_name_whitespace,
            'Y' : evoke_name_whitespace, 'Z' : evoke_name_whitespace, '_' : evoke_name_whitespace,

            'a' : evoke_name_whitespace, 'b' : evoke_name_whitespace, 'c' : evoke_name_whitespace,
            'd' : evoke_name_whitespace, 'e' : evoke_name_whitespace, 'f' : evoke_name_whitespace,
            'g' : evoke_name_whitespace, 'h' : evoke_name_whitespace, 'i' : evoke_name_whitespace,
            'j' : evoke_name_whitespace, 'k' : evoke_name_whitespace, 'l' : evoke_name_whitespace,
            'm' : evoke_name_whitespace, 'n' : evoke_name_whitespace, 'o' : evoke_name_whitespace,
            'p' : evoke_name_whitespace, 'q' : evoke_name_whitespace, 'r' : evoke_name_whitespace,
            's' : evoke_name_whitespace, 't' : evoke_name_whitespace, 'u' : evoke_name_whitespace,
            'v' : evoke_name_whitespace, 'w' : evoke_name_whitespace, 'x' : evoke_name_whitespace,
            'y' : evoke_name_whitespace, 'z' : evoke_name_whitespace,
        }.__getitem__

    find_evoke_whitespace_atom = {
            '"' : evoke_whitespace__double_quote,
            "'" : evoke_whitespace__single_quote,

            '.' : evoke_whitespace_number,
            '0' : evoke_whitespace_number, '1' : evoke_whitespace_number, '2' : evoke_whitespace_number,
            '3' : evoke_whitespace_number, '4' : evoke_whitespace_number, '5' : evoke_whitespace_number,
            '6' : evoke_whitespace_number, '7' : evoke_whitespace_number, '8' : evoke_whitespace_number,
            '9' : evoke_whitespace_number,

            'A' : evoke_whitespace_name, 'B' : evoke_whitespace_name, 'C' : evoke_whitespace_name,
            'D' : evoke_whitespace_name, 'E' : evoke_whitespace_name, 'F' : evoke_whitespace_name,
            'G' : evoke_whitespace_name, 'H' : evoke_whitespace_name, 'I' : evoke_whitespace_name,
            'J' : evoke_whitespace_name, 'K' : evoke_whitespace_name, 'L' : evoke_whitespace_name,
            'M' : evoke_whitespace_name, 'N' : evoke_whitespace_name, 'O' : evoke_whitespace_name,
            'P' : evoke_whitespace_name, 'Q' : evoke_whitespace_name, 'R' : evoke_whitespace_name,
            'S' : evoke_whitespace_name, 'T' : evoke_whitespace_name, 'U' : evoke_whitespace_name,
            'V' : evoke_whitespace_name, 'W' : evoke_whitespace_name, 'X' : evoke_whitespace_name,
            'Y' : evoke_whitespace_name, 'Z' : evoke_whitespace_name, '_' : evoke_whitespace_name,

            'a' : evoke_whitespace_name, 'b' : evoke_whitespace_name, 'c' : evoke_whitespace_name,
            'd' : evoke_whitespace_name, 'e' : evoke_whitespace_name, 'f' : evoke_whitespace_name,
            'g' : evoke_whitespace_name, 'h' : evoke_whitespace_name, 'i' : evoke_whitespace_name,
            'j' : evoke_whitespace_name, 'k' : evoke_whitespace_name, 'l' : evoke_whitespace_name,
            'm' : evoke_whitespace_name, 'n' : evoke_whitespace_name, 'o' : evoke_whitespace_name,
            'p' : evoke_whitespace_name, 'q' : evoke_whitespace_name, 'r' : evoke_whitespace_name,
            's' : evoke_whitespace_name, 't' : evoke_whitespace_name, 'u' : evoke_whitespace_name,
            'v' : evoke_whitespace_name, 'w' : evoke_whitespace_name, 'x' : evoke_whitespace_name,
            'y' : evoke_whitespace_name, 'z' : evoke_whitespace_name,
        }.__getitem__


    share(
        'conjure_arguments_0',                      conjure_arguments_0,
        'conjure__colon__right_square_bracket',     conjure__colon__right_square_bracket,
        'conjure__comma__right_brace',              conjure__comma__right_brace,
        'conjure__comma__right_parenthesis',        conjure__comma__right_parenthesis,
        'conjure__comma__right_square_bracket',     conjure__comma__right_square_bracket,
        'conjure_dot_name',                         conjure_dot_name,
        'conjure_dot_name_pair',                    conjure_dot_name_pair,
        'conjure_empty_list',                       conjure_empty_list,
        'conjure_empty_map',                        conjure_empty_map,
        'conjure_is_not',                           conjure_is_not,
        'conjure__left_square_bracket__colon',      conjure__left_square_bracket__colon,
        'conjure_not_in',                           conjure_not_in,
        'evoke_arguments_0',                        evoke_arguments_0,
        'evoke__colon__right_square_bracket',       evoke__colon__right_square_bracket,
        'evoke__comma__right_brace',                evoke__comma__right_brace,
        'evoke__comma__right_parenthesis',          evoke__comma__right_parenthesis,
        'evoke_empty_list',                         evoke_empty_list,
        'evoke_empty_map',                          evoke_empty_map,
        'evoke_empty_tuple',                        evoke_empty_tuple,
        'evoke_is_not',                             evoke_is_not,
        'evoke__left_square_bracket__colon',        evoke__left_square_bracket__colon,
        'evoke_name_whitespace',                    evoke_name_whitespace,
        'evoke_not_in',                             evoke_not_in,
        'evoke_whitespace_name',                    evoke_whitespace_name,
        'find_evoke_atom_whitespace',               find_evoke_atom_whitespace,
        'find_evoke_comma_something',               find_evoke_comma_something,
        'find_evoke_whitespace_atom',               find_evoke_whitespace_atom,
    )
