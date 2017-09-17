#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.ActionWord')
def gem():
    require_gem('Sapphire.CreateMeta')
    require_gem('Sapphire.TokenCache')


    create_ActionWord_WithNewlines = Shared.create_ActionWord_WithNewlines       #   Due to 'privileged'
    lookup_adjusted_meta           = Shared.lookup_adjusted_meta                 #   Due to 'privileged'

    lookup_action_word  = lookup_normal_token
    provide_action_word = provide_normal_token


    action_word__Meta__cache = {}                   #   Map { String : Meta }

    find_action_word__Meta = action_word__Meta__cache.__getitem__


    def construct_token__with_newlines(t, s, newlines, ends_in_newline):
        t.s               = s
        t.newlines        = newlines
        t.ends_in_newline = ends_in_newline


    @share
    def conjure_action_word(full, s):
        assert s[-1] != '\n'

        r = lookup_action_word(s)

        if r is not none:
            return r

        s = intern_string(s)

        Meta     = find_action_word__Meta(full)
        newlines = s.count('\n')

        return provide_action_word(
                   s,
                   (
                       provide_action_word(s, Meta(s))
                           if newlines is 0 else
                               (
                                      lookup_adjusted_meta(Meta)
                                   or create_ActionWord_WithNewlines(Meta, construct_token__with_newlines)
                                )(s, newlines, false)
                   ),
               )


    @share
    def conjure_action_word__ends_in_newline(full, s):
        assert s[-1] == '\n'

        r = lookup_action_word(s)

        if r is not none:
            return r

        s = intern_string(s)

        Meta = find_action_word__Meta(full)

        return provide_action_word(
                   s,
                   (
                         lookup_adjusted_meta(Meta)
                      or create_ActionWord_WithNewlines(Meta, construct_token__with_newlines)
                   )(s, s.count('\n'), true)
               )


    @share
    def initialize_action_word__Meta(many):
        provide_action_word__Meta = action_word__Meta__cache.setdefault

        for [k, Meta] in many:
            provide_action_word__Meta(k, Meta)

        assert length(many) == length(action_word__Meta__cache)


    @share
    @privileged
    def produce_conjure_action_word(name, Meta, produce_ends_in_newline = false):
        assert type(name)                    is String
        assert type(Meta)                    is Type
        assert type(produce_ends_in_newline) is Boolean


        def conjure_action_word(s):
            assert s[-1] != '\n'

            r = lookup_action_word(s)

            if r is not none:
                return r

            s = intern_string(s)

            newlines = s.count('\n')

            return provide_action_word(
                       s,
                       (
                           Meta(s)
                               if newlines is 0 else
                                   (
                                         lookup_adjusted_meta(Meta)
                                      or create_ActionWord_WithNewlines(Meta, construct_token__with_newlines)
                                   )(s, newlines, false)
                       ),
                   )


        if __debug__:
            conjure_action_word.__name__ = intern_arrange('conjure_%s', name)


        if produce_ends_in_newline is false:
            return conjure_action_word


        def conjure_action_word__ends_in_newline(s):
            assert s[-1] == '\n'

            r = lookup_action_word(s)

            if r is not none:
                return r

            s = intern_string(s)

            return provide_action_word(
                       s,
                       (
                             lookup_adjusted_meta(Meta)
                          or create_ActionWord_WithNewlines(Meta, construct_token__with_newlines)
                       )(s, s.count('\n'), true)
                   )


        if __debug__:
            conjure_action_word__ends_in_newline.__name__ = intern_arrange('conjure_%s__ends_in_newline', name)

        return ((conjure_action_word, conjure_action_word__ends_in_newline))
