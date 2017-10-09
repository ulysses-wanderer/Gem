#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Development')
def gem():
    require_gem('Sapphire.Parse')

    variables = [
                    0,                  #   0 = copyright
                ]

    query = variables.__getitem__
    write = variables.__setitem__

    qc = Method(query, 0)
    wc = Method(write, 0)

    wc0 = Method(wc, 0)


    #
    #   Tokens
    #
    LP = conjure_left_parenthesis ('(')
    RP = conjure_right_parenthesis(')')

    empty_indentation__function = conjure_indented_token( empty_indentation, conjure_keyword_function('def '))


    class Copyright(Object):
        __slots__ = ((
            'year',                     #   Integer
            'author',                   #   String+
        ))


        def __init__(t, year, author):
            t.year   = year
            t.author = author


        def write(t, f):
            copyright = qc()

            if t is not copyright:
                if copyright is not 0:
                    close_copyright(f)

                wc(t)

                f.blank2()
                f.line('#<Copyright (c) %d %s.  All rights reserved.>', t.year, t.author)
                f.blank_suppress()


    Copyright.k1 = Copyright.year
    Copyright.k2 = Copyright.author


    copyright_cache = {}

    conjure_copyright__X__dual = produce_conjure_dual('copyright', Copyright, copyright_cache)


    def conjure_copyright(year, author):
        return conjure_copyright__X__dual(intern_integer(year), intern_string(author))


    def close_copyright(f):
        if qc() is not 0:
            wc0()

            f.blank_suppress()
            f.line('#</Copyright>')
            f.blank2()


    class TwigCode(Object):
        __slots__ = ((
            'path',                     #   String+
            'part',                     #   String
            'copyright',                #   Copyright
            'twig',                     #   Any
        ))


        def __init__(t, path, part, copyright, twig):
            t.path      = path
            t.part      = part
            t.copyright = copyright
            t.twig      = twig


        def write(t, f):
            t.copyright.write(f)

            f.blank2()
            f.line(arrange("#<source %r %s>", t.path, t.part))
            t.twig.write(f.write)
            f.line('#</source>')
            f.blank2()


    def extract_boot(path, tree, index, copyright):
        boot_code = tree[index]

        #@boot('Boot')
        boot_code__decorator_header = conjure_decorator_header(
                                          empty_indentation__at_sign,
                                          conjure_call_expression(
                                              conjure_name('boot'),
                                              conjure_arguments_1(LP, conjure_single_quote("'Boot'"), RP),
                                          ),
                                          empty_line_marker,
                                      )

        assert boot_code.is_decorated_definition
        assert boot_code.a is boot_code__decorator_header

        return TwigCode(path, arrange('[%d]', index), extract_copyright(tree), boot_code)


    def extract_copyright(tree):
        copyright = tree[0].prefix

        assert copyright.is_comment_suite
        assert length(copyright) is 3
        assert copyright[0] == empty_comment_line
        assert copyright[1].is_comment_line
        assert copyright[2] == empty_comment_line

        m = copyright_match(copyright[1])

        if m is none:
            raise_runtime_error('failed to extract copyright from: %r', copyright[1])

        return conjure_copyright(Integer(m.group('year')), m.group('author'))


    def extract_sardnoyx_boot():
        path = '../Sardonyx/Boot.py'

        tree = parse_python(path)

        assert length(tree) is 1

        return ((
                   extract_boot(path, tree, 0, extract_copyright(tree)),
               ))


    def extract_sapphire_main():
        path = '../Sapphire/Main.py'

        tree = parse_python(path)

        assert length(tree) is 5

        copyright = extract_copyright(tree)


        #
        #   [0]:
        #       def boot(module_name):
        #           ...
        #
        boot_decorator = tree[0]

        #def boot(module_name):
        boot_decorator__function_header = conjure_function_header(
                                              empty_indentation__function,
                                              conjure_name('boot'),
                                              conjure_parameters_1(LP, conjure_name('module_name'), RP),
                                              colon__empty_line_marker,
                                          )

        assert boot_decorator.is_function_definition
        assert boot_decorator.a is boot_decorator__function_header
        assert boot_decorator.b.is_statement_suite


        #
        #   [1]: empty lines
        #
        assert tree[1].is_empty_line_suite


        #
        #   [2]:
        #       @boot('Boot')
        #       def boot():
        #           ...
        #
        boot = extract_boot(path, tree, 2, copyright)

        del boot        #   We don't really want this, but just extracted it for testing purposes


        #
        #   [3]
        #
        assert tree[3].is_empty_line_suite


        #
        #   [4]:
        #       @gem('Sapphire.Main')
        #       def gem():
        #           ...
        #
        main = tree[4]

        #@gem('Sapphire.Main')
        main__decorator_header = conjure_decorator_header(
                                    empty_indentation__at_sign,
                                    conjure_call_expression(
                                        conjure_name('gem'),
                                        conjure_arguments_1(LP, conjure_single_quote("'Sapphire.Main'"), RP),
                                    ),
                                    empty_line_marker,
                                )

        #def gem():
        main__function_header = conjure_function_header(
                                    empty_indentation__function,
                                    conjure_name('gem'),
                                    conjure_parameters_0(LP, RP),
                                    colon__empty_line_marker,
                                )

        assert main.is_decorated_definition
        assert main.a is main__decorator_header
        assert main.b.is_function_definition
        assert main.b.a is main__function_header
        assert main.b.b.is_statement_suite


        #
        #   Result
        #
        return ((
                   TwigCode(path, '[0]', copyright, boot_decorator),
                   TwigCode(path, '[4]', copyright, main),
               ))



    @share
    def development():
        [boot_decorator, main_code] = extract_sapphire_main()
        [boot_code]                 = extract_sardnoyx_boot()


        output_path = '../bin/.pyxie/hma.py'

        with create_DelayedFileOutput(output_path) as f:
            boot_decorator.write(f)
            boot_code.write(f)
            main_code.write(f)

            close_copyright(f)

        #partial(read_text_from_path(output_path))
