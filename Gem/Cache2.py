#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Gem.Cache2')
def gem():
    require_gem('Gem.Absent')
    require_gem('Gem.Horde')


    map__get     = Map.get
    map__provide = Map.setdefault
    map__store   = Map.__setitem__


    class LiquidMap(Map):
        __slots__ = (())


        def items_sorted_by_key(t):
            value = t.__getitem__

            for k in sorted_list(t):
                yield (( k, value(k) ))


        lookup  = map__get
        provide = map__provide
        store   = map__store


    class LiquidMap_WithNub(Map):
        __slots__ = ((
            'nub',                              #   Method
        ))


        def __init__(t, nub):
            t.nub = nub


        def items_sorted_by_key(t):
            value = t.__getitem__

            for k in sorted_list(t, key = t.nub):
                yield (( k, value(k) ))


        lookup  = map__get
        provide = map__provide
        store   = map__store


    cache_names   = LiquidMap()                 #   Map String+ of Map
    lookup_cache  = cache_names.get
    provide_cache = cache_names.setdefault


    @export
    def produce_conjure_by_name__V2(
            name, Meta,

            cache = absent,
    ):
        if cache is absent:
            cache = create_cache(name)

        lookup  = cache.get
        provide = cache.setdefault


        def conjure_by_name(k):
            r = lookup(k)

            if r is not none:
                return r

            interned_k = intern_string(k)

            return provide(interned_k, Meta(interned_k))


        if __debug__:
           return rename_function(intern_arrange('conjure_%s', name), conjure_by_name)


        return conjure_by_name


    @export
    def produce_conjure_unique_dual(
            name,
            Meta,

            cache  = absent,
            lookup = absent,
            store  = absent,
            nub    = none,
    ):
        if cache is absent:
            cache = create_cache(name, nub = nub)

        if lookup is absent:
            lookup = cache.get

        if store is absent:
            store = cache.__setitem__


        def conjure_unique_dual(k1, k2):
            first = lookup(k1, absent)

            if first.k2 is k2:
                return first

            if not first.is_horde:
                r = Meta(k1, k2)

                store(k1, (r   if first is absent else   create_horde_23(first.k2, k2, first, r)))

                return r

            return first.provision2_k2(store, Meta, k1, k2)


        if __debug__:
            return rename_function(intern_arrange('conjure_%s', name), conjure_unique_dual)

        return conjure_unique_dual


    @export
    def produce_conjure_unique_dual__21(
            name,
            Meta,

            cache  = absent,
            lookup = absent,
            store  = absent,
            nub    = none,
    ):
        if cache is absent:
            cache = create_cache(name, nub = nub)

        if lookup is absent:
            lookup = cache.get

        if store is absent:
            store = cache.__setitem__


        def conjure_unique_dual__21(k1, k2):
            first = lookup(k2, absent)

            if first.k1 is k1:
                return first

            if not first.is_horde:
                r = Meta(k1, k2)

                store(k2, (r   if first is absent else   create_horde_23(first.k1, k1, first, r)))

                return r

            return first.provision2_k1(store, Meta, k1, k2)


        if __debug__:
            return rename_function(intern_arrange('conjure_%s__21', name), conjure_unique_dual__21)

        return conjure_unique_dual__21


    @export
    def produce_conjure_unique_triple(
            name,
            Meta,

            cache  = absent,
            lookup = absent,
            store  = absent,
            nub    = none,
    ):
        if cache is absent:
            cache = create_cache(name, nub = nub)

        if lookup is absent:
            lookup = cache.get

        if store is absent:
            store = cache.__setitem__


        def conjure_unique_triple(k1, k2, k3):
            first = lookup(k1, absent)

            if first.k2 is k2:
                if first.k3 is k3:
                    return first

                r = Meta(k1, k2, k3)

                store(k1, create_horde_1(k2, create_horde_23(first.k3, k3, first, r)))

                return r

            if not first.is_horde:
                r = Meta(k1, k2, k3)

                store(k1, (r   if first is absent else   create_horde_23(first.k2, k2, first, r)))

                return r

            skip = first.skip

            if skip is 0:
                second = first.glimpse(k2, absent)

                if second.k3 is k3:
                    return second

                if not second.is_horde:
                    r = Meta(k1, k2, k3)

                    if second is absent:
                        first.insert(k2, r)
                    else:
                        first.displace(k2, conjure_horde_23(second.k3, k3, second, r))

                    return r

                r = second.glimpse(k3)

                if r is not none:
                    assert r.k3 is k3

                    return r

                r = Meta(k1, k2, k3)

                second__2 = second.insert(k3, r)

                if second is not second__2:
                    first.displace(k1, second__2)

                return r

            if skip is k2:
                r = first.glimpse(k3)

                if r is not none:
                    assert (r.k2 is k2) and (r.k3 is k3)

                    return r

                r = Meta(k1, k2, k3)

                first__2 = first.insert(k3, r)

                if first is not first__2:
                    assert first__2.skip is k2

                    store(k1, first__2)

                return r

            r = Meta(k1, k2, k3)

            store(k1, create_horde_23(skip, k2, first.remove_skip(), r))

            return r


        if __debug__:
            return rename_function(intern_arrange('conjure_%s', name), conjure_unique_triple)

        return conjure_unique_triple


    @export
    def create_cache(name, nub = none):
        assert name not in cache_names

        return provide_cache(
                   intern_string(name),
                   (LiquidMap()   if nub is none else   LiquidMap_WithNub(nub)),
               )


    if __debug__:
        def dump_single_cache(name, cache):
            line('===  %s  ===', name)

            for [k, v] in cache.items_sorted_by_key():
                if not v.is_horde:
                    line('%s: %s',
                         (
                            portray_string(k)  if k.__class__ is String  else
                            k                  if k.__class__ is Integer else
                            k.display_token()
                         ),
                         v.display_token())

                    continue

                line('%s:',
                     (
                        portray_string(k)  if k.__class__ is String  else
                        k                  if k.__class__ is Integer else
                        k.display_token()
                     ))

                for [k2, w] in v.items_sorted_by_key():
                    if not w.is_horde:
                        line('  %s: %s',
                             (
                                portray_string(k2)  if k2.__class__ is String  else
                                k2                  if k2.__class__ is Integer else
                                k2.display_token()
                             ),
                             w.display_token())

                        continue

                    line('  %s:',
                         (
                            portray_string(k2)  if k2.__class__ is String  else
                            k2                  if k2.__class__ is Integer else
                            k2.display_token()
                         ))

                    for [k3, x] in w.items_sorted_by_key():
                        if not x.is_horde:
                            line('    %s: %s', k3.display_token(), x.display_token())
                            continue

                        line('    %s:', k3.display_token())

                        for [k4, y] in x.items_sorted_by_key():
                            line('      %s:', k4.display_token())
                            line('        %s', y.display_token())

        @export
        def dump_caches(use_name = none):
            if use_name is none:
                line('Total caches: %d', length(cache_names))

                for [name, cache] in cache_names.items_sorted_by_key():
                    line('%s: %d', name, length(cache))

                return

            dump_single_cache(use_name, cache_names[use_name])
    else:
        @export
        def dump_caches(use_name = none):
            pass
