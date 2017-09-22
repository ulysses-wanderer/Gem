#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Parse1Expression')
def gem():
    show = 0


    #
    #   1.  Postfix-Expression (Python 2.7.14rc1 grammer calls this 'trailer')
    #
    #       postfix-expression
    #           : atom
    #           | dot-expression
    #           | call-expression
    #           | method-call-expression
    #           | index-expression
    #
    #       dot-expression
    #           : postfix-expression '.' name
    #
    #       call-expression
    #           : postfix-expression '(' ] ')'
    #           : postfix-expression '(' argument-list ')'
    #
    #       method-call-expression
    #           : postfix-expression '.' name '(' ')'
    #           | postfix-expression '.' name '(' argument-list ')'
    #
    #       index-expression
    #           : postfix-expression '[' ']'
    #           | postfix-expression '[' subscript-list ']'
    #
    #       subscript-list
    #           : subscript
    #           | subscript-list ',' subscript
    #
    #       subscript
    #           : '.' '.' '.'
    #           | ternary-expression
    #           | ternary-expression ':'
    #           | ':' ternary-expression
    #           | [ternary-expression] ':' [ternary-expression] ':' [ternary-expression]
    #
    @share
    def parse1_postfix_expression__left_operator(left, operator, indented = 0):
        assert operator.is_postfix_operator

        while 7 is 7:
            assert qk() is none

            if operator.is_dot:
                name = tokenize_name()

                if qn() is not none:
                    return conjure_member_expression(left, conjure_dot_name(operator, name))

                operator_2 = tokenize_operator()

                if operator_2.is_dot:
                    if qn() is not none:
                        raise_unknown_line()

                    name_2 = tokenize_name()

                    if qn() is not none:
                        return conjure_member_expression(
                                   left,
                                   conjure_dot_name_pair(
                                       conjure_dot_name(operator,   name),
                                       conjure_dot_name(operator_2, name_2),
                                   ),
                               )

                    operator_3 = tokenize_operator()

                    if operator_3.is_dot:
                        if qn() is not none:
                            raise_unknown_line()

                        name_3 = tokenize_name()

                        if qn() is not none:
                            return conjure_member_expression(
                                       left,
                                       conjure_dot_name_triplet(
                                           conjure_dot_name(operator,   name),
                                           conjure_dot_name(operator_2, name_2),
                                           conjure_dot_name(operator_3, name_3),
                                       ),
                                   )

                        operator_4 = tokenize_operator()

                        if operator_4.is_dot:
                            if qn() is not none:
                                raise_unknown_line()

                            name_4 = tokenize_name()

                            left = conjure_member_expression(
                                       left,
                                       conjure_dot_name_quadruplet(
                                           conjure_dot_name(operator,   name),
                                           conjure_dot_name(operator_2, name_2),
                                           conjure_dot_name(operator_3, name_3),
                                           conjure_dot_name(operator_4, name_4),
                                       ),
                                   )

                            if qn() is not none:
                                return left

                            operator_5 = tokenize_operator()

                            if not operator_5.is_postfix_operator:
                                wk(operator_5)

                                return left

                            operator = operator_5
                        else:
                            left = conjure_member_expression(
                                       left,
                                       conjure_dot_name_triplet(
                                           conjure_dot_name(operator,   name),
                                           conjure_dot_name(operator_2, name_2),
                                           conjure_dot_name(operator_3, name_3),
                                       ),
                                   )

                            if not operator_4.is_postfix_operator:
                                wk(operator_4)

                                return left

                            operator = operator_4

                    else:
                        left = conjure_member_expression(
                                   left,
                                   conjure_dot_name_pair(
                                       conjure_dot_name(operator,   name),
                                       conjure_dot_name(operator_2, name_2),
                                   ),
                               )

                        if not operator_3.is_postfix_operator:
                            wk(operator_3)

                            return left

                        operator = operator_3

                else:
                    left = conjure_member_expression(left, conjure_dot_name(operator, name))

                    if not operator_2.is_postfix_operator:
                        wk(operator_2)

                        return left

                    operator = operator_2

            if operator.is__arguments_0__or__left_parenthesis:
                if operator.is_left_parenthesis:
                    assert qd() > 0
                    assert qn() is none

                    operator = parse1_arguments__left_parenthesis(operator)

                newline = qn()

                if (indented is not 0) and (newline is not none) and (qk() is none):
                    wn(none)

                    return left.call_statement(indented, left, operator, newline)

                left = left.call_expression(left, operator)

                operator = qk()

                if operator is not none:
                    if not operator.is_postfix_operator:
                        return left

                    wk(none)
                else:
                    if newline is not none:
                        return left

                    operator = tokenize_operator()

                    if not operator.is_postfix_operator:
                        wk(operator)

                        return left

            if operator.is_left_square_bracket:
                if qn() is not none:
                    raise_unknown_line()

                middle = parse1_atom()

                if middle.is_colon:
                    operator = conjure__left_square_bracket__colon(operator, middle)
                else:
                    operator_2 = qk()

                    if operator_2 is none:
                        if qn() is not none:
                            raise_unknown_line()

                        operator_2 = tokenize_operator()
                    else:
                        wk(none)

                    if not operator_2.is_end_of_ternary_expression:
                        middle = parse1_ternary_expression__X__any_expression(middle, operator_2)

                        operator_2 = qk()

                        if operator_2 is none:
                            raise_unknown_line()

                        wk(none)

                    if operator_2.is_right_square_bracket:
                        left = IndexExpression(left, NormalIndex(operator, middle, operator_2))
                    elif operator_2.is_colon:
                        if qn() is not none:
                            raise_unknown_line()

                        middle_2 = parse1_atom()

                        if middle_2.is_right_square_bracket:
                            left = IndexExpression(
                                       left,
                                       HeadIndex(
                                           operator,
                                           middle,
                                           conjure__colon__right_square_bracket(operator_2, middle_2),
                                       ),
                                   )
                        else:
                            operator_3 = qk()

                            if operator_3 is none:
                                if qn() is not none:
                                    raise_unknown_line()

                                operator_3 = tokenize_operator()
                            else:
                                wk(none)

                            if not operator_3.is_end_of_ternary_expression:
                                middle_2 = parse1_ternary_expression__X__any_expression(middle_2, operator_3)

                                operator_3 = qk()

                                if operator_3 is none:
                                    raise_unknown_line()

                                wk(none)

                            if not operator_3.is_right_square_bracket:
                                raise_unknown_line()

                            left = IndexExpression(
                                       left,
                                       RangeIndex(operator, middle, operator_2, middle_2, operator_3),
                                   )
                    elif operator_2.is_colon__right_square_bracket:
                        left = IndexExpression(left, HeadIndex(operator, middle, operator_2))
                    else:
                        my_line('operator_2: %r', operator_2)
                        raise_unknown_line()

                    if qn() is not none:
                        return left

                    operator = qk()

                    if operator is not none:
                        if not operator.is_postfix_operator:
                            return left

                        wk(none)
                    else:
                        if qn() is not none:
                            return left

                        operator = tokenize_operator()

                        if not operator.is_postfix_operator:
                            wk(operator)

                            return left

            if operator.is_tail_index:
                middle_2 = parse1_atom()

                if middle_2.is_right_square_bracket:
                    operator = conjure_all_index(operator.a, operator.b, middle_2)
                else:
                    operator_2 = qk()

                    if operator_2 is none:
                        if qn() is not none:
                            raise_unknown_line()

                        operator_2 = tokenize_operator()
                    else:
                        wk(none)

                    if not operator_2.is_right_square_bracket:
                        raise_unknown_line()

                    left = IndexExpression(left, TailIndex(operator, middle_2, operator_2))

                    if qn() is not none:
                        return left

                    operator = qk()

                    if operator is not none:
                        if not operator.is_postfix_operator:
                            return left

                        wk(none)
                    else:
                        if qn() is not none:
                            return left

                        operator = tokenize_operator()

                        if not operator.is_postfix_operator:
                            wk(operator)

                            return left

            if operator.is_all_index:
                left = IndexExpression(left, operator)

                if qn() is not none:
                    return left

                operator = qk()

                if operator is not none:
                    if not operator.is_postfix_operator:
                        return left

                    wk(none)
                else:
                    if qn() is not none:
                        return left

                    operator = tokenize_operator()

                    if not operator.is_postfix_operator:
                        wk(operator)

                        return left

            assert operator.is_postfix_operator

        raise_unknown_line()


    #
    #   2.  Power-Expression (Python 2.7.14rc1 grammer calls this 'power')
    #
    #       power-expression
    #           :   postfix-expression
    #           |   postfix-expression '**' unary-expression
    #
    def parse1_power_expression__left_operator(left, power_operator):
        return PowerExpression(left, power_operator, parse1_unary_expression())


    #
    #   3.  Unary-Expression (Python 2.7.14rc1 grammer calls this 'factor')
    #
    @share
    def parse1_twos_complement_expression__operator(operator):
        return TwosComplementExpression(operator, parse1_unary_expression())


    @share
    def parse1_negative_expression__operator(operator):
        return NegativeExpression(operator, parse1_unary_expression())


    def parse1_unary_expression():
        left = parse1_atom()

        operator = qk()

        if operator is none:
            newline = qn()

            if qn() is not none:
                return left

            operator = tokenize_operator()

            if qk() is not none:
                raise_unknown_line()

            if operator.is_end_of_unary_expression:
                wk(operator)
                return left
        else:
            if operator.is_end_of_unary_expression:
                return left

            wk(none)

        if operator.is_postfix_operator:
            left = parse1_postfix_expression__left_operator(left, operator)

            operator = qk()

            if operator is none:
                if qn() is none:
                    raise_unknown_line()

                return left

            if operator.is_end_of_unary_expression:
                return left

            wk(none)

        if operator.is_power_operator:
            left = parse1_power_expression__left_operator(left, operator)

            operator = qk()

            if operator is none:
                if qn() is none:
                    raise_unknown_line()

                return left

            if operator.is_end_of_unary_expression:
                return left

            wk(none)

        if operator.is_power_operator:
            left = parse1_power_expression__left_operator(left, operator)

            operator = qk()

            if operator is none:
                if qn() is none:
                    raise_unknown_line()

                return left

            if operator.is_end_of_unary_expression:
                return left

            wk(none)

        raise_unknown_line()


    #
    #   4.  Multiply-Expression (Python 2.7.14rc1 grammer calls this 'term')
    #
    def parse1_multiply_expression__left_operator(left, multiply_operator):
        right = parse1_unary_expression()

        operator = qk()

        if operator is none:
            if qn() is not none:
                return multiply_operator.expression_meta(left, multiply_operator, right)

            operator = tokenize_operator()

            if operator.is_end_of_multiply_expression:
                wk(operator)

                return multiply_operator.expression_meta(left, multiply_operator, right)
        else:
            if operator.is_end_of_multiply_expression:
                return multiply_operator.expression_meta(left, multiply_operator, right)

            wk(none)

        if not operator.is_multiply_operator:
            raise_unknown_line()

        many = [left, multiply_operator, right, operator]

        while 7 is 7:
            many.append(parse1_unary_expression())

            operator = qk()

            if operator is none:
                if qn() is not none:
                    return MultiplyExpression_Many(Tuple(many))

                operator = tokenize_operator()

                if operator.is_end_of_multiply_expression:
                    wk(operator)

                    return MultiplyExpression_Many(Tuple(many))
            else:
                if operator.is_end_of_multiply_expression:
                    return MultiplyExpression_Many(Tuple(many))

                wk(none)

            if not operator.is_multiply_operator:
                raise_unknown_line()

            many.append(operator)


    def parse1_multiply_expression():
        left = parse1_atom()

        operator = qk()

        if operator is not none:
            if operator.is_end_of_multiply_expression:
                return left

            wk(none)
        else:
            if qn() is not none:
                return left

            operator = tokenize_operator()

            if operator.is_end_of_multiply_expression:
                wk(operator)

                return left

        if operator.is_postfix_operator:
            left = parse1_postfix_expression__left_operator(left, operator)

            operator = qk()

            if operator is none:
                if qn() is none:
                    raise_unknown_line()

                return left

            if operator.is_end_of_multiply_expression:
                return left

            wk(none)

        if operator.is_power_operator:
            left = parse1_power_expression__left_operator(left, operator)

            operator = qk()

            if operator is none:
                if qn() is none:
                    raise_unknown_line()

                return left

            if operator.is_end_of_multiply_expression:
                return left

            wk(none)

        if operator.is_multiply_operator:
            return parse1_multiply_expression__left_operator(left, operator)

        #my_line('left: %r; operator: %r; s: %s', left, operator, portray_string(qs()[qj():]))
        raise_unknown_line()



    #
    #   5.  Arithmetic-Expression (Python 2.7.14rc1 grammer calls this 'arith_expr')
    #
    def parse1_arithmetic_expression__left_operator(left, add_operator):
        assert add_operator.is_arithmetic_operator

        right = parse1_multiply_expression()

        operator = qk()

        if operator is none:
            if qn() is not none:
                return add_operator.expression_meta(left, add_operator, right)

            operator = tokenize_operator()

            if operator.is_end_of_arithmetic_expression:
                wk(operator)

                return add_operator.expression_meta(left, add_operator, right)
        else:
            if operator.is_end_of_arithmetic_expression:
                return add_operator.expression_meta(left, add_operator, right)

            wk(none)

        if not operator.is_arithmetic_operator:
            raise_unknown_line()

        many = [left, add_operator, right, operator]

        while 7 is 7:
            many.append(parse1_multiply_expression())

            operator = qk()

            if operator is none:
                if qn() is not none:
                    return ArithmeticExpression_Many(Tuple(many))

                operator = tokenize_operator()

                if operator.is_end_of_arithmetic_expression:
                    wk(operator)

                    return ArithmeticExpression_Many(Tuple(many))
            else:
                if operator.is_end_of_arithmetic_expression:
                    return ArithmeticExpression_Many(Tuple(many))

                wk(none)

            if not operator.is_arithmetic_operator:
                raise_unknown_line()

            many.append(operator)


    def parse1_arithmetic_expression():
        left = parse1_atom()

        operator = qk()

        if operator is not none:
            if operator.is_end_of_arithmetic_expression:
                return left

            wk(none)
        else:
            if qn() is not none:
                return left

            operator = tokenize_operator()

            if operator.is_end_of_arithmetic_expression:
                wk(operator)

                return left

        if operator.is_postfix_operator:
            left = parse1_postfix_expression__left_operator(left, operator)

            operator = qk()

            if operator is none:
                if qn() is none:
                    raise_unknown_line()

                return left

            if operator.is_end_of_arithmetic_expression:
                return left

            wk(none)

        if operator.is_power_operator:
            left = parse1_power_expression__left_operator(left, operator)

            operator = qk()

            if operator is none:
                if qn() is none:
                    raise_unknown_line()

                return left

            if operator.is_end_of_arithmetic_expression:
                return left

            wk(none)

        if operator.is_multiply_operator:
            left = parse1_multiply_expression__left_operator(left, operator)

            operator = qk()

            if operator is none:
                if qn() is none:
                    raise_unknown_line()

                return left

            if operator.is_end_of_arithmetic_expression:
                return left

            wk(none)

        if operator.is_arithmetic_operator:
            return parse1_arithmetic_expression__left_operator(left, operator)

        #my_line('left: %r; operator: %r; s: %s', left, operator, portray_string(qs()[qj():]))
        raise_unknown_line()


    #
    #   6.  Shift-Expression (Python 2.7.14rc1 grammer calls this 'shift_expr')
    #

    #
    #   7.  Logical-And-Expression (Python 2.7.14rc1 grammer calls this 'and_expr')
    #
    def parse1_logical_and_expression__left_operator(left, logical_and_operator):
        assert logical_and_operator.is_logical_and_operator

        right = parse1_arithmetic_expression()

        operator = qk()

        if operator is none:
            if qn() is not none:
                return LogicalAndExpression_1(left, logical_and_operator, right)

            operator = tokenize_operator()

            if operator.is_end_of_logical_and_expression:
                wk(operator)

                return LogicalAndExpression_1(left, logical_and_operator, right)
        else:
            if operator.is_end_of_logical_and_expression:
                return LogicalAndExpression_1(left, logical_and_operator, right)

            wk(none)

        if not operator.is_logical_and_operator:
            raise_unknown_line()

        many = [left, logical_and_operator, right, operator]

        while 7 is 7:
            many.append(parse1_arithmetic_expression())

            operator = qk()

            if operator is none:
                if qn() is not none:
                    return LogicalAndExpression_Many(Tuple(many))

                operator = tokenize_operator()

                if operator.is_end_of_logical_and_expression:
                    wk(operator)

                    return LogicalAndExpression_Many(Tuple(many))
            else:
                if operator.is_end_of_logical_and_expression:
                    return LogicalAndExpression_Many(Tuple(many))

                wk(none)

            if not operator.is_logical_and_operator:
                raise_unknown_line()

            many.append(operator)


    @share
    def parse1_logical_and_expression():
        left = parse1_atom()

        operator = qk()

        if operator is not none:
            if operator.is_end_of_logical_and_expression:
                return left

            wk(none)
        else:
            if qn() is not none:
                return left

            operator = tokenize_operator()

            if operator.is_end_of_logical_and_expression:
                wk(operator)

                return left

        if operator.is_postfix_operator:
            left = parse1_postfix_expression__left_operator(left, operator)

            operator = qk()

            if operator is none:
                if qn() is none:
                    raise_unknown_line()

                return left

            if operator.is_end_of_logical_and_expression:
                return left

            wk(none)

        if operator.is_power_operator:
            left = parse1_power_expression__left_operator(left, operator)

            operator = qk()

            if operator is none:
                if qn() is none:
                    raise_unknown_line()

                return left

            if operator.is_end_of_logical_and_expression:
                return left

            wk(none)

        if operator.is_multiply_operator:
            left = parse1_multiply_expression__left_operator(left, operator)

            operator = qk()

            if operator is none:
                if qn() is none:
                    raise_unknown_line()

                return left

            if operator.is_end_of_logical_and_expression:
                return left

            wk(none)

        if operator.is_arithmetic_operator:
            left = parse1_arithmetic_expression__left_operator(left, operator)

            operator = qk()

            if operator is none:
                if qn() is none:
                    raise_unknown_line()

                return left

            if operator.is_end_of_logical_and_expression:
                return left

            wk(none)

        if operator.is_logical_and_operator:
            return parse1_logical_and_expression__left_operator(left, operator)

        #my_line('left: %r; operator: %r; s: %s', left, operator, portray_string(qs()[qj():]))
        raise_unknown_line()



    #
    #   8.  Logical-Exclusive-Or-Expression (Python 2.7.14rc1 grammer calls this 'xor_expr')
    #

    #
    #   9.  Normal-Expression (Logical-Or) (Python 2.7.14rc1 grammer calls this 'expr')
    #
    def parse1_normal_expression__left_operator(left, logical_or_operator):
        assert logical_or_operator.is_logical_or_operator

        right = parse1_logical_and_expression()

        operator = qk()

        if operator is none:
            if qn() is not none:
                return LogicalOrExpression_1(left, logical_or_operator, right)

            operator = tokenize_operator()

            if operator.is_end_of_logical_or_expression:
                wk(operator)

                return LogicalOrExpression_1(left, logical_or_operator, right)
        else:
            if operator.is_end_of_logical_or_expression:
                return LogicalOrExpression_1(left, logical_or_operator, right)

            wk(none)

        if not operator.is_logical_or_operator:
            raise_unknown_line()

        many = [left, logical_or_operator, right, operator]

        while 7 is 7:
            many.append(parse1_logical_and_expression())

            operator = qk()

            if operator is none:
                if qn() is not none:
                    return LogicalOrExpression_Many(Tuple(many))

                operator = tokenize_operator()

                if operator.is_end_of_logical_or_expression:
                    wk(operator)

                    return LogicalOrExpression_Many(Tuple(many))
            else:
                if operator.is_end_of_logical_or_expression:
                    return LogicalOrExpression_Many(Tuple(many))

                wk(none)

            if not operator.is_logical_or_operator:
                raise_unknown_line()

            many.append(operator)


    @share
    def parse1_normal_expression():
        left = parse1_atom()

        operator = qk()

        if operator is not none:
            if operator.is_end_of_logical_or_expression:
                return left

            wk(none)
        else:
            if qn() is not none:
                return left

            operator = tokenize_operator()

            if operator.is_end_of_logical_or_expression:
                wk(operator)

                return left

        if operator.is_postfix_operator:
            left = parse1_postfix_expression__left_operator(left, operator)

            operator = qk()

            if operator is none:
                if qn() is none:
                    raise_unknown_line()

                return left

            if operator.is_end_of_logical_or_expression:
                return left

            wk(none)

        if operator.is_power_operator:
            left = parse1_power_expression__left_operator(left, operator)

            operator = qk()

            if operator is none:
                if qn() is none:
                    raise_unknown_line()

                return left

            if operator.is_end_of_logical_or_expression:
                return left

            wk(none)

        if operator.is_multiply_operator:
            left = parse1_multiply_expression__left_operator(left, operator)

            operator = qk()

            if operator is none:
                if qn() is none:
                    raise_unknown_line()

                return left

            if operator.is_end_of_logical_or_expression:
                return left

            wk(none)

        if operator.is_arithmetic_operator:
            left = parse1_arithmetic_expression__left_operator(left, operator)

            operator = qk()

            if operator is none:
                if qn() is none:
                    raise_unknown_line()

                return left

            if operator.is_end_of_logical_or_expression:
                return left

            wk(none)

        if operator.is_logical_and_operator:
            left = parse1_logical_and_expression__left_operator(left, operator)

            operator = qk()

            if operator is none:
                if qn() is none:
                    raise_unknown_line()

                return left

            if operator.is_end_of_logical_or_expression:
                return left

            wk(none)

        if operator.is_logical_or_operator:
            return parse1_normal_expression__left_operator(left, operator)

        #my_line('left: %r; operator: %r; s: %s', left, operator, portray_string(qs()[qj():]))
        raise_unknown_line()


    #
    #   10. Normal-Expression-List (Python 2.7.14rc1 grammer calls this 'exprlist')
    #
    @share
    def parse1_normal_expression_list():
        return parse1_arithmetic_expression()       #   Temporary until , is implemented


    #
    #   11.  Compare-Expression (Python 2.7.14rc1 grammer calls this 'comparasion')
    #
    @share
    def parse1_compare_expression__left_operator(left, compare_operator):
        assert compare_operator.is_compare_operator

        if compare_operator.is_keyword_not:
            #my_line('full: %s', portray_string(qs()))
            raise_unknown_line()

        right = parse1_normal_expression()

        operator = qk()

        if operator is none:
            if qn() is not none:
                return compare_operator.expression_meta(left, compare_operator, right)

            operator = tokenize_operator()

            if operator.is_end_of_compare_expression:
                wk(operator)

                return compare_operator.expression_meta(left, compare_operator, right)
        else:
            if operator.is_end_of_compare_expression:
                return compare_operator.expression_meta(left, compare_operator, right)

            wk(none)

        many = [left, compare_operator, right, operator]

        while 7 is 7:
            many.append(parse1_normal_expression())

            operator = qk()

            if operator is none:
                if qn() is not none:
                    return CompareExpression_Many(Tuple(many))

                operator = tokenize_operator()

                if operator.is_end_of_compare_expression:
                    wk(operator)

                    return CompareExpression_Many(Tuple(many))
            else:
                if operator.is_end_of_compare_expression:
                    return CompareExpression_Many(Tuple(many))

                wk(none)

            many.append(operator)


    def parse1_compare_expression():
        assert qk() is none

        left = parse1_atom()

        operator = qk()

        if operator is not none:
            if operator.is_end_of_compare_expression:
                return left

            wk(none)
        else:
            if qn() is not none:
                return left

            operator = tokenize_operator()

            if operator.is_end_of_compare_expression:
                wk(operator)

                return left

        if operator.is_postfix_operator:
            left = parse1_postfix_expression__left_operator(left, operator)

            operator = qk()

            if operator is none:
                if qn() is none:
                    raise_unknown_line()

                return left

            if operator.is_end_of_compare_expression:
                return left

            wk(none)

        if operator.is_power_operator:
            left = parse1_power_expression__left_operator(left, operator)

            operator = qk()

            if operator is none:
                if qn() is none:
                    raise_unknown_line()

                return left

            if operator.is_end_of_compare_expression:
                return left

            wk(none)

        if operator.is_multiply_operator:
            left = parse1_multiply_expression__left_operator(left, operator)

            operator = qk()

            if operator is none:
                if qn() is none:
                    raise_unknown_line()

                return left

            if operator.is_end_of_compare_expression:
                return left

            wk(none)

        if operator.is_arithmetic_operator:
            left = parse1_arithmetic_expression__left_operator(left, operator)

            operator = qk()

            if operator is none:
                if qn() is none:
                    raise_unknown_line()

                return left

            if operator.is_end_of_compare_expression:
                return left

            wk(none)

        if operator.is_logical_and_operator:
            left = parse1_logical_and_expression__left_operator(left, operator)

            operator = qk()

            if operator is none:
                if qn() is none:
                    raise_unknown_line()

                return left

            if operator.is_end_of_compare_expression:
                return left

            wk(none)

        if operator.is_logical_or_operator:
            left = parse1_normal_expression__left_operator(left, operator)

            operator = qk()

            if operator is none:
                if qn() is none:
                    raise_unknown_line()

                return left

            if operator.is_end_of_compare_expression:
                return left

            wk(none)

        if operator.is_compare_operator:
            return parse1_compare_expression__left_operator(left, operator)

        #my_line('left: %r; operator: %r; s: %s', left, operator, portray_string(qs()[qj():]))
        raise_unknown_line()



    #
    #   12.  Not-Expression (Python 2.7.14rc1 grammer calls this 'not_test')
    #
    #       not-expression
    #           : compare-expression
    #           | 'not' not-test
    #
    #   NOTE [FIX IN FUTURE -- When really parsing not expressions properly]:
    #       Uses .is_end_of_compare_expression on purpose (there is no .is_end_of_not_expression, as it would be
    #       identicial to .is_end_of_compare_expression)
    #
    @share
    def parse1_not_expression__operator(not_operator):
        assert not_operator.is_keyword_not

        return NotExpression(not_operator, parse1_compare_expression()) #   Temporary until handle 'not' atom itself


    #
    #   13. Boolean-And-Expression (Python 2.7.14rc1 grammer calls this 'and_test')
    #
    def parse1_boolean_and_expression__left_operator(left, operator):
        assert operator.is_keyword_and

        right = parse1_compare_expression()

        operator_2 = qk()

        if operator_2 is none:
            if qn() is not none:
                return AndExpression_1(left, operator, right)

            operator_2 = tokenize_operator()

            if operator_2.is_end_of_boolean_and_expression:
                wk(operator_2)

                return AndExpression_1(left, operator, right)
        else:
            if operator_2.is_end_of_boolean_and_expression:
                return AndExpression_1(left, operator, right)

            wk(none)

        many = [left, operator, right, operator_2]

        while 7 is 7:
            many.append(parse1_compare_expression())

            operator_7 = qk()

            if operator_7 is none:
                if qn() is not none:
                    return AndExpression_Many(Tuple(many))

                operator_7 = tokenize_operator()

                if operator_7.is_end_of_boolean_and_expression:
                    wk(operator_7)

                    return AndExpression_Many(Tuple(many))
            else:
                if operator_7.is_end_of_boolean_and_expression:
                    return AndExpression_Many(Tuple(many))

                wk(none)

            if not operator_7.is_keyword_and:
                raise_unknown_line()

            many.append(operator_7)


    def parse1_boolean_and_expression():
        left = parse1_atom()

        operator = qk()

        if operator is not none:
            if operator.is_end_of_boolean_and_expression:
                return left

            wk(none)
        else:
            if qn() is not none:
                return left

            operator = tokenize_operator()

            if operator.is_end_of_boolean_and_expression:
                wk(operator)

                return left

        if operator.is_postfix_operator:
            left = parse1_postfix_expression__left_operator(left, operator)

            operator = qk()

            if operator is none:
                if qn() is none:
                    raise_unknown_line()

                return left

            if operator.is_end_of_boolean_and_expression:
                return left

            wk(none)

        if operator.is_power_operator:
            left = parse1_power_expression__left_operator(left, operator)

            operator = qk()

            if operator is none:
                if qn() is none:
                    raise_unknown_line()

                return left

            if operator.is_end_of_boolean_and_expression:
                return left

            wk(none)

        if operator.is_multiply_operator:
            left = parse1_multiply_expression__left_operator(left, operator)

            operator = qk()

            if operator is none:
                if qn() is none:
                    raise_unknown_line()

                return left

            if operator.is_end_of_boolean_and_expression:
                return left

            wk(none)

        if operator.is_arithmetic_operator:
            left = parse1_arithmetic_expression__left_operator(left, operator)

            operator = qk()

            if operator is none:
                if qn() is none:
                    raise_unknown_line()

                return left

            if operator.is_end_of_boolean_and_expression:
                return left

            wk(none)

        if operator.is_logical_and_operator:
            left = parse1_logical_and_expression__left_operator(left, operator)

            operator = qk()

            if operator is none:
                if qn() is none:
                    raise_unknown_line()

                return left

            if operator.is_end_of_boolean_and_expression:
                return left

            wk(none)

        if operator.is_logical_or_operator:
            left = parse1_normal_expression__left_operator(left, operator)

            operator = qk()

            if operator is none:
                if qn() is none:
                    raise_unknown_line()

                return left

            if operator.is_end_of_boolean_and_expression:
                return left

            wk(none)

        if operator.is_compare_operator:
            left = parse1_compare_expression__left_operator(left, operator)

            operator = qk()

            if operator is none:
                if qn() is none:
                    raise_unknown_line()

                return left

            if operator.is_end_of_boolean_and_expression:
                return left

            wk(none)

        if operator.is_keyword_and:
            return parse1_boolean_and_expression__left_operator(left, operator)

        #my_line('left: %r; operator: %r; s: %s', left, operator, portray_string(qs()[qj():]))
        raise_unknown_line()



    #
    #   14. Boolean-Or-Expression (Python 2.7.14rc1 grammer calls this 'or_test')
    #
    def parse1_boolean_or_expression__left_operator(left, operator):
        assert operator.is_keyword_or

        right = parse1_boolean_and_expression()

        operator_2 = qk()

        if operator_2 is none:
            if qn() is not none:
                return OrExpression_1(left, operator, right)

            operator_2 = tokenize_operator()

            if operator_2.is_end_of_boolean_or_expression:
                wk(operator_2)

                return OrExpression_1(left, operator, right)
        else:
            if operator_2.is_end_of_boolean_or_expression:
                return OrExpression_1(left, operator, right)

            wk(none)

        many = [left, operator, right, operator_2]

        while 7 is 7:
            many.append(parse1_boolean_and_expression())

            operator_7 = qk()

            if operator_7 is none:
                if qn() is not none:
                    return OrExpression_Many(Tuple(many))

                operator_7 = tokenize_operator()

                if operator_7.is_end_of_boolean_or_expression:
                    wk(operator_7)

                    return OrExpression_Many(Tuple(many))
            else:
                if operator_7.is_end_of_boolean_or_expression:
                    return OrExpression_Many(Tuple(many))

                wk(none)

            if not operator_7.is_keyword_or:
                raise_unknown_line()

            many.append(operator_7)


    def parse1_boolean_or_expression():
        left = parse1_atom()

        operator = qk()

        if operator is not none:
            if operator.is_end_of_boolean_or_expression:
                return left

            wk(none)
        else:
            if qn() is not none:
                return left

            operator = tokenize_operator()

            if operator.is_end_of_boolean_or_expression:
                wk(operator)

                return left

        if operator.is_postfix_operator:
            left = parse1_postfix_expression__left_operator(left, operator)

            operator = qk()

            if operator is none:
                if qn() is none:
                    raise_unknown_line()

                return left

            if operator.is_end_of_boolean_or_expression:
                return left

            wk(none)

        if operator.is_power_operator:
            left = parse1_power_expression__left_operator(left, operator)

            operator = qk()

            if operator is none:
                if qn() is none:
                    raise_unknown_line()

                return left

            if operator.is_end_of_boolean_or_expression:
                return left

            wk(none)

        if operator.is_multiply_operator:
            left = parse1_multiply_expression__left_operator(left, operator)

            operator = qk()

            if operator is none:
                if qn() is none:
                    raise_unknown_line()

                return left

            if operator.is_end_of_boolean_or_expression:
                return left

            wk(none)

        if operator.is_arithmetic_operator:
            left = parse1_arithmetic_expression__left_operator(left, operator)

            operator = qk()

            if operator is none:
                if qn() is none:
                    raise_unknown_line()

                return left

            if operator.is_end_of_boolean_or_expression:
                return left

            wk(none)

        if operator.is_compare_operator:
            left = parse1_compare_expression__left_operator(left, operator)

            operator = qk()

            if operator is none:
                if qn() is none:
                    raise_unknown_line()

                return left

            if operator.is_end_of_boolean_or_expression:
                return left

            wk(none)

        if operator.is_logical_and_operator:
            left = parse1_logical_and_expression__left_operator(left, operator)

            operator = qk()

            if operator is none:
                if qn() is none:
                    raise_unknown_line()

                return left

            if operator.is_end_of_boolean_and_expression:
                return left

            wk(none)

        if operator.is_logical_or_operator:
            left = parse1_normal_expression__left_operator(left, operator)

            operator = qk()

            if operator is none:
                if qn() is none:
                    raise_unknown_line()

                return left

            if operator.is_end_of_boolean_or_expression:
                return left

            wk(none)

        if operator.is_keyword_and:
            left = parse1_boolean_and_expression__left_operator(left, operator)

            operator = qk()

            if operator is none:
                if qn() is none:
                    raise_unknown_line()

                return left

            if operator.is_end_of_boolean_or_expression:
                return left

            wk(none)

        if operator.is_keyword_or:
            return parse1_boolean_or_expression__left_operator(left, operator)

        #my_line('left: %r; operator: %r; s: %s', left, operator, portray_string(qs()[qj():]))
        raise_unknown_line()



    #
    #   15.  Ternary-Expression (Python 2.7.14rc1 grammer calls this 'test')
    #
    #           ternary-expression
    #               : boolean-or-expression
    #               | boolean-or-expression 'if' boolean-or-expression 'else' ternary-expression
    #               | lambda-expression
    #
    #           lambda-Expression
    #               : 'lambda' [variable-argument-list] ':' ternary-expression
    #
    def parse1_ternary_expression__left_operator(left, operator):
        assert operator.is_keyword_if

        middle = parse1_boolean_or_expression()

        operator_2 = qk()

        wk(none)

        if not operator_2.is_keyword_else:
            #my_line('left: %r; operator: %r; middle: %r; operator_2: %r; s: %s',
            #        left, operator, middle, operator_2, portray_string(qs()[qj():]))

            raise_unknown_line()

        return TernaryExpression(left, operator, middle, operator_2, parse1_ternary_expression())


    @share
    def parse1_ternary_expression__X__any_expression(left, operator):
        if operator.is_postfix_operator:
            left = parse1_postfix_expression__left_operator(left, operator)

            operator = qk()

            if operator is none:
                if qn() is none:
                    raise_unknown_line()

                return left

            if operator.is_end_of_ternary_expression:
                return left

            wk(none)

        if operator.is_power_operator:
            left = parse1_power_expression__left_operator(left, operator)

            operator = qk()

            if operator is none:
                if qn() is none:
                    raise_unknown_line()

                return left

            if operator.is_end_of_ternary_expression:
                return left

            wk(none)

        if operator.is_multiply_operator:
            left = parse1_multiply_expression__left_operator(left, operator)

            operator = qk()

            if operator is none:
                if qn() is none:
                    raise_unknown_line()

                return left

            if operator.is_end_of_ternary_expression:
                return left

            wk(none)

        if operator.is_arithmetic_operator:
            left = parse1_arithmetic_expression__left_operator(left, operator)

            operator = qk()

            if operator is none:
                if qn() is none:
                    raise_unknown_line()

                return left

            if operator.is_end_of_ternary_expression:
                return left

            wk(none)

        if operator.is_compare_operator:
            left = parse1_compare_expression__left_operator(left, operator)

            operator = qk()

            if operator is none:
                if qn() is none:
                    raise_unknown_line()

                return left

            if operator.is_end_of_ternary_expression:
                return left

            wk(none)

        if operator.is_logical_and_operator:
            left = parse1_logical_and_expression__left_operator(left, operator)

            operator = qk()

            if operator is none:
                if qn() is none:
                    raise_unknown_line()

                return left

            if operator.is_end_of_ternary_expression:
                return left

            wk(none)

        if operator.is_logical_or_operator:
            left = parse1_normal_expression__left_operator(left, operator)

            operator = qk()

            if operator is none:
                if qn() is none:
                    raise_unknown_line()

                return left

            if operator.is_end_of_ternary_expression:
                return left

            wk(none)

        if operator.is_keyword_and:
            left = parse1_boolean_and_expression__left_operator(left, operator)

            operator = qk()

            if operator is none:
                if qn() is none:
                    raise_unknown_line()

                return left

            if operator.is_end_of_ternary_expression:
                return left

            wk(none)


        if operator.is_keyword_or:
            left = parse1_boolean_or_expression__left_operator(left, operator)

            operator = qk()

            if operator is none:
                if qn() is none:
                    raise_unknown_line()

                return left

            if operator.is_end_of_ternary_expression:
                return left

            wk(none)

        if operator.is_keyword_if:
            return parse1_ternary_expression__left_operator(left, operator)

        #my_line('left: %r; operator: %r; s: %s', left, operator, portray_string(qs()[qj():]))
        raise_unknown_line()


    @share
    def parse1_ternary_expression():
        left = parse1_atom()

        operator = qk()

        if operator is not none:
            if operator.is_end_of_ternary_expression:
                return left

            wk(none)
        else:
            if qn() is not none:
                return left

            operator = tokenize_operator()

            if operator.is_end_of_ternary_expression:
                wk(operator)

                return left

        return parse1_ternary_expression__X__any_expression(left, operator)


    #
    #   16.  Ternary-Expression-List (Python 2.7.14rc1 grammer calls this 'testlist')
    #
    @share
    def parse1_ternary_expression_list__X_any_expresion(left, operator):
        if operator.is_postfix_operator:
            left = parse1_postfix_expression__left_operator(left, operator)

            operator = qk()

            if operator is none:
                if qn() is none:
                    raise_unknown_line()

                return left

            if operator.is_end_of_ternary_expression_list:
                return left

            wk(none)

        if operator.is_power_operator:
            left = parse1_power_expression__left_operator(left, operator)

            operator = qk()

            if operator is none:
                if qn() is none:
                    raise_unknown_line()

                return left

            if operator.is_end_of_ternary_expression_list:
                return left

            wk(none)

        if operator.is_multiply_operator:
            left = parse1_multiply_expression__left_operator(left, operator)

            operator = qk()

            if operator is none:
                if qn() is none:
                    raise_unknown_line()

                return left

            if operator.is_end_of_ternary_expression_list:
                return left

            wk(none)

        if operator.is_arithmetic_operator:
            left = parse1_arithmetic_expression__left_operator(left, operator)

            operator = qk()

            if operator is none:
                if qn() is none:
                    raise_unknown_line()

                return left

            if operator.is_end_of_ternary_expression_list:
                return left

            wk(none)

        if operator.is_logical_and_operator:
            left = parse1_logical_and_expression__left_operator(left, operator)

            operator = qk()

            if operator is none:
                if qn() is none:
                    raise_unknown_line()

                return left

            if operator.is_end_of_ternary_expression_list:
                return left

            wk(none)

        if operator.is_logical_or_operator:
            left = parse1_normal_expression__left_operator(left, operator)

            operator = qk()

            if operator is none:
                if qn() is none:
                    raise_unknown_line()

                return left

            if operator.is_end_of_ternary_expression_list:
                return left

            wk(none)

        if operator.is_compare_operator:
            left = parse1_compare_expression__left_operator(left, operator)

            operator = qk()

            if operator is none:
                if qn() is none:
                    raise_unknown_line()

                return left

            if operator.is_end_of_ternary_expression_list:
                return left

            wk(none)

        if operator.is_keyword_and:
            left = parse1_boolean_and_expression__left_operator(left, operator)

            operator = qk()

            if operator is none:
                if qn() is none:
                    raise_unknown_line()

                return left

            if operator.is_end_of_ternary_expression_list:
                return left

            wk(none)

        if operator.is_keyword_or:
            left = parse1_boolean_or_expression__left_operator(left, operator)

            operator = qk()

            if operator is none:
                if qn() is none:
                    raise_unknown_line()

                return left

            if operator.is_end_of_ternary_expression_list:
                return left

            wk(none)

        if operator.is_keyword_if:
            left = parse1_ternary_expression__left_operator(left, operator)

            operator = qk()

            if operator is none:
                if qn() is none:
                    raise_unknown_line()

                return left

            if operator.is_end_of_ternary_expression_list:
                return left

            wk(none)

        #my_line('line: %d; left: %r; operator: %r', ql(), left, operator)
        raise_unknown_line()


    @share
    def parse1_ternary_expression_list():
        left = parse1_atom()

        operator = qk()

        if operator is not none:
            if operator.is_end_of_ternary_expression_list:
                return left

            wk(none)
        else:
            if qn() is not none:
                return left

            operator = tokenize_operator()

            if operator.is_end_of_ternary_expression_list:
                wk(operator)

                return left

        return parse1_ternary_expression_list__X_any_expresion(left, operator)


    #
    #   17.  Comprehension-Expression-List (Python 2.7.14rc1 grammer calls this 'testlist_comp')
    #
    def parse1_comprehension_expression__left_operator(left, operator):
        assert operator.is_keyword_for

        while 7 is 7:
            if operator.is_keyword_for:
                middle = parse1_normal_expression_list()

                in_operator = qk()

                wk(none)

                if not in_operator.is_keyword_in:
                    #my_line('left: %r; operator: %r; middle: %r; in_operator: %r; s: %s',
                    #        left, operator, middle, in_operator, portray_string(qs()[qj():]))

                    raise_unknown_line()

                left = ComprehensionForExpression(left, operator, middle, in_operator, parse1_boolean_or_expression())

                operator = qk()

                if (operator is none) or (operator.is_end_of_comprehension_expression_list):
                    return left

                wk(none)

            if operator.is_keyword_if:
                left = ComprehensionIfExpression(left, operator, parse1_boolean_or_expression())

                operator = qk()

                if (operator is none) or (operator.is_end_of_comprehension_expression_list):
                    return left

                wk(none)

            assert (operator.is_keyword_for) or (operator.is_keyword_if)


    @share
    def parse1_comprehension_expression__X__any_expression(left, operator):
        if operator.is_postfix_operator:
            left = parse1_postfix_expression__left_operator(left, operator)

            operator = qk()

            if operator is none:
                if qn() is none:
                    raise_unknown_line()

                return left

            if operator.is_end_of_comprehension_expression:
                return left

            wk(none)

        if operator.is_power_operator:
            left = parse1_power_expression__left_operator(left, operator)

            operator = qk()

            if operator is none:
                if qn() is none:
                    raise_unknown_line()

                return left

            if operator.is_end_of_comprehension_expression:
                return left

            wk(none)

        if operator.is_multiply_operator:
            left = parse1_multiply_expression__left_operator(left, operator)

            operator = qk()

            if operator is none:
                if qn() is none:
                    raise_unknown_line()

                return left

            if operator.is_end_of_comprehension_expression:
                return left

            wk(none)

        if operator.is_arithmetic_operator:
            left = parse1_arithmetic_expression__left_operator(left, operator)

            operator = qk()

            if operator is none:
                if qn() is none:
                    raise_unknown_line()

                return left

            if operator.is_end_of_comprehension_expression:
                return left

            wk(none)

        if operator.is_compare_operator:
            left = parse1_compare_expression__left_operator(left, operator)

            operator = qk()

            if operator is none:
                if qn() is none:
                    raise_unknown_line()

                return left

            if operator.is_end_of_comprehension_expression:
                return left

            wk(none)

        if operator.is_logical_and_operator:
            left = parse1_logical_and_expression__left_operator(left, operator)

            operator = qk()

            if operator is none:
                if qn() is none:
                    raise_unknown_line()

                return left

            if operator.is_end_of_comprehension_expression:
                return left

            wk(none)

        if operator.is_logical_or_operator:
            left = parse1_normal_expression__left_operator(left, operator)

            operator = qk()

            if operator is none:
                if qn() is none:
                    raise_unknown_line()

                return left

            if operator.is_end_of_comprehension_expression:
                return left

            wk(none)

        if operator.is_keyword_and:
            left = parse1_boolean_and_expression__left_operator(left, operator)

            operator = qk()

            if operator is none:
                if qn() is none:
                    raise_unknown_line()

                return left

            if operator.is_end_of_comprehension_expression:
                return left

            wk(none)


        if operator.is_keyword_or:
            left = parse1_boolean_or_expression__left_operator(left, operator)

            operator = qk()

            if operator is none:
                if qn() is none:
                    raise_unknown_line()

                return left

            if operator.is_end_of_comprehension_expression:
                return left

            wk(none)

        if operator.is_keyword_if:
            left = parse1_ternary_expression__left_operator(left, operator)

            operator = qk()

            if operator is none:
                if qn() is none:
                    raise_unknown_line()

                return left

            if operator.is_end_of_comprehension_expression:
                return left

            wk(none)

        if operator.is_keyword_for:
            return parse1_comprehension_expression__left_operator(left, operator)

        my_line('left: %r; operator: %r; s: %s', left, operator, portray_string(qs()[qj():]))
        raise_unknown_line()
