#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Tokenize1Operator')
def gem():
    show = 0


    @share
    def skip_tokenize_prefix():
        parse_context.iterate_lines.next()

        m = next_nested_line_match(qs())

        if m is none:
            raise_unknown_line(1)

        if m.group('comment_newline') is not none:
            raise_unknown_line(2)

        wj(m.end())


    @share
    def tokenize_operator():
        s = qs()
        m = operator_match(s, qj())

        if m is none:
            #my_line(portray_string(s[qj() : ]))
            raise_unknown_line(1)

        operator_s = m.group('operator')

        if operator_s is not none:
            conjure = find_operator_conjure_function(operator_s)

            if m.end('comment_newline') is -1:
                if conjure is conjure_right_parenthesis:
                    d = qd()

                    if d is 0:
                        raise_unknown_line(2)

                    wd(d - 1)

                j = m.end()
                r = conjure(s[qi() : j])

                wi(j)
                wj(j)

                return r

            d = qd()

            if d is 0:
                if conjure is conjure_colon:
                    return conjure_colon_newline(s[qi() : ])

                operator_end = m.end('operator')
                wn(conjure_token_newline(s[operator_end : ]))

                return conjure(s[qi():operator_end])

            if conjure is conjure_right_parenthesis:
                if d is 1:
                    i = m.end('operator')

                    wd0()
                    wn(conjure_token_newline(s[i : ]))

                    return conjure_right_parenthesis(s[qi() : i])

                wd(d - 1)

            r = conjure(s[qi() : ])

            skip_tokenize_prefix()

            return r

        left_parenthesis__ow__end = m.end('left_parenthesis__ow')
        right_parenthesis         = m.group('right_parenthesis')

        if right_parenthesis is not none:
            left_parenthesis = conjure_left_parenthesis(s[qi() : left_parenthesis__ow__end])

            if m.end('comment_newline') is -1:
                right_parenthesis = conjure_right_parenthesis(right_parenthesis)

                wi(m.end('right_parenthesis'))
                wj(m.end())
            else:
                if qd() is 0:
                    right_parenthesis = conjure_right_parenthesis(right_parenthesis)

                    wn(conjure_token_newline(s[m.end('right_parenthesis') : ]))
                else:
                    right_parenthesis = conjure_right_parenthesis(s[left_parenthesis__ow__end : ])

                    skip_tokenize_prefix()

            return Arguments_0(left_parenthesis, right_parenthesis)

        if m.end('comment_newline') is -1:
            left_parenthesis = conjure_left_parenthesis(s[qi() : left_parenthesis__ow__end])

            j = m.end()

            wd(qd() + 1)
            wi(j)
            wj(j)

            return left_parenthesis

        left_parenthesis = conjure_left_parenthesis(s[qi() : ])

        skip_tokenize_prefix()

        wd(qd() + 1)

        if show is 7:
            my_line('%r; %s', left_parenthesis, portray_string(s[qj() : ]))

        return left_parenthesis
