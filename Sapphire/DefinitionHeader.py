#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.DefinitionHeader')
def gem():
    require_gem('Sapphire.Tree')


    conjure_vw_frill            = Shared.conjure_vw_frill               #   due to privileged
    produce_conjure_triple__213 = Shared.produce_conjure_triple__213    #   due to privileged


    class DefinitionHeader(SapphireTrunk):
        __slots__ = ((
            'frill',                    #   XY_Frill | Commented_VW_Frill
            'name',                     #   String
            'parameters',               #   Parameter_0 | Parameter_1 | Parameter_Many
        ))


        is_any_else                           = false
        is_any_except_or_finally              = false
        is_class_decorator_or_function_header = true
        is_else_header_or_fragment            = false
        is_statement_header                   = true
        is_statement                          = false
        split_comment                         = 1


        def __init__(t, frill, name, parameters):
            t.frill      = frill
            t.name       = name
            t.parameters = parameters


        def  __repr__(t):
            return arrange('<%s %s %r %r>', t.__class__.__name__, t.frill, t.name, t.parameters)


        add_comment = 0


        def count_newlines(t):
            return t.frill.count_newlines() + t.name.count_newlines() + t.parameters.count_newlines()


        def display_token(t):
            frill          = t.frill
            indented_token = frill.v

            return arrange('<%s +%d %s %s %s %s>',
                           t                         .display_name,
                           indented_token.indentation.total,
                           indented_token.token      .display_token(),
                           t             .name       .display_token(),
                           t             .parameters .display_token(),
                           frill         .b          .display_token())



        def dump_token(t, f, newline = true):
            assert newline is true

            frill          = t.frill
            indented_token = frill.v

            f.partial('<%s +%d ', t.display_name, indented_token.indentation.total)

            indented_token.token     .dump_token(f)
            t             .name      .dump_token(f)
            t             .parameters.dump_token(f)
            r = frill     .w         .dump_token(f, false)

            return f.token_result(r, newline)


        @property
        def indentation(t):
            return t.frill.v.indentation

            
        def write(t, w):
            frill = t.frill

            w(frill.v.s + t.name.s)
            t.parameters.write(w)
            w(frill.w.s)


    DefinitionHeader.k1 = DefinitionHeader.frill
    DefinitionHeader.k2 = DefinitionHeader.name
    DefinitionHeader.k3 = DefinitionHeader.parameters


    @privileged
    def produce_conjure_definition_header(name, Meta):
        conjure_triple__312 = produce_conjure_triple__213(name, Meta)


        def conjure_definition_header(indented_keyword, name, parameters, colon_newline):
            return conjure_triple__312(
                       conjure_vw_frill(indented_keyword, colon_newline),
                       name,
                       parameters,
                   )


        if __debug__:
            conjure_definition_header.__name__ = intern_arrange('conjure_%s', name)

        return (( conjure_definition_header, static_method(conjure_triple__312) ))


    @share
    class ClassHeader(DefinitionHeader):
        __slots__    = (())
        display_name = 'class-header'


    @share
    class FunctionHeader(DefinitionHeader):
        __slots__          = (())
        display_name       = 'function-header'
        is_function_header = true


    [
        conjure_class_header, ClassHeader.conjure_with_frill,
    ] = produce_conjure_definition_header(
            'class-header',
            ClassHeader,
        )

    [
        conjure_function_header, FunctionHeader.conjure_with_frill,
    ] = produce_conjure_definition_header(
            'function-header',
            FunctionHeader,
        )


    FunctionHeader.conjure = static_method(conjure_function_header)


    share(
        'conjure_class_header',     conjure_class_header,
        'conjure_function_header',  conjure_function_header,
    )
