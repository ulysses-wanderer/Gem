#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Expression')
def gem():
    require_gem('Sapphire.Elemental')


    class BookcaseExpression(Object):
        __slots__ = ((
            'left',                     #   Operator+
            'middle',                   #   Expression+
            'right',                    #   Operator+
        ))

        is__right_parenthesis__colon__newline = false
        is_right_parenthesis                  = false
        is_right_square_bracket               = false


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


        display_full_token = display_token


        def write(t, w):
            w(t.left.s)
            t.middle.write(w)
            t.right .write(w)


    @share
    class BookcaseAtom(BookcaseExpression):
        __slots__    = (())
        display_name = 'bookcased-atom'


        is__atom__or__special_operator = true
        is_atom                        = true


    @share
    class BookcaseIdentifier(BookcaseExpression):
        __slots__    = (())
        display_name = 'bookcased-identifier'


        is__atom__or__special_operator = true
        is_atom                        = true
        is_identifier                  = true


    @share
    class Arguments_1(BookcaseExpression):
        __slots__    = (())
        display_name = '(1)'


    @share
    class HeadIndex(BookcaseExpression):
        __slots__ = (())


        def display_token(t):
            if (t.left.s == '[') and (t.right.s == ':]'):
                return arrange('<head-index [ %s :]>', t.middle.display_token())

            return arrange('<head-index %s %s %s>',
                           t.left  .display_token(),
                           t.middle.display_token(),
                           t.right .display_token())


    @share
    class ListExpression_1(BookcaseExpression):
        __slots__                      = (())
        display_name                   = '[1]'
        is__atom__or__special_operator = true
        is_atom                        = true


        def display_token(t):
            if t.left.s == '[' and t.right.s == ']':
                return arrange('[%s]', t.middle.display_token())

            return arrange('<%s %s %s>',
                           t.left  .display_token(),
                           t.middle.display_token(),
                           t.right .display_token())


    @share
    class NormalIndex(BookcaseExpression):
        __slots__    = (())
        display_name = 'index'


        def display_token(t):
            if (t.left.s == '[') and (t.right.s == ']'):
                return arrange('<%s [ %s ]>', t.display_name, t.middle.display_token())

            return arrange('<%s %s %s %s>',
                           t.display_name,
                           t.left  .display_token(),
                           t.middle.display_token(),
                           t.right .display_token())


    @share
    class ParenthesizedExpression(BookcaseExpression):
        __slots__                      = (())
        display_name                   = '()'
        is__atom__or__special_operator = true
        is_atom                        = true


        def display_token(t):
            if t.left.s == '(' and t.right.s == ')':
                return arrange('(%s)', t.middle.display_token())

            return arrange('(%s %s %s)',
                           t.left  .display_token(),
                           t.middle.display_token(),
                           t.right .display_token())


    @share
    class TailIndex(BookcaseExpression):
        __slots__ = (())


        def display_token(t):
            if (t.left.s == '[:') and (t.right.s == ']'):
                return arrange('<tail-index [: %s ]>', t.middle.display_token())

            return arrange('<tail-index %s %s %s>',
                           t.left  .display_token(),
                           t.middle.display_token(),
                           t.right .display_token())

    @share
    class TupleExpression_1(BookcaseExpression):
        __slots__                      = (())
        display_name                   = '{,}'
        is__atom__or__special_operator = true
        is_atom                        = true


    class BookcasedDualExpression(Object):
        __slots__ = ((
            'left_operator',            #   Operator*
            'left',                     #   Expression*
            'middle_operator',          #   Operator*
            'right',                    #   Expression*
            'right_operator',           #   Operator*
        ))


        def __init__(t, left_operator, left, middle_operator, right, right_operator):
            t.left_operator   = left_operator
            t.left            = left
            t.middle_operator = middle_operator
            t.right           = right
            t.right_operator  = right_operator


        def __repr__(t):
            return arrange('<%s %r %r %r %r %r>',
                           t.__class__.__name__, t.left_operator, t.left, t.middle_operator, t.right, t.right_operator)


        def display_token(t):
            return arrange('<%s %s %s %s %s %s>',
                           t.display_name,
                           t.left_operator  .display_token(),
                           t.left           .display_token(),
                           t.middle_operator.display_token(),
                           t.right          .display_token(),
                           t.right_operator .display_token())


        def write(t, w):
            t.left_operator  .write(w)
            t.left           .write(w)
            t.middle_operator.write(w)
            t.right          .write(w)
            t.right_operator .write(w)


    @share
    class Arguments_2(BookcasedDualExpression):
        __slots__    = (())
        display_name = '(2)'


    @share
    class ListExpression_2(BookcasedDualExpression):
        __slots__                      = (())
        is__atom__or__special_operator = true
        is_atom                        = true


        def display_token(t):
            if t.left_operator.s == '[' and t.right_operator.s == ']':
                return arrange('<[2] %s %s %s>',
                               t.left           .display_token(),
                               t.middle_operator.display_token(),
                               t.right          .display_token())


            return arrange('<[2] %s %s %s %s %s>',
                           t.left_operator  .display_full_token(),
                           t.left           .display_token(),
                           t.middle_operator.display_token(),
                           t.right          .display_token(),
                           t.right_operator .display_full_token())


    @share
    class RangeIndex(BookcasedDualExpression):
        __slots__    = (())
        display_name = 'range-index'


    @share
    class TupleExpression_2(BookcasedDualExpression):
        __slots__                      = (())
        is__atom__or__special_operator = true
        is_atom                        = true


        def display_token(t):
            if t.left_operator.s == '(' and t.right_operator.s == ')':
                return arrange('({,2} %s %s %s)',
                               t.left           .display_token(),
                               t.middle_operator.display_token(),
                               t.right          .display_token())


            return arrange('({,2} %s %s %s %s %s)',
                           t.left_operator  .display_full_token(),
                           t.left           .display_token(),
                           t.middle_operator.display_token(),
                           t.right          .display_token(),
                           t.right_operator .display_full_token())


    Identifier .bookcase_meta = BookcaseIdentifier
    DoubleQuote.bookcase_meta = BookcaseAtom
    SingleQuote.bookcase_meta = BookcaseAtom
    Number     .bookcase_meta = BookcaseAtom
