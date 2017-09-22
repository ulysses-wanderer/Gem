#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.TripleToken')
def gem():
    conjure_line_marker  = Shared.conjure_line_marker       #   Due to privileged
    lookup_adjusted_meta = Shared.lookup_adjusted_meta      #   Due to privileged
    lookup_line_marker   = Shared.lookup_line_marker        #   Due to privileged
    lookup_normal_token  = Shared.lookup_normal_token       #   Due to privileged
    provide_line_marker  = Shared.provide_line_marker       #   Due to privileged
    provide_normal_token = Shared.provide_normal_token      #   Due to privileged
    qi                   = Shared.qi                        #   Due to privileged
    qs                   = Shared.qs                        #   Due to privileged


    def construct_triple_token(t, s, a, b, c):
        assert (t.ends_in_newline is t.line_marker is false) and (t.newlines is 0)
        assert s == a.s + b.s + c.s
        assert '\n' not in s

        t.s      = s
        t.a  = a
        t.b = b
        t.c  = c


    def construct_triple_token__with_newlines(t, s, a, b, c, newlines, ends_in_newline):
        assert t.line_marker is false
        assert s == a.s + b.s + c.s
        assert ends_in_newline is (c.s[-1] == '\n')
        assert newlines >= 1

        t.s               = s
        t.a           = a
        t.b          = b
        t.c           = c
        t.newlines        = newlines
        t.ends_in_newline = ends_in_newline


    def construct_triple_operator__line_marker_1(t, s, a, b, c):
        assert (t.ends_in_newline is t.line_marker is true) and (t.newlines is 1)
        assert s == a.s + b.s + c.s
        assert s.count('\n') is 1
        assert c.s[-1] == '\n'

        t.s      = s
        t.a  = a
        t.b = b
        t.c  = c


    def construct_triple_token__line_marker__many(t, s, a, b, c, newlines):
        assert (t.ends_in_newline is t.line_marker is true) and (newlines > 1)
        assert s == a.s + b.s + c.s
        assert s.count('\n') == newlines
        assert c.s[-1] == '\n'

        t.s        = s
        t.a    = a
        t.b   = b
        t.c    = c
        t.newlines = newlines


    class BaseTripleOperator(KeywordAndOperatorBase):
        __slots__ = ((
            'a',         #   Operator+
            'b',        #   Operator+
            'c',         #   Operator+
        ))


        __init__ = construct_triple_token


        def __repr__(t):
            return arrange('<%s %r %r %r>', t.__class__.__name__, t.a, t.b, t.c)


        def display_full_token(t):
            display_name = t.display_name
            a_s          = t.a.s
            b_s          = t.b.s
            c_s          = t.c.s

            return arrange('<%s <%s> <%s> <%s>>',
                           display_name,
                           (portray_string(a_s)   if '\n' in a_s else   a_s),
                           (portray_string(b_s)   if '\n' in b_s else   b_s),
                           (portray_string(c_s)   if '\n' in c_s else   c_s))


        def display_token(t):
            display_name = t.display_name

            if display_name == t.s:
                return display_name

            a_s = t.a.s
            b_s = t.b.s
            c_s = t.c.s

            return arrange('<%s <%s> <%s> <%s>>',
                           display_name,
                           (portray_string(a_s)   if '\n' in a_s else   a_s),
                           (portray_string(b_s)   if '\n' in b_s else   b_s),
                           (portray_string(c_s)   if '\n' in c_s else   c_s))


    class AllIndex(BaseTripleOperator):
        __slots__           = (())
        display_name        = '[:]'
        is_all_index        = true
        is_postfix_operator = true


    class RightParenthesis_Colon_LineMarker_1(BaseTripleOperator):
        __slots__                                  = (())
        display_name                               = r'):\n'
        ends_in_newline                            = true
        is__any__right_parenthesis__colon__newline = true
        is__right_parenthesis__colon__newline      = true
        line_marker                                = true
        newlines                                   = 1


        __init__ = construct_triple_operator__line_marker_1


    class Whitespace_Atom_Whitespace(BaseTripleOperator):
        __slots__                      = (())
        display_name                   = 'whitespace+atom+whitespace'
        is__atom__or__special_operator = true
        is_atom                        = true


    class Whitespace_Name_Whitespace(BaseTripleOperator):
        __slots__                      = (())
        display_name                   = 'whitespace+name+whitespace'
        is__atom__or__special_operator = true
        is_atom                        = true
        is_identifier                  = true


    def create_triple_token__with_newlines(Meta, s, a, b, c):
        assert s == a.s + b.s + c.s

        newlines = s.count('\n')

        return (
                   Meta(s, a, b, c)
                       if newlines is 0 else
                           (
                                 lookup_adjusted_meta(Meta)
                              or create_ActionWord_WithNewlines(Meta, construct_triple_token__with_newlines)
                           )(s, a, b, c, newlines, s[-1] == '\n')
               )


    def create_triple_token__line_marker(Meta, s, a, b, c):
        assert (s == a.s + b.s + c.s) and (s[-1] == '\n')

        newlines = s.count('\n')

        return (
                   Meta(s, a, b, c)
                       if newlines is 1 else
                       (
                             lookup_adjusted_meta(Meta)
                          or create_ActionWord_LineMarker_Many(Meta, construct_triple_token__line_marker__many)
                       )(s, a, b, c, newlines)
               )


    @privileged
    def produce_conjure_triple_token(
            name, Meta,
            
            lookup      = lookup_normal_token,
            provide     = provide_normal_token,
            line_marker = false
    ):
        if line_marker:
            assert (lookup is lookup_normal_token) and (provide is provide_normal_token)

            create_triple_token = create_triple_token__line_marker
            lookup              = lookup_line_marker
            provide             = provide_line_marker
        else:
            create_triple_token = create_triple_token__with_newlines


        def conjure_triple_token(a, b, c):
            s = a.s + b.s + c.s

            r = lookup(s)

            if r is not none:
                assert (r.a is a) and (r.b is b) and (r.c is c)

                return r

            s = intern_string(s)

            return provide(s, create_triple_token(Meta, s, a, b, c))


        if __debug__:
            conjure_triple_token.__name__ = intern_arrange('conjure_%s', name)

        return conjure_triple_token


    @privileged
    def produce_evoke_triple_token(
            name, Meta, conjure_a, conjure_b,
            
            conjure_c                  = absent,
            conjure_c__ends_in_newline = absent,
            lookup                     = lookup_normal_token,
            provide                    = provide_normal_token,
            line_marker                = false,
    ):
        assert type(line_marker) is Boolean


        if line_marker:
            assert (lookup is lookup_normal_token) and (provide is provide_normal_token)
            assert (conjure_c is conjure_c__ends_in_newline is absent)


            def evoke_triple_token(a_end, b_end):
                assert qi() < a_end < b_end

                triple_s = qs()[qi() : ]

                r = lookup_line_marker(triple_s)
               
                if r is not none:
                    assert (type(r) is Meta) or (type(r) is lookup_adjusted_meta(Meta))

                    return r

                s        = qs()
                triple_s = intern_string(triple_s)

                return provide_line_marker(
                           triple_s,
                           create_triple_token__line_marker(
                               Meta,
                               triple_s,
                               conjure_a          (s[qi()  : a_end]),
                               conjure_b          (s[a_end : b_end]),
                               conjure_line_marker(s[b_end :      ]),
                           ),
                       )
        else:
            def evoke_triple_token(a_end, b_end, c_end):
                assert qi() < a_end < b_end

                full = qs()[qi() : c_end]

                r = lookup(full)
               
                if r is not none:
                    assert (type(r) is Meta) or (type(r) is lookup_adjusted_meta(Meta))

                    return r

                full = intern_string(full)
                s    = qs()

                return provide(
                           full,
                           create_triple_token__with_newlines(
                               Meta,
                               full,
                               conjure_a(s[qi()  : a_end]),
                               conjure_b(s[a_end : b_end]),
                               (conjure_c__ends_in_newline   if c_end is none else   conjure_c)(s[b_end : c_end]),
                           ),
                       )


        if __debug__:
            evoke_triple_token.__name__ = intern_arrange('evoke_%s', name)


        return evoke_triple_token


    conjure_all_index = produce_conjure_triple_token('all_index', AllIndex)

    conjure__right_parenthesis__colon__line_marker = produce_conjure_triple_token(
                                                         'right_parenthesis__colon__line_marker',
                                                         RightParenthesis_Colon_LineMarker_1,

                                                         line_marker = true
                                                     )

    evoke_all_index = produce_evoke_triple_token(
                          'all_index',
                          AllIndex,
                          conjure_left_square_bracket,
                          conjure_colon,
                          conjure_right_square_bracket,
                          conjure_right_square_bracket__ends_in_newline,
                      )


    evoke__right_parenthesis__colon__line_marker = produce_evoke_triple_token(
                                                       'right_parenthesis__colon__line_marker',
                                                       RightParenthesis_Colon_LineMarker_1,
                                                       conjure_right_parenthesis,
                                                       conjure_colon,

                                                       line_marker = true,
                                                   )

    evoke_whitespace__double_quote__whitespace = produce_evoke_triple_token(
                                                     'whitespace+double-quote+whitespace',
                                                     Whitespace_Atom_Whitespace,
                                                     conjure_whitespace,
                                                     conjure_double_quote,
                                                     conjure_whitespace,
                                                     conjure_whitespace__ends_in_newline,
                                                 )

    evoke_whitespace_name_whitespace = produce_evoke_triple_token(
                                           'whitespace+name+whitespace',
                                           Whitespace_Name_Whitespace,
                                           conjure_whitespace,
                                           conjure_name,
                                           conjure_whitespace,
                                           conjure_whitespace__ends_in_newline,
                                       )

    evoke_whitespace_number_whitespace = produce_evoke_triple_token(
                                             'whitespace+number+whitespace',
                                             Whitespace_Atom_Whitespace,
                                             conjure_whitespace,
                                             conjure_number,
                                             conjure_whitespace,
                                             conjure_whitespace__ends_in_newline,
                                         )

    evoke_whitespace__single_quote__whitespace = produce_evoke_triple_token(
                                                     'whitespace+single-quote+whitespace',
                                                     Whitespace_Atom_Whitespace,
                                                     conjure_whitespace,
                                                     conjure_single_quote,
                                                     conjure_whitespace,
                                                     conjure_whitespace__ends_in_newline,
                                                 )

    find_evoke_whitespace_atom_whitespace = {
            '"' : evoke_whitespace__double_quote__whitespace,
            "'" : evoke_whitespace__single_quote__whitespace,

            '.' : evoke_whitespace_number_whitespace,
            '0' : evoke_whitespace_number_whitespace, '1' : evoke_whitespace_number_whitespace,
            '2' : evoke_whitespace_number_whitespace, '3' : evoke_whitespace_number_whitespace,
            '4' : evoke_whitespace_number_whitespace, '5' : evoke_whitespace_number_whitespace,
            '6' : evoke_whitespace_number_whitespace, '7' : evoke_whitespace_number_whitespace,
            '8' : evoke_whitespace_number_whitespace, '9' : evoke_whitespace_number_whitespace,

            'A' : evoke_whitespace_name_whitespace, 'B' : evoke_whitespace_name_whitespace,
            'C' : evoke_whitespace_name_whitespace, 'D' : evoke_whitespace_name_whitespace,
            'E' : evoke_whitespace_name_whitespace, 'F' : evoke_whitespace_name_whitespace,
            'G' : evoke_whitespace_name_whitespace, 'H' : evoke_whitespace_name_whitespace,
            'I' : evoke_whitespace_name_whitespace, 'J' : evoke_whitespace_name_whitespace,
            'K' : evoke_whitespace_name_whitespace, 'L' : evoke_whitespace_name_whitespace,
            'M' : evoke_whitespace_name_whitespace, 'N' : evoke_whitespace_name_whitespace,
            'O' : evoke_whitespace_name_whitespace, 'P' : evoke_whitespace_name_whitespace,
            'Q' : evoke_whitespace_name_whitespace, 'R' : evoke_whitespace_name_whitespace,
            'S' : evoke_whitespace_name_whitespace, 'T' : evoke_whitespace_name_whitespace,
            'U' : evoke_whitespace_name_whitespace, 'V' : evoke_whitespace_name_whitespace,
            'W' : evoke_whitespace_name_whitespace, 'X' : evoke_whitespace_name_whitespace,
            'Y' : evoke_whitespace_name_whitespace, 'Z' : evoke_whitespace_name_whitespace,
            '_' : evoke_whitespace_name_whitespace,

            'a' : evoke_whitespace_name_whitespace, 'b' : evoke_whitespace_name_whitespace,
            'c' : evoke_whitespace_name_whitespace, 'd' : evoke_whitespace_name_whitespace,
            'e' : evoke_whitespace_name_whitespace, 'f' : evoke_whitespace_name_whitespace,
            'g' : evoke_whitespace_name_whitespace, 'h' : evoke_whitespace_name_whitespace,
            'i' : evoke_whitespace_name_whitespace, 'j' : evoke_whitespace_name_whitespace,
            'k' : evoke_whitespace_name_whitespace, 'l' : evoke_whitespace_name_whitespace,
            'm' : evoke_whitespace_name_whitespace, 'n' : evoke_whitespace_name_whitespace,
            'o' : evoke_whitespace_name_whitespace, 'p' : evoke_whitespace_name_whitespace,
            'q' : evoke_whitespace_name_whitespace, 'r' : evoke_whitespace_name_whitespace,
            's' : evoke_whitespace_name_whitespace, 't' : evoke_whitespace_name_whitespace,
            'u' : evoke_whitespace_name_whitespace, 'v' : evoke_whitespace_name_whitespace,
            'w' : evoke_whitespace_name_whitespace, 'x' : evoke_whitespace_name_whitespace,
            'y' : evoke_whitespace_name_whitespace, 'z' : evoke_whitespace_name_whitespace,
        }.__getitem__


    share(
        'conjure_all_index',                                conjure_all_index,
        'conjure__right_parenthesis__colon__line_marker',   conjure__right_parenthesis__colon__line_marker,
        'evoke_all_index',                                  evoke_all_index,
        'evoke__right_parenthesis__colon__line_marker',     evoke__right_parenthesis__colon__line_marker,
        'find_evoke_whitespace_atom_whitespace',            find_evoke_whitespace_atom_whitespace,
    )
