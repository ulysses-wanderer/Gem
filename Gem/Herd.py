#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Gem.Herd')
def gem():
    #
    #   Herd:
    #
    #       Liquid (modifiable)
    #       Map (Associative Array)
    #       Unordered
    #       Key must not include absent
    #
    #   .inject
    #   .lookup
    #   .provide
    #       Use == for comparing keys
    #
    #       All the verbs here do NOT have an 'is' inside them.
    #
    #   .glimpse
    #   .insert
    #   .provision
    #       Unique Keys: Use 'is' for comparing keys
    #
    #       NOTE: All the verbs here have an 'is' inside them.
    #


    require_gem('Gem.Method')


    map__lookup  = Map.get
    map__provide = Map.setdefault
    map__store   = Map.__setitem__


    def item_0(pair):
        return pair[0]


    class Herd_0(Object):
        __slots__ = (())


        is_herd = true
        k1      = absent
        k2      = absent
        k3      = absent
        skip    = 0


        @static_method
        def items_sorted_by_key():
            return (())


    class Herd_1(Object):
        __slots__ = ((
            'a',                        #   Any
            'v',                        #   Any
        ))


        is_herd      = true
        is_herd_many = false
        k1           = absent
        k2           = absent
        k3           = absent
        skip         = 0


        def __init__(t, a, v):
            assert a is not absent

            t.a = a
            t.v = v


        def displace(t, k, v):
            assert t.a is k

            t.v = v


        def glimpse(t, k, d = none):
            if t.a is k: return t.v

            assert k is not absent

            return d


        def insert(t, b, w):
            assert (b is not absent) and (t.a is not b)

            return create_herd_2(t.a, b, t.v, w)


        def items_sorted_by_key(t):
            return (( ((t.a, t.v)), ))


        def provision(t, b, w):
            a = t.a
            if a is b: return t

            return create_herd_2(a, b, t.v, w)


        if 0:
            def provision_triple(t, displace, Meta, k1, k2, k3):
                a = t.a
                if a is k2:
                    v = t.v
                    if v.k3 is k3:  return v

                    if not v.is_herd:
                        r   = Meta(k1, k2, k3)
                        t.v = create_herd_2(v.k3, k3, v, r)
                        return r

                    return v.provision_triple_step2(displace_1v, t, Meta, k1, k2, k3)

                r = Meta(k1, k2, k3)

                displace(k1, create_herd_2(a, k2, t.v, r))

                return r


        if 0:
            def provision_triple__312(t, displace, Meta, k1, k2, k3):
                a = t.a
                if a is k1:
                    v = t.v
                    if v.k2 is k2:  return v

                    if not v.is_herd:
                        r   = Meta(k1, k2, k3)
                        t.v = create_herd_2(v.k2, k2, v, r)
                        return r

                    return v.provision_triple_step2__312(displace_1v, t, Meta, k1, k2, k3)

                r = Meta(k1, k2, k3)

                displace(k3, create_herd_2(a, k1, t.v, r))

                return r


        if 0:
            def provision_triple_step2(t, displace, parent, Meta, k1, k2, k3):
                a = t.a
                if a is k3:     return t.v

                r = Meta(k1, k2, k3)

                if parent.is_herd_many:
                    displace(parent, k2, create_herd_2(a, k3, t.v, r))
                    return r

                displace(parent, create_herd_2(a, k3, t.v, r))
                return r


    class Herd_2(Object):
        __slots__ = ((
            'a',                        #   Any
            'b',                        #   Any
            'v',                        #   Any
            'w',                        #   Any
        ))


        is_herd      = true
        is_herd_many = false
        k1           = absent
        k2           = absent
        k3           = absent
        skip         = 0


        def count_nested(t):
            v = t.v
            w = t.w

            if v.is_herd:
                if w.is_herd:
                    return v.count_nested() + w.count_nested()

                return v.count_nested() + 1

            if w.is_herd:
                return 1 + w.count_nested()

            return 2


        def displace(t, k, v):
            if t.a is k:
                t.v = v
                return

            assert t.b is k

            t.w = v


        def glimpse(t, k, d = none):
            if t.a is k: return t.v
            if t.b is k: return t.w

            assert k is not absent

            return d


        def insert(t, c, x):
            assert (c is not absent) and (t.a is not c) and (t.b is not c)

            return create_herd_3(t.a, t.b, c, t.v, t.w, x)


        def items_sorted_by_key(t):
            a = t.a
            b = t.b

            nub = a.nub

            av = ((a, t.v))
            bw = ((b, t.w))

            if nub(a) < nub(b):
                return ((av, bw))

            return ((bw, av))


        def provision(t, c, x):
            a = t.a
            if a is c: return t

            b = t.b
            if b is c: return t

            return create_herd_3(a, b, c, t.v, t.w, x)


        def provision_dual(t, displace, Meta, k1, k2):
            a = t.a
            if a is k2: return t.v

            b = t.b
            if b is k2: return t.w

            r = Meta(k1, k2)

            displace(k1, create_herd_3(a, b, k2, t.v, t.w, r))

            return r


        def provision_dual__21(t, displace, Meta, k1, k2):
            a = t.a
            if a is k1: return t.v

            b = t.b
            if b is k1: return t.w

            r = Meta(k1, k2)

            displace(k2, create_herd_3(a, b, k1, t.v, t.w, r))

            return r


        def provision_triple(t, displace, Meta, k1, k2, k3):
            a = t.a
            if a is k2:
                v = t.v
                if v.k3 is k3:  return v

                if not v.is_herd:
                    r   = Meta(k1, k2, k3)
                    t.v = create_herd_2(v.k3, k3, v, r)
                    return r

                return v.provision_triple_step2(displace_2v, t, Meta, k1, k2, k3)

            b = t.b
            if b is k2:
                w = t.w
                if w.k3 is k3:  return w

                if not w.is_herd:
                    r   = Meta(k1, k2, k3)
                    t.w = create_herd_2(w.k3, k3, w, r)
                    return r

                return w.provision_triple_step2(displace_2w, t, Meta, k1, k2, k3)

            r = Meta(k1, k2, k3)

            displace(k1, create_herd_3(a, b, k2, t.v, t.w, r))

            return r


        def provision_triple__312(t, displace, Meta, k1, k2, k3):
            a = t.a
            if a is k1:
                v = t.v
                if v.k2 is k2:  return v

                if not v.is_herd:
                    r   = Meta(k1, k2, k3)
                    t.v = create_herd_2(v.k2, k2, v, r)
                    return r

                return v.provision_triple_step2__312(displace_2v, t, Meta, k1, k2, k3)

            b = t.b
            if b is k1:
                w = t.w
                if w.k2 is k2:  return w

                if not w.is_herd:
                    r   = Meta(k1, k2, k3)
                    t.w = create_herd_2(w.k2, k2, w, r)
                    return r

                return w.provision_triple_step2__312(displace_2w, t, Meta, k1, k2, k3)

            r = Meta(k1, k2, k3)

            displace(k3, create_herd_3(a, b, k1, t.v, t.w, r))

            return r


        def provision_triple_step2(t, displace, parent, Meta, k1, k2, k3):
            a = t.a
            if a is k3:     return t.v

            b = t.b
            if b is k3:     return t.w

            r = Meta(k1, k2, k3)

            if parent.is_herd_many:
                displace(parent, k2, create_herd_3(a, b, k3, t.v, t.w, r))
                return r

            displace(parent, create_herd_3(a, b, k3, t.v, t.w, r))
            return r


        def provision_triple_step2__312(t, displace, parent, Meta, k1, k2, k3):
            a = t.a
            if a is k2:     return t.v

            b = t.b
            if b is k2:     return t.w

            r = Meta(k1, k2, k3)

            if parent.is_herd_many:
                displace(parent, k1, create_herd_3(a, b, k2, t.v, t.w, r))
                return r

            displace(parent, create_herd_3(a, b, k2, t.v, t.w, r))
            return r


        def sanitize(t):
            v = t.v.sanitize()
            w = t.w.sanitize()

            if v is 0:  return w
            if w is 0:  return v

            t.v = v
            t.w = w
            return t


    class Herd_3(Object):
        __slots__ = ((
            'a',                        #   Any
            'b',                        #   Any
            'c',                        #   Any
            'v',                        #   Any
            'w',                        #   Any
            'x',                        #   Any
        ))


        is_herd      = true
        is_herd_many = false
        k1           = absent
        k2           = absent
        k3           = absent
        skip         = 0


        def count_nested(t):
            v = t.v
            w = t.w
            x = t.x

            if v.is_herd:
                if w.is_herd:
                    if x.is_herd:
                        return v.count_nested() + w.count_nested() + x.count_nested()

                    return v.count_nested() + w.count_nested() + 1

                if x.is_herd:
                    return v.count_nested() + 1 + x.count_nested()

                return v.count_nested() + 2

            if w.is_herd:
                if x.is_herd:
                    return 1 + w.count_nested() + x.count_nested()

                return 2 + w.count_nested()         #  1 + w.count_nested() + 1

            if x.is_herd:
                return 2 + x.count_nested()

            return 3


        def displace(t, k, v):
            if t.a is k:
                t.v = v
                return

            if t.b is k:
                t.w = v
                return

            assert t.c is k

            t.x = v


        def glimpse(t, k, d = none):
            if t.a is k: return t.v
            if t.b is k: return t.w
            if t.c is k: return t.x

            assert k is not absent

            return d


        def insert(t, d, y):
            assert (d is not absent) and (t.a is not d) and (t.b is not d) and (t.c is not d)

            return create_herd_4567(t.a, t.b, t.c, d, t.v, t.w, t.x, y)


        def items_sorted_by_key(t):
            a = t.a
            b = t.b
            c = t.c

            nub = a.nub

            av = ((a, t.v))
            bw = ((b, t.w))
            cx = ((c, t.x))
            ka = nub(a)
            kb = nub(b)
            kc = nub(c)

            if ka < kb:
                if kb < kc:
                    return ((av, bw, cx))

                if ka < kc:
                    return ((av, cx, bw))

                return ((cx, av, bw))

            if ka < kc:
                return ((bw, av, cx))

            if kb < kc:
                return ((bw, cx, av))

            return ((cx, bw, av))


        def provision(t, d, y):
            a = t.a
            if a is d: return t

            b = t.b
            if b is d: return t

            c = t.c
            if c is d: return t

            return create_herd_4567(a, b, c, d, t.v, t.w, t.x, y)


        def provision_dual(t, displace, Meta, k1, k2):
            a = t.a
            if a is k2: return t.v

            b = t.b
            if b is k2: return t.w

            c = t.c
            if c is k2: return t.x

            r = Meta(k1, k2)

            displace(k1, create_herd_4567(a, b, c, k2, t.v, t.w, t.x, r))

            return r


        def provision_dual__21(t, displace, Meta, k1, k2):
            a = t.a
            if a is k1: return t.v

            b = t.b
            if b is k1: return t.w

            c = t.c
            if c is k1: return t.x

            r = Meta(k1, k2)

            displace(k2, create_herd_4567(a, b, c, k1, t.v, t.w, t.x, r))

            return r


        def provision_triple(t, displace, Meta, k1, k2, k3):
            a = t.a
            if a is k2:
                v = t.v
                if v.k3 is k3:  return v

                if not v.is_herd:
                    r   = Meta(k1, k2, k3)
                    t.v = create_herd_2(v.k3, k3, v, r)
                    return r

                return v.provision_triple_step2(displace_3v, t, Meta, k1, k2, k3)

            b = t.b
            if b is k2:
                w = t.w
                if w.k3 is k3:  return w

                if not w.is_herd:
                    r   = Meta(k1, k2, k3)
                    t.w = create_herd_2(w.k3, k3, w, r)
                    return r

                return w.provision_triple_step2(displace_3w, t, Meta, k1, k2, k3)

            c = t.c
            if c is k2:
                x = t.x
                if x.k3 is k3:  return x

                if not x.is_herd:
                    r   = Meta(k1, k2, k3)
                    t.x = create_herd_2(x.k3, k3, x, r)
                    return r

                return x.provision_triple_step2(displace_3x, t, Meta, k1, k2, k3)

            r = Meta(k1, k2, k3)

            displace(k1, create_herd_4567(a, b, c, k2, t.v, t.w, t.x, r))

            return r


        def provision_triple__312(t, displace, Meta, k1, k2, k3):
            a = t.a
            if a is k1:
                v = t.v
                if v.k2 is k2:  return v

                if not v.is_herd:
                    r   = Meta(k1, k2, k3)
                    t.v = create_herd_2(v.k2, k2, v, r)
                    return r

                return v.provision_triple_step2__312(displace_3v, t, Meta, k1, k2, k3)

            b = t.b
            if b is k1:
                w = t.w
                if w.k2 is k2:  return w

                if not w.is_herd:
                    r   = Meta(k1, k2, k3)
                    t.w = create_herd_2(w.k2, k2, w, r)
                    return r

                return w.provision_triple_step2__312(displace_3w, t, Meta, k1, k2, k3)

            c = t.c
            if c is k1:
                x = t.x
                if x.k2 is k2:  return x

                if not x.is_herd:
                    r   = Meta(k1, k2, k3)
                    t.x = create_herd_2(x.k2, k2, x, r)
                    return r

                return x.provision_triple_step2__312(displace_3x, t, Meta, k1, k2, k3)

            r = Meta(k1, k2, k3)

            displace(k3, create_herd_4567(a, b, c, k1, t.v, t.w, t.x, r))

            return r


        def provision_triple_step2(t, displace, parent, Meta, k1, k2, k3):
            a = t.a
            if a is k3:     return t.v

            b = t.b
            if b is k3:     return t.w

            c = t.c
            if c is k3:     return t.x

            r = Meta(k1, k2, k3)

            if parent.is_herd_many:
                displace(parent, k2, create_herd_4567(a, b, c, k3, t.v, t.w, t.x, r))
                return r

            displace(parent, create_herd_4567(a, b, c, k3, t.v, t.w, t.x, r))
            return r


        def provision_triple_step2__312(t, displace, parent, Meta, k1, k2, k3):
            a = t.a
            if a is k2:     return t.v

            b = t.b
            if b is k2:     return t.w

            c = t.c
            if c is k2:     return t.x

            r = Meta(k1, k2, k3)

            if parent.is_herd_many:
                displace(parent, k1, create_herd_4567(a, b, c, k2, t.v, t.w, t.x, r))
                return r

            displace(parent, create_herd_4567(a, b, c, k2, t.v, t.w, t.x, r))
            return r


        def sanitize(t):
            v = t.v.sanitize()
            w = t.w.sanitize()
            x = t.x.sanitize()

            if v is 0:
                if w is 0:  return x
                if x is 0:  return w

                return create_herd_2(t.b, t.c, w, x)

            if w is 0:
                if x is 0:  return v

                return create_herd_2(t.a, t.c, v, x)

            if x is 0:
                return create_herd_2(t.a, t.b, v, w)

            t.v = v
            t.w = w
            t.x = x
            return t


    class Herd_4567(Object):
        __slots__ = ((
            'a',                        #   Any
            'b',                        #   Any
            'c',                        #   Any
            'd',                        #   Any
            'e',                        #   Absent | Any
            'e6',                       #   Absent | Vacant | Any
            'e7',                       #   Absent | Vacant | Any
            'v',                        #   Any
            'w',                        #   Any
            'x',                        #   Any
            'y',                        #   Any
            'z',                        #   Any
            'z6',                       #   Any
            'z7',                       #   Any
        ))


        is_herd      = true
        is_herd_many = false
        k1           = absent
        k2           = absent
        k3           = absent
        skip         = 0


        def count_nested(t):
            v = t.v
            w = t.w
            x = t.x
            y = t.y

            if t.e is absent:
                return (
                             (v.count_nested()   if v.is_herd else   1)
                           + (w.count_nested()   if w.is_herd else   1)
                           + (x.count_nested()   if x.is_herd else   1)
                           + (y.count_nested()   if y.is_herd else   1)
                       )

            z = t.z

            if t.e6 is absent:
                return (
                             (v.count_nested()   if v.is_herd else   1)
                           + (w.count_nested()   if w.is_herd else   1)
                           + (x.count_nested()   if x.is_herd else   1)
                           + (y.count_nested()   if y.is_herd else   1)
                           + (z.count_nested()   if z.is_herd else   1)
                       )


            z6 = t.z6

            if t.e7 is absent:
                return (
                             (v .count_nested()   if v .is_herd else   1)
                           + (w .count_nested()   if w .is_herd else   1)
                           + (x .count_nested()   if x .is_herd else   1)
                           + (y .count_nested()   if y .is_herd else   1)
                           + (z .count_nested()   if z .is_herd else   1)
                           + (z6.count_nested()   if z6.is_herd else   1)
                       )

            z7 = t.z7

            return (
                         (v .count_nested()   if v .is_herd else   1)
                       + (w .count_nested()   if w .is_herd else   1)
                       + (x .count_nested()   if x .is_herd else   1)
                       + (y .count_nested()   if y .is_herd else   1)
                       + (z .count_nested()   if z .is_herd else   1)
                       + (z6.count_nested()   if z6.is_herd else   1)
                       + (z7.count_nested()   if z7.is_herd else   1)
                   )


        def displace(t, k, v):
            if t.a is k:
                t.v = v
                return

            if t.b is k:
                t.w = v
                return

            if t.c is k:
                t.x = v
                return

            if t.d is k:
                t.y = v
                return

            if t.e is k:
                t.z = v
                return

            if t.e6 is k:
                t.z6 = v
                return

            assert t.e7 is k

            t.z7 = v


        def glimpse(t, k, d = none):
            if t.a is k:        return t.v
            if t.b is k:        return t.w
            if t.c is k:        return t.x
            if t.d is k:        return t.y

            assert k is not absent

            e = t.e
            if e is k:          return t.z
            if e is absent:     return d

            e6 = t.e6
            if e6 is k:         return t.z6
            if e6 is absent:    return d

            if t.e7 is k:       return t.z7

            return d


        def insert(t, e8, z8):
            assert (t.a is not e8) and (t.b is not e8) and (t.c is not e8) and (t.d is not e8)
            assert e8 is not absent

            e = t.e
            if e is absent:
                t.e  = e8
                t.e6 = absent
                t.z  = z8
                return t
            assert t.e is not e8

            e6 = t.e6
            if e6 is absent:
                t.e6 = e8
                t.e7 = absent
                t.z6 = z8
                return t
            assert t.e6 is not e8

            e7 = t.e7
            if e7 is absent:
                t.e7 = e8
                t.z7 = z8
                return t
            assert t.e7 is not e8

            return create_herd_many(t.a, t.b, t.c, t.d, e, e6, e7, e8, t.v, t.w, t.x, t.y, t.z, t.z6, t.z7, z8)


        def items_sorted_by_key(t):
            a   = t.a
            nub = a.nub

            e = t.e

            if e is absent:
                r = [((a, t.v)), ((t.b, t.w)), ((t.c, t.x)), ((t.d, t.y))]
            else:
                e6 = t.e6

                if e6 is absent:
                    r = [((a, t.v)), ((t.b, t.w)), ((t.c, t.x)), ((t.d, t.y)), ((e, t.z))]
                else:
                    e7 = t.e7

                    if e7 is absent:
                        r = [((a, t.v)), ((t.b, t.w)), ((t.c, t.x)), ((t.d, t.y)), ((e, t.z)), ((e6, t.z6))]
                    else:
                        r = [
                                ((a,   t.v)),
                                ((t.b, t.w)),
                                ((t.c, t.x)),
                                ((t.d, t.y)),
                                ((e,   t.z)),
                                ((e6,  t.z6)),
                                ((e7,  t.z7)),
                            ]


            if nub is 0:
                r.sort(key = item_0)

                return r


            def nub_of_item_0(pair):
                return nub(pair[0])


            r.sort(key = nub_of_item_0)

            return r


        def provision(t, e8, z8):
            a = t.a
            if a is e8: return t

            b = t.b
            if b is e8: return t

            c = t.c
            if c is e8: return t

            d = t.d
            if d is e8: return t

            assert e8 is not absent

            e = t.e
            if e is e8: return t
            if e is absent:
                t.e  = e8
                t.z  = z8
                t.e6 = absent
                return t

            e6 = t.e6
            if e6 is e8: return t
            if e6 is absent:
                t.e6 = e8
                t.z6 = z8
                t.e7 = absent
                return t

            e7 = t.e7
            if e7 is e8: return t
            if e7 is absent:
                t.e7 = e8
                t.z7 = z8
                return t

            return create_herd_many(a, b, c, d, e, e6, e7, e8, t.v, t.w, t.x, t.y, t.z, t.z6, t.z7, z8)


        def provision_dual(t, displace, Meta, k1, k2):
            a = t.a
            if a is k2:     return t.v

            b = t.b
            if b is k2:     return t.w

            c = t.c
            if c is k2:     return t.x

            d = t.d
            if d is k2:     return t.y

            e = t.e
            if e is k2:     return t.z
            if e is absent:
                t.e  = k2
                t.e6 = absent
                t.z  = r = Meta(k1, k2)
                return r

            e6 = t.e6
            if e6 is k2:    return t.z6
            if e6 is absent:
                t.e6 = k2
                t.e7 = absent
                t.z6 = r = Meta(k1, k2)
                return r

            e7 = t.e7
            if e7 is k2:    return t.z7

            r = Meta(k1, k2)

            if e7 is absent:
                t.e7 = k2
                t.z7 = Meta(k1, k2)
                return r

            displace(k1, create_herd_many(a, b, c, d, e, e6, e7, k2, t.v, t.w, t.x, t.y, t.z, t.z6, t.z7, r))

            return r


        def provision_dual__21(t, displace, Meta, k1, k2):
            a = t.a
            if a is k1:     return t.v

            b = t.b
            if b is k1:     return t.w

            c = t.c
            if c is k1:     return t.x

            d = t.d
            if d is k1:     return t.y

            e = t.e
            if e is k1:     return t.z
            if e is absent:
                t.e  = k1
                t.e6 = absent
                t.z  = r = Meta(k1, k2)
                return r

            e6 = t.e6
            if e6 is k1:    return t.z6
            if e6 is absent:
                t.e6 = k1
                t.e7 = absent
                t.z6 = r = Meta(k1, k2)
                return r

            e7 = t.e7
            if e7 is k1:    return t.z7

            r = Meta(k1, k2)

            if e7 is absent:
                t.e7 = k1
                t.z7 = Meta(k1, k2)
                return r

            displace(k2, create_herd_many(a, b, c, d, e, e6, e7, k1, t.v, t.w, t.x, t.y, t.z, t.z6, t.z7, r))

            return r


        def provision_triple(t, displace, Meta, k1, k2, k3):
            a = t.a
            if a is k2:
                v = t.v
                if v.k3 is k3:  return v
                if not v.is_herd:
                    r   = Meta(k1, k2, k3)
                    t.v = create_herd_2(v.k3, k3, v, r)
                    return r
                return v.provision_triple_step2(displace_4v, t, Meta, k1, k2, k3)

            b = t.b
            if b is k2:
                w = t.w
                if w.k3 is k3:  return w
                if not w.is_herd:
                    r   = Meta(k1, k2, k3)
                    t.w = create_herd_2(w.k3, k3, w, r)
                    return r
                return w.provision_triple_step2(displace_4w, t, Meta, k1, k2, k3)

            c = t.c
            if c is k2:
                x = t.x
                if x.k3 is k3:  return x
                if not x.is_herd:
                    r   = Meta(k1, k2, k3)
                    t.x = create_herd_2(x.k3, k3, x, r)
                    return r
                return x.provision_triple_step2(displace_4x, t, Meta, k1, k2, k3)

            d = t.d
            if d is k2:
                y = t.y
                if y.k3 is k3:  return y
                if not y.is_herd:
                    r   = Meta(k1, k2, k3)
                    t.y = create_herd_2(y.k3, k3, y, r)
                    return r
                return y.provision_triple_step2(displace_4y, t, Meta, k1, k2, k3)

            e = t.e
            if e is k2:
                z = t.z
                if z.k3 is k3:  return z
                if not z.is_herd:
                    r   = Meta(k1, k2, k3)
                    t.z = create_herd_2(z.k3, k3, z, r)
                    return r
                return z.provision_triple_step2(displace_4z, t, Meta, k1, k2, k3)
            if e is absent:
                t.e  = k2
                t.e6 = absent
                t.z  = r = Meta(k1, k2, k3)
                return r

            e6 = t.e6
            if e6 is k2:
                z6 = t.z6
                if z6.k3 is k3:  return z6
                if not z6.is_herd:
                    r    = Meta(k1, k2, k3)
                    t.z6 = create_herd_2(z6.k3, k3, z6, r)
                    return r
                return z6.provision_triple_step2(displace_4z6, t, Meta, k1, k2, k3)
            if e6 is absent:
                t.e6 = k2
                t.e7 = absent
                t.z6 = r = Meta(k1, k2, k3)
                return r

            e7 = t.e7
            if e7 is k2:
                z7 = t.z7
                if z7.k3 is k3:  return z7
                if not z7.is_herd:
                    r    = Meta(k1, k2, k3)
                    t.z7 = create_herd_2(z7.k3, k3, z7, r)
                    return r
                return z7.provision_triple_step2(displace_4z7, t, Meta, k1, k2, k3)
            r = Meta(k1, k2, k3)                                                        #   r created here
            if e7 is absent:
                t.e7 = k2
                t.z7 = r = Meta(k1, k2, k3)
                return r

            displace(k1, create_herd_many(a, b, c, d, e, e6, e7, k2, t.v, t.w, t.x, t.y, t.z, t.z6, t.z7, r))

            return r


        def provision_triple__312(t, displace, Meta, k1, k2, k3):
            a = t.a
            if a is k1:
                v = t.v
                if v.k2 is k2:  return v
                if not v.is_herd:
                    r   = Meta(k1, k2, k3)
                    t.v = create_herd_2(v.k2, k2, v, r)
                    return r
                return v.provision_triple_step2__312(displace_4v, t, Meta, k1, k2, k3)

            b = t.b
            if b is k1:
                w = t.w
                if w.k2 is k2:  return w
                if not w.is_herd:
                    r   = Meta(k1, k2, k3)
                    t.w = create_herd_2(w.k2, k2, w, r)
                    return r
                return w.provision_triple_step2__312(displace_4w, t, Meta, k1, k2, k3)

            c = t.c
            if c is k1:
                x = t.x
                if x.k2 is k2:  return x
                if not x.is_herd:
                    r   = Meta(k1, k2, k3)
                    t.x = create_herd_2(x.k2, k2, x, r)
                    return r
                return x.provision_triple_step2__312(displace_4x, t, Meta, k1, k2, k3)

            d = t.d
            if d is k1:
                y = t.y
                if y.k2 is k2:  return y
                if not y.is_herd:
                    r   = Meta(k1, k2, k3)
                    t.y = create_herd_2(y.k2, k2, y, r)
                    return r
                return y.provision_triple_step2__312(displace_4y, t, Meta, k1, k2, k3)

            e = t.e
            if e is k1:
                z = t.z
                if z.k2 is k2:  return z
                if not z.is_herd:
                    r   = Meta(k1, k2, k3)
                    t.z = create_herd_2(z.k2, k2, z, r)
                    return r
                return z.provision_triple_step2__312(displace_4z, t, Meta, k1, k2, k3)
            if e is absent:
                t.e  = k1
                t.e6 = absent
                t.z  = r = Meta(k1, k2, k3)
                return r

            e6 = t.e6
            if e6 is k1:
                z6 = t.z6
                if z6.k2 is k2:  return z6
                if not z6.is_herd:
                    r    = Meta(k1, k2, k3)
                    t.z6 = create_herd_2(z6.k2, k2, z6, r)
                    return r
                return z6.provision_triple_step2__312(displace_4z6, t, Meta, k1, k2, k3)
            if e6 is absent:
                t.e6 = k1
                t.e7 = absent
                t.z6 = r = Meta(k1, k2, k3)
                return r

            e7 = t.e7
            if e7 is k1:
                z7 = t.z7
                if z7.k2 is k2:  return z7
                if not z7.is_herd:
                    r    = Meta(k1, k2, k3)
                    t.z7 = create_herd_2(z7.k2, k2, z7, r)
                    return r
                return z7.provision_triple_step2__312(displace_4z7, t, Meta, k1, k2, k3)
            r = Meta(k1, k2, k3)                                                        #   r created here
            if e7 is absent:
                t.e7 = k1
                t.z7 = r = Meta(k1, k2, k3)
                return r

            displace(k3, create_herd_many(a, b, c, d, e, e6, e7, k1, t.v, t.w, t.x, t.y, t.z, t.z6, t.z7, r))

            return r


        def provision_triple_step2(t, displace, parent, Meta, k1, k2, k3):
            a = t.a
            if a is k3:     return t.v

            b = t.b
            if b is k3:     return t.w

            c = t.c
            if c is k3:     return t.x

            d = t.d
            if d is k3:     return t.y

            e = t.e
            if e is k3:     return t.z
            if e is absent:
                t.e  = k3
                t.e6 = absent
                t.z  = r = Meta(k1, k2, k3)
                return r

            e6 = t.e6
            if e6 is k3:    return t.z6
            if e6 is absent:
                t.e6 = k3
                t.e7 = absent
                t.z6 = r = Meta(k1, k2, k3)
                return r

            e7 = t.e7
            if e7 is k3:    return t.z7

            r = Meta(k1, k2, k3)

            if e7 is absent:
                t.e7 = k3
                t.z7 = r
                return r

            if parent.is_herd_many:
                displace(
                    parent,
                    k2,
                    create_herd_many(a, b, c, d, e, e6, e7, k3, t.v, t.w, t.x, t.y, t.z, t.z6, t.z7, r),
                )

                return r

            displace(parent, create_herd_many(a, b, c, d, e, e6, e7, k3, t.v, t.w, t.x, t.y, t.z, t.z6, t.z7, r))
            return r


        def provision_triple_step2__312(t, displace, parent, Meta, k1, k2, k3):
            a = t.a
            if a is k2:     return t.v

            b = t.b
            if b is k2:     return t.w

            c = t.c
            if c is k2:     return t.x

            d = t.d
            if d is k2:     return t.y

            e = t.e
            if e is k2:     return t.z
            if e is absent:
                t.e  = k2
                t.e6 = absent
                t.z  = r = Meta(k1, k2, k3)
                return r

            e6 = t.e6
            if e6 is k2:    return t.z6
            if e6 is absent:
                t.e6 = k2
                t.e7 = absent
                t.z6 = r = Meta(k1, k2, k3)
                return r

            e7 = t.e7
            if e7 is k2:    return t.z7

            r = Meta(k1, k2, k3)

            if e7 is absent:
                t.e7 = k2
                t.z7 = r
                return r

            if parent.is_herd_many:
                displace(
                    parent,
                    k1,
                    create_herd_many(a, b, c, d, e, e6, e7, k2, t.v, t.w, t.x, t.y, t.z, t.z6, t.z7, r),
                )

                return r

            displace(parent, create_herd_many(a, b, c, d, e, e6, e7, k2, t.v, t.w, t.x, t.y, t.z, t.z6, t.z7, r))
            return r


        def sanitize(t):
            #
            #   a/v:    unknown
            #
            v = t.v.sanitize()
            if v is 0:
                #
                #   This should be:
                #
                #       index = 0
                #
                #   However, instead the code that should be below:
                #
                #       if index is 0:
                #           v = t.w.sanitize()
                #           if v is not 0:
                #               a     = t.b
                #               index = 1
                #
                #   is inline'd into here and then rewritten as:
                #
                #       v = t.w.sanitize()
                #       if v is 0:
                #           index = 0
                #       else:
                #           a     = t.b
                #           index = 1
                #

                #
                #   .a/.v:    sanitize
                #   .b/.w:    unknown
                #
                v = t.w.sanitize()
                if v is 0:
                    index = 0
                else:
                    a     = t.b
                    index = 1
            else:
                #
                #   .a/.v:    keep
                #   .b/.w:    unknown
                #
                w = t.w.sanitize()
                if w is 0:
                    a     = t.a
                    index = 1
                else:
                    #
                    #   .a/.v:    keep
                    #   .b/.w:    keep
                    #   .c/.x:    unknown
                    #
                    x = t.x.sanitize()

                    if x is 0:
                        a     = t.a
                        b     = t.b
                        index = 2
                    else:
                        #
                        #   .a/.v:    keep
                        #   .b/.w:    keep
                        #   .c/.x:    keep
                        #   .d/.y:    unknown
                        #
                        y = t.y.sanitize()

                        if y is 0:
                            a     = t.a
                            b     = t.b
                            c     = t.c
                            index = 2
                        else:
                            if t.e is absent:
                                t.v = v
                                t.w = w
                                t.x = x
                                t.y = y
                                return t

                            #
                            #   .a/.v:    keep
                            #   .b/.w:    keep
                            #   .c/.x:    keep
                            #   .d/.y:    keep
                            #   .e/.z:    unknown
                            #
                            z = t.z.sanitize()

                            if z is 0:
                                a     = t.a
                                b     = t.b
                                c     = t.c
                                d     = t.d
                                index = 4
                            else:
                                e6 = t.e6
                                if e6 is absent:
                                    t.v = v
                                    t.w = w
                                    t.x = x
                                    t.y = y
                                    t.z = z
                                    return t

                                #
                                #   .a /.v :  keep
                                #   .b /.w :  keep
                                #   .c /.x :  keep
                                #   .d /.y :  keep
                                #   .e /.z :  keep
                                #   .e6/.z6:  unknown
                                #
                                z6 = t.z6.sanitize()

                                if z6 is 0:
                                    a     = t.a
                                    b     = t.b
                                    c     = t.c
                                    d     = t.d
                                    e     = t.e
                                    index = 5
                                else:
                                    t.v  = v
                                    t.w  = w
                                    t.x  = x
                                    t.y  = y
                                    t.z  = z
                                    t.z6 = z6

                                    if t.e7 is absent:
                                        return t

                                    #
                                    #   .a /.v :  keep
                                    #   .b /.w :  keep
                                    #   .c /.x :  keep
                                    #   .d /.y :  keep
                                    #   .e /.z :  keep
                                    #   .e6/.z6:  keep
                                    #   .e7/.z7:  unknown
                                    #
                                    z7 = t.z7.sanitize()

                                    if z7 is 0:
                                        t.e7 = absent
                                        del t.z7
                                        return t

                                    t.z7 = z7
                                    return t

            #
            #   At this point:
            #
            #       index is 0:
            #               Ignore .a/.v
            #               Ignore .b/.w
            #               Examination from .c/.x
            #
            #       index is 1
            #               keep either   .a/v or .b/w
            #               ignore either .a/v or .b/w
            #               Examination from .c/.x
            #
            #       index is 2:
            #               keep   .a/.v
            #               keep   .b/.w
            #               ignore .c/.x
            #               Examination from .d/.y
            #
            #       index is 3:
            #               keep   .a/.v
            #               keep   .b/.w
            #               keep   .c/.x
            #               ignore .d/.y
            #               Examination from .e/.z
            #
            #       index is 4:
            #               keep   .a/.v
            #               keep   .b/.w
            #               keep   .c/.x
            #               keep   .d/.y
            #               ignore .e/.z
            #               Examination from .e6/.z6
            #
            #       index is 5:
            #               keep   .a /.v
            #               keep   .b /.w
            #               keep   .c /.x
            #               keep   .d /.y
            #               keep   .e /.z
            #               ignore .e6/.z6
            #               Examination from .e7/.z7
            #

            #
            #   .a/.v:  keep or sanitize
            #   .b/.w:  unknown (unless index >= 1)
            #
            #   The following is done above (see comments there):
            #
            #       if index is 0:
            #           v = t.w.sanitize()
            #           if v is not 0:
            #               a     = t.b
            #               index = 1
            #

            #
            #   .a/.v:  keep or sanitize
            #   .v/.w:  keep or sanitize
            #   .c/.x:  unknown (unless index >= 2)
            #
            if index is 0:
                v = t.x.sanitize()

                if v is not 0:
                    a     = t.c
                    index = 1
            elif index is 1:
                w = t.x.sanitize()

                if w is not 0:
                    b     = t.c
                    index = 2


            #
            #   .a/.v:  keep or sanitize
            #   .v/.w:  keep or sanitize
            #   .c/.x:  keep or sanitize
            #   .d/.y:  unknown (unless index >= 3)
            #
            if index is 0:
                v = t.y.sanitize()

                if v is not 0:
                    a     = t.d
                    index = 1
            elif index is 1:
                w = t.y.sanitize()

                if w is not 0:
                    b     = t.d
                    index = 2
            elif index is 2:
                x = t.y.sanitize()

                if x is not 0:
                    c     = t.d
                    index = 3

            #
            #   .a/.v:  keep or sanitize
            #   .v/.w:  keep or sanitize
            #   .c/.x:  keep or sanitize
            #   .d/.y:  keep or sanitize
            #   .e/.z:  unknown (unless index >= 4)
            #
            if t.e is absent:
                if index is 0:  return 0
                if index is 1:  return v
                if index is 2:  return create_herd_2(a, b, v, w)

                assert index is 3

                return create_herd_3(a, b, c, v, w, x)

            if index is 0:
                v = t.z.sanitize()

                if v is not 0:
                    a     = t.e
                    index = 1
            elif index is 1:
                w = t.z.sanitize()

                if w is not 0:
                    b     = t.e
                    index = 2
            elif index is 2:
                x = t.z.sanitize()

                if x is not 0:
                    c     = t.e
                    index = 3
            elif index is 3:
                y = t.z.sanitize()

                if y is not 0:
                    d     = t.e
                    index = 4

            #
            #   .a /.v :    keep or sanitize
            #   .v /.w :    keep or sanitize
            #   .c /.x :    keep or sanitize
            #   .d /.y :    keep or sanitize
            #   .e /.z :    keep or sanitize
            #   .e6/.z6:    unknown (unless index >= 5)
            #
            if t.e6 is absent:
                if index is 0:  return 0
                if index is 1:  return v
                if index is 2:  return create_herd_2(a, b, v, w)
                if index is 3:  return create_herd_3(a, b, c, v, w, x)

                assert index is 4

                t.a = a
                t.b = b
                t.c = c
                t.d = d

                t.v = v
                t.w = w
                t.x = x
                t.y = y

                t.e = absent
                del t.z

                return t

            if index is 0:
                v = t.z6.sanitize()

                if v is not 0:
                    a     = t.e6
                    index = 1
            elif index is 1:
                w = t.z6.sanitize()

                if w is not 0:
                    b     = t.e6
                    index = 2
            elif index is 2:
                x = t.z6.sanitize()

                if x is not 0:
                    c     = t.e6
                    index = 3
            elif index is 3:
                y = t.z6.sanitize()

                if y is not 0:
                    d     = t.e6
                    index = 4
            elif index is 4:
                z = t.z6.sanitize()

                if z is not 0:
                    e     = t.e6
                    index = 5
            else:
                assert index is 5

            #
            #   .a /.v :    keep or sanitize
            #   .v /.w :    keep or sanitize
            #   .c /.x :    keep or sanitize
            #   .d /.y :    keep or sanitize
            #   .e /.z :    keep or sanitize
            #   .e6/.z6:    keep or sanitize
            #   .e7/.z7:    unknown
            #
            if t.e7 is absent:
                if index is 0:  return 0
                if index is 1:  return v
                if index is 2:  return create_herd_2(a, b, v, w)
                if index is 3:  return create_herd_3(a, b, c, v, w, x)

                t.a = a
                t.b = b
                t.c = c
                t.d = d

                t.v = v
                t.w = w
                t.x = x
                t.y = y

                if index is 4:
                    t.e = absent
                    del t.z, t.z6
                    return t

                assert index is 5

                t.e = e
                t.z = z

                t.e6 = absent
                del t.z6
                return t

            if index is 0:
                return t.z7.sanitize()

            if index is 1:
                w = t.z7.sanitize()

                if w is 0:
                    return v

                return create_herd_2(a, t.e7, v, w)

            if index is 2:
                x = t.z7.sanitize()

                if x is 0:
                    return create_herd_2(a, b, v, w)

                return create_herd_3(a, b, t.e7, v, w, x)

            if index is 3:
                y = t.z7.sanitize()

                if y is 0:
                    return create_herd_3(a, b, c, v, w, x)

                t.a = a
                t.b = b
                t.c = c
                t.d = t.e7

                t.v = v
                t.w = w
                t.x = x
                t.y = y

                t.e = absent
                del t.z, t.z6, t.z7

                return t

            t.a = a
            t.b = b
            t.c = c
            t.d = d

            t.v = v
            t.w = w
            t.x = x
            t.y = y

            if index is 4:
                z = t.z7.sanitize()

                if z is 0:
                    t.e = absent
                    del t.z, t.z6, t.z7
                    return t

                t.e = t.e7
                t.z = z

                t.e6 = absent
                del t.z6, t.z7
                return t

            assert index is 5

            t.e = e
            t.z = z

            z6 = t.z7.sanitize()

            if z6 is 0:
                t.e6 = absent
                del t.z6, t.z7
                return t

            t.e6 = t.e7
            t.z6 = z6

            t.e7 = absent
            del t.z7
            return t


    class Herd_Many(Map):
        __slots__ = (())


        is_herd      = true
        is_herd_many = true
        k1           = absent
        k2           = absent
        k3           = absent
        skip         = 0


        count_nested = count_nested__map


        if __debug__:
            def displace(t, k, v):
                assert k in t

                t[k] = v
        else:
            displace = map__store


        glimpse = map__lookup
        lookup  = map__lookup


        def inject(t, k, v):
            assert map__lookup(t, k) is none

            map__store(t, k, v)
            return t


        insert              = inject
        items_sorted_by_key = items_sorted_by_key__herd_many


        def provision(t, k, v):
            map__provide(t, k, v)
            return t


        def provision_dual(t, _displace, Meta, k1, k2):
            return (map__lookup(t, k2)) or (map__provide(t, k2, Meta(k1, k2)))


        def provision_dual__21(t, _displace, Meta, k1, k2):
            return (map__lookup(t, k1)) or (map__provide(t, k1, Meta(k1, k2)))


        def provision_triple(t, displace, Meta, k1, k2, k3):
            second = map__lookup(t, k2, absent)

            if second.k3 is k3:
                return second

            if not second.is_herd:
                r = Meta(k1, k2, k3)

                if second is absent:
                    return map__provide(t, k2, r)

                map__store(t, k2, create_herd_2(second.k3, k3, second, r))

                return r

            return second.provision_triple_step2(map__store, t, Meta, k1, k2, k3)


        def provision_triple__312(t, displace, Meta, k1, k2, k3):
            second = map__lookup(t, k1, absent)

            if second.k2 is k2:
                return second

            if not second.is_herd:
                r = Meta(k1, k2, k3)

                if second is absent:
                    return map__provide(t, k1, r)

                map__store(t, k1, create_herd_2(second.k2, k2, second, r))

                return r

            return second.provision_triple_step2__312(map__store, t, Meta, k1, k2, k3)


        def provision_triple_step2(t, _displace, _parent, Meta, k1, k2, k3):
            return (map__lookup(t, k3)) or (map__provide(t, k3, Meta(k1, k2, k3)))


        def provision_triple_step2__312(t, _displace, _parent, Meta, k1, k2, k3):
            return (map__lookup(t, k2)) or (map__provide(t, k2, Meta(k1, k2, k3)))


    empty_herd = Herd_0()


    new_Herd_1    = Method(Object.__new__, Herd_1)
    new_Herd_2    = Method(Object.__new__, Herd_2)
    new_Herd_3    = Method(Object.__new__, Herd_3)
    new_Herd_4567 = Method(Object.__new__, Herd_4567)
    new_Herd_Many = Method(Map   .__new__, Herd_Many)


    @export
    def create_herd_1(a, v):
        assert a is not absent

        t = new_Herd_1()

        t.a = a
        t.v = v

        return t


    @export
    def create_herd_2(a, b, v, w):
        assert (a is not absent) and (a is not b) and (b is not absent)

        t = new_Herd_2()

        t.a = a
        t.b = b
        t.v = v
        t.w = w

        return t


    def create_herd_3(a, b, c, v, w, x):
        assert (a is not absent) and (a is not b) and (a is not c)
        assert (b is not absent) and (b is not c)
        assert (c is not absent)

        t = new_Herd_3()

        t.a = a
        t.b = b
        t.c = c
        t.v = v
        t.w = w
        t.x = x

        return t


    @share
    def create_herd_4567(a, b, c, d, v, w, x, y):
        assert (a is not absent) and (a is not b) and (a is not c) and (a is not d)
        assert (b is not absent) and (b is not c) and (b is not d)
        assert (c is not absent) and (c is not d)
        assert d is not absent

        t = new_Herd_4567()

        t.a = a
        t.b = b
        t.c = c
        t.d = d
        t.e = absent
        t.v = v
        t.w = w
        t.x = x
        t.y = y

        return t


    def create_herd_many(a, b, c, d, e, e6, e7, e8, v, w, x, y, z, z6, z7, z8):
        assert (a is not absent) and (a is not b) and (a is not c) and (a is not d) and (a is not e)
        assert (a is not e6) and (a is not e7) and (a is not e8)
        assert (b is not absent) and (b is not c) and (b is not d) and (b is not e) and (b is not e6)
        assert (b is not e7) and (b is not e8)
        assert (c is not absent) and (c is not d) and (c is not e) and (c is not e6) and (c is not e7)
        assert (c is not e8)
        assert (d is not absent) and (d is not e) and (d is not e6) and (d is not e7) and (d is not e8)
        assert (e is not absent) and (e is not e6) and (e is not e7) and (e is not e8)
        assert (e6 is not absent) and (e6 is not e7) and (e6 is not e8)
        assert (e7 is not absent) and (e7 is not e8)
        assert e8 is not absent

        t = new_Herd_Many()

        t[a]  = v
        t[b]  = w
        t[c]  = x
        t[d]  = y
        t[e]  = z
        t[e6] = z6
        t[e7] = z7
        t[e8] = z8

        return t


    displace_1v  = Herd_1   .v .__set__
    displace_2v  = Herd_2   .v .__set__
    displace_2w  = Herd_2   .w .__set__
    displace_3v  = Herd_3   .v .__set__
    displace_3w  = Herd_3   .w .__set__
    displace_3x  = Herd_3   .x .__set__
    displace_4v  = Herd_4567.v .__set__
    displace_4w  = Herd_4567.w .__set__
    displace_4x  = Herd_4567.x .__set__
    displace_4y  = Herd_4567.y .__set__
    displace_4z  = Herd_4567.z .__set__
    displace_4z6 = Herd_4567.z6.__set__
    displace_4z7 = Herd_4567.z7.__set__


    Herd_0.provision = Herd_0.provide = Herd_0.inject = HerHerdrt = static_method(create_herd_1)

    export(
        'empty_herd',      empty_herd
    )
