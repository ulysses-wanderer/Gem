#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Parse1Call')
def gem():
    show = 0


    @share
    def parse1_call_expression__left__operator(left, left_parenthesis):
        return ExpressionCall(left, parse1_arguments__left_parenthesis(left_parenthesis))


    @share
    def parse1_argument7__left(left):
        operator = tokenize_operator()

        while not operator.is_end_of_expression:
            if operator.is_postfix_operator:
                left = parse1_postfix_expression__left__operator(left, operator)

                operator = qk()

                assert operator is not none

                wk(none)
                continue

            my_line('operator: %r', operator)
            raise_unknown_line(1)

        wk(operator)

        return left
    
    @share
    def parse1_arguments__left_parenthesis(left_parenthesis):
        argument_1 = parse1__argument__first_atom()

        if argument_1.is_right_parenthesis:
            raise_unknown_line(1)

        while 7 is 7:
            operator_1 = tokenize_operator()

            if operator_1.is_left_parenthesis:
                argument_1 = parse1_call_expression__left__operator(argument_1, operator_1)

                assert qk() is none
                assert qn() is none
                continue

            if operator_1.is_left_square_bracket:
                argument_1 = parse1_index_expression__left__operator(argument_1, operator_1)

                assert qk() is none
                assert qn() is none
                continue

            if operator_1.is_right_parenthesis:
                return Arguments_1(left_parenthesis, argument_1, operator_1)

            if operator_1.is_comma:
                break

            raise_unknown_line(2)

        argument_2 = parse1__argument__first_atom()

        if argument_2.is_right_parenthesis:
            return Arguments_1(
                       left_parenthesis,
                       argument_1,
                       Comma_RightParenthesis(operator_1, argument_2),
                   )

        argument_2 = parse1_argument7__left(argument_2)
        operator_2 = qk()

        wk(none)

        if operator_2.is_right_parenthesis:
            return Arguments_2(left_parenthesis, argument_1, operator_1, argument_2, operator_2)

        if not operator_2.is_comma:
            raise_unknown_line(4)

        argument_3 = parse1__argument__first_atom()

        if argument_3.is_right_parenthesis:
            return Arguments_2(
                       left_parenthesis,
                       argument_1,
                       operator_1,
                       argument_2,
                       Comma_RightParenthesis(operator_2, argument_3),
                   )

        many = [left_parenthesis, argument_1, operator_1, argument_2, operator_2]

        while 7 is 7:
            argument_3 = parse1_argument7__left(argument_3)
            operator_7 = qk()

            wk(none)

            if operator_7.is_right_parenthesis:
                many.append(argument_3)
                many.append(operator_7)
                return Arguments_Many(Tuple(many))

            if not operator_7.is_comma:
                raise_unknown_line(5)

            many.append(argument_3)

            argument_3 = parse1__argument__first_atom()

            if argument_3.is_right_parenthesis:
                many.append(Comma_RightParenthesis(operator_7, argument_3))
                return Arguments_Many(Tuple(many))

            many.append(operator_7)
