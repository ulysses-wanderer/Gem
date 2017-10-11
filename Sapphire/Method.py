#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Method')
def gem():
    @share
    def find_require_gem__0(t, e):
        pass


    @share
    def is_name__0(t, name):
        return false


    @share
    def remove_comments__0(t):
        return 0


    @share
    def remove_comments__a__plain(t):
        a = t.a

        a__2 = a.remove_comments()

        if a is a__2:
            return t

        return t.conjure_plain(a__2)


    @share
    def remove_comments__ab(t):
        a = t.a
        b = t.b

        a__2 = a.remove_comments()
        b__2 = b.remove_comments()

        if (a is a__2) and (b is b__2):
            return t

        return t.conjure(a__2, b__2)


    @share
    def remove_comments__ab__always(t):
        return t.conjure(t.a.remove_comments(), t.b.remove_comments())


    @share
    def remove_comments__ab__plain(t):
        a = t.a
        b = t.b

        a__2 = a.remove_comments()
        b__2 = b.remove_comments()

        if (a is a__2) and (b is b__2):
            return t

        return t.conjure_plain(a__2, b__2)


    @share
    def remove_comments__self(t):
        return t


    @share
    def transform__ab(t, mutations):
        assert mutations.remove_comments

        a = t.a
        b = t.b

        a__2 = a.remove_comments()
        b__2 = b.transform(mutations)

        if (a is a__2) and (b is b__2):
            return t

        return t.conjure(a__2, b__2)
