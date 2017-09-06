#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Expression')
def gem():
    require_gem('Sapphire.Elemental')


    @share
    class BinaryExpression(Object):
        __slots__ = ((
            'left',                     #   Expression
            'operator',                 #   Operator*
            'right',                    #   Expression
        ))


        def __init__(t, left, operator, right):
            assert type(left)  is not String
            assert type(right) is not String

            t.left     = left
            t.operator = operator
            t.right    = right


        def __repr__(t):
            return arrange('<%s %r %r %r>', t.__class__.__name__, t.left, t.operator, t.right)


        def display_token(t):
            return arrange('<%s %s %s %s>',
                           t.display_name,
                           t.left    .display_token(),
                           t.operator.display_token(),
                           t.right   .display_token())


        def write(t, w):
            t.left    .write(w)
            t.operator.write(w)
            t.right   .write(w)


    @share
    class CompareEqualExpression(BinaryExpression):
        __slots__    = (())
        display_name = '=='


    @share
    class CommaExpression(BinaryExpression):
        __slots__    = (())
        display_name = ','


    @share
    class OrExpression(BinaryExpression):
        __slots__    = (())
        display_name = 'or'


    @share
    class BaseExpression_Many(Object):
        __slots__ = ((
            'many',                     #   Tuple of *
        ))


        def __init__(t, many):
            t.many = many


        def __repr__(t):
            return arrange('<%s %r>', t.__class__.__name__, ' '.join(portray(v)   for v in t.many))


        def write(t, w):
            for v in t.many:
                v.write(w)


    @share
    class Arguments_Many(BaseExpression_Many):
        __slots__ = (())


        def display_token(t):
            many = t.many

            if (many[0].s == '(') and (many[-1].s == ')'):
                return arrange('(%s)', ' '.join(v.display_token()   for v in t.many[1:-1]))

            return arrange('(%s %s %s)',
                           t.many[0] .display_full_token(),
                           ' '.join(v.display_token()   for v in t.many[1:-1]),
                           t.many[-1].display_full_token())


    @share
    class ParameterColon_Many(BaseExpression_Many):
        __slots__ = (())


        def display_token(t):
            many = t.many

            if (many[0].s == '(') and (many[-1].s == '):'):
                return arrange('<(): %s>', ' '.join(v.display_token()   for v in t.many[1:-1]))

            return arrange('<(): %s %s %s>',
                           t.many[0] .display_full_token(),
                           ' '.join(v.display_token()   for v in t.many[1:-1]),
                           t.many[-1].display_full_token())


    @share
    class TupleExpression_Many(BaseExpression_Many):
        __slots__ = (())


        is__atom__or__right_parenthesis = true
        is_atom                         = true
        is_right_parenthesis            = false


        def display_token(t):
            many = t.many

            if (many[0].s == '(') and (many[-1].s == ')'):
                return arrange('({,*} %s)', ' '.join(v.display_token()   for v in t.many[1:-1]))

            return arrange('({,*} %s %s %s)',
                           t.many[0] .display_full_token(),
                           ' '.join(v.display_token()   for v in t.many[1:-1]),
                           t.many[-1].display_full_token())



    @share
    class Arguments_2(Object):
        __slots__ = ((
            'left_parenthesis',         #   OperatorLeftParenthesis
            'argument_0',               #   Expression*
            'comma_0',                  #   OperatorComma
            'argument_1',               #   Expression*
            'right_parenthesis',        #   OperatorRightParenthesis
        ))


        def __init__(t, left_parenthesis, argument_0, comma_0, argument_1, right_parenthesis):
            t.left_parenthesis  = left_parenthesis
            t.argument_0        = argument_0
            t.comma_0           = comma_0
            t.argument_1        = argument_1
            t.right_parenthesis = right_parenthesis


        def __repr__(t):
            return arrange('<Arguments_2 %r %r %r %r %r>',
                           t.left_parenthesis,
                           t.argument_0,
                           t.comma_0,
                           t.argument_1,
                           t.right_parenthesis)


        def display_token(t):
            return arrange('<(2) %s %s %s %s %s>',
                           t.left_parenthesis .display_token(),
                           t.argument_0       .display_token(),
                           t.comma_0          .display_token(),
                           t.argument_1       .display_token(),
                           t.right_parenthesis.display_token())


        def write(t, w):
            t.left_parenthesis .write(w)
            t.argument_0       .write(w)
            t.comma_0          .write(w)
            t.argument_1       .write(w)
            t.right_parenthesis.write(w)


    @share
    class ExpressionBookcase(Object):
        __slots__ = ((
            'left',                     #   Operator+
            'middle',                   #   Expression+
            'right',                    #   Operator+
        ))


        def __init__(t, left, middle, right):
            t.left   = left
            t.middle = middle
            t.right  = right


        def __repr__(t):
            return arrange('<%s %r %r %r>', t.__class__.__name__, t.left, t.middle, t.right)


        def display_token(t):
            return arrange('<%s %s %s %s>',
                           t.display_name,
                           t.left  .display_token(),
                           t.middle.display_token(),
                           t.right .display_token())


        def write(t, w):
            w(t.left.s)
            t.middle.write(w)
            t.right .write(w)


    @share
    class BookcaseAtom(ExpressionBookcase):
        __slots__    = (())
        display_name = 'bookcased-atom'


        is__atom__or__right_parenthesis       = true
        is_atom                               = true
        is__right_parenthesis__colon__newline = false
        is_right_parenthesis                  = false


    @share
    class Arguments_1(ExpressionBookcase):
        __slots__    = (())
        display_name = '(1)'


    @share
    class PathenthesizedExpression(ExpressionBookcase):
        __slots__                       = (())
        display_name                    = '()'
        is__atom__or__right_parenthesis = true
        is_atom                         = true
        is_right_parenthesis            = false


        def display_token(t):
            if t.left.s == '(' and t.right.s == ')':
                return arrange('(%s)', t.middle.display_token())

            return arrange('(%s %s %s)',
                           t.left  .display_token(),
                           t.middle.display_token(),
                           t.right .display_token())


    @share
    class TupleExpression_1(ExpressionBookcase):
        __slots__                       = (())
        display_name                    = '{,}'
        is__atom__or__right_parenthesis = true
        is_atom                         = true
        is_right_parenthesis            = false


    @share
    class ExpressionCall(Object):
        __slot__ = ((
            'left',                         #   Expression
            'arguments',                    #   Arguments*
        ))


        def __init__(t, left, arguments):
            assert type(arguments) is not String

            t.left      = left
            t.arguments = arguments


        def __repr__(t):
            return arrange('<ExpressionCall %r %r>', t.left, t.arguments)


        def display_token(t):
            return arrange('<call %s %s>', t.left.display_token(), t.arguments.display_token())


        def write(t, w):
            t.left     .write(w)
            t.arguments.write(w)


    @share
    class ExpressionDot(Object):
        __slots__ = ((
            'left',                     #   Expression
            'operator',                 #   OperatorDot
            'right',                    #   Identifier
        ))


        def __init__(t, left, operator, right):
            assert (type(left) is not String) and (operator.is_dot) and (right.is_identifier)

            t.left     = left
            t.operator = operator
            t.right    = right


        def __repr__(t):
            return arrange('<ExpressionDot %r %r %r>', t.left, t.operator, t.right)


        def display_token(t):
            return arrange('<. %s %s %s>',
                           t.left    .display_token(),
                           t.operator.display_token(),
                           t.right   .display_token())


        def write(t, w):
            t.left.write(w)
            w(t.operator.s + t.right.s)


    @share
    class ExpressionIndex_1(Object):
        __slots__ = ((
            'array',                    #   Expression
            'left_square_bracket',      #   LeftSquareBracket
            'index',                    #   Expression
            'right_square_bracket',     #   RightSquareBracket
        ))


        def __init__(t, array, left_square_bracket, index, right_square_bracket):
            t.array                = array
            t.left_square_bracket  = left_square_bracket
            t.index                = index
            t.right_square_bracket = right_square_bracket


        def __repr__(t):
            return arrange('<[] %r %r %r %r>',
                           t.array, t.left_square_bracket, t.index, t.right_square_bracket)


        def display_token(t):
            return arrange('<[] %s %s %s %s>',
                           t.array               .display_token(),
                           t.left_square_bracket .display_token(),
                           t.index               .display_token(),
                           t.right_square_bracket.display_token())


        def write(t, w):
            t.array               .write(w)
            t.left_square_bracket .write(w)
            t.index               .write(w)
            t.right_square_bracket.write(w)


    @share
    class ExpressionMethodCall(Object):
        __slot__ = ((
            'left',                     #   Expression
            'dot',                      #   OperatorDot
            'right',                    #   Identifier
            'arguments',                #   Arguments*
        ))


        def __init__(t, left, dot, right, arguments):
            t.left      = left
            t.dot       = dot
            t.right     = right
            t.arguments = arguments


        def __repr__(t):
            return arrange('<ExpressionCall %r %r %r %r>', t.left, t.dot, t.right, t.arguments)


    @share
    class TupleExpression_2(Object):
        __slots__ = ((
            'left',                     #   OperatorLeftParenthesis
            'middle_1',                 #   Expression+
            'comma_1',                  #   OperatorComma
            'middle_2',                 #   Expression+
            'right',                    #   OperatorRightParenthesis | Comma_RightParenthesis
        ))


        is__atom__or__right_parenthesis = true
        is_atom                         = true
        is_right_parenthesis            = false


        def __init__(t, left, middle_1, comma_1, middle_2, right):
            t.left     = left
            t.middle_1 = middle_1
            t.comma_1  = comma_1
            t.middle_2 = middle_2
            t.right    = right


        def __repr__(t):
            return arrange('<TupleExpression_2 %r %r %r %r %r>', t.left, t.middle_1, t.comma_1, t.middle_2, t.right)


        def display_token(t):
            if t.left.s == '(' and t.right.s == ')':
                return arrange('({,2} %s %s %s)',
                               t.middle_1.display_token(),
                               t.comma_1 .display_token(),
                               t.middle_2.display_token())

            return arrange('({,2} %s %s %s %s %s)',
                           t.left    .display_full_token(),
                           t.middle_1.display_token(),
                           t.comma_1 .display_token(),
                           t.middle_2.display_token(),
                           t.right   .display_full_token())


        def write(t, w):
            w(t.left.s)
            t.middle_1.write(w)
            t.comma_1 .write(w)
            t.middle_2.write(w)
            t.right   .write(w)


    class PostfixExpression(Object):
        __slots__ = ((
            'left',                     #   Expression
            'operator',                 #   Operator*
        ))


        def __init__(t, left, operator):
            t.left     = left
            t.operator = operator


        def __repr__(t):
            return arrange('<%s %r %r>', t.__class__.__name__, t.left, t.operator)


        def display_token(t):
            return arrange('<%s %s %s>',
                           t.display_name,
                           t.left    .display_token(),
                           t.operator.display_token())


        def write(t, w):
            t.left    .write(w)
            t.operator.write(w)


    @share
    class SuffixAtom(PostfixExpression):
        __slots__                             = (())
        display_name                          = 'suffixed-atom'
        is__atom__or__right_parenthesis       = true
        is_atom                               = true
        is__right_parenthesis__colon__newline = false
        is_right_parenthesis                  = false


    class UnaryExpression(Object):
        __slots__ = ((
            'operator',                 #   Operator*
            'right',                    #   Expression
        ))


        def __init__(t, operator, right):
            t.operator = operator
            t.right    = right


        def __repr__(t):
            return arrange('<%s %r %r>', t.__class__.__name__, t.operator, t.right)


        def display_token(t):
            return arrange('<%s %s %s>',
                           t.display_name,
                           t.operator.display_token(),
                           t.right   .display_token())


        def write(t, w):
            t.operator.write(w)
            t.right   .write(w)


    @share
    class NotExpression(UnaryExpression):
        __slots__    = (())
        display_name = 'not'


    @share
    class PrefixAtom(UnaryExpression):
        __slots__                             = (())
        display_name                          = 'prefixed-atom'
        is__atom__or__right_parenthesis       = true
        is_atom                               = true
        is__right_parenthesis__colon__newline = false
        is_right_parenthesis                  = false


    OperatorCompareEqual.compare_expression_meta = CompareEqualExpression
