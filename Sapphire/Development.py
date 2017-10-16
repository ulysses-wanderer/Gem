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
    empty_indentation__function = conjure_indented_token(empty_indentation, FUNCTION__W)

    #def gem():
    gem__function_header = conjure_function_header(
                               empty_indentation__function,
                               conjure_name('gem'),
                               conjure_parameters_0(LP, RP),
                               COLON__LINE_MARKER,
                           )


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


    class RequireMany(Object):
        __slots__ = ((
            'vary',                     #   SapphireTransform
            'vary_total',               #   Integer

            'latest_many',              #   List of String
            '_append_latest',           #   Method

            'twig_many',                #   List of Twig
            '_append_twig',             #   Method

            'processed_set',            #   LiquidSet of String
            '_add_processed',           #   Method
            '_contains_processed',      #   Method
        ))


        def __init__(t, vary, vary_total):
            t.vary       = vary
            t.vary_total = vary_total

            t.latest_many    = many        = []
            t._append_latest = many.append

            t.twig_many    = many        = []
            t._append_twig = many.append

            t.processed_set       = processed = LiquidSet()
            t._add_processed      = processed.add
            t._contains_processed = processed.__contains__

            #
            #   Ignore these file, pretend we already saw them
            #
            t._add_processed('Gem.Path2')
            t._add_processed('Sapphire.Boot')
            t._add_processed('Sapphire.Parse2')


        def add_require_gem(t, module_name):
            assert module_name.is_single_quote

            s = module_name.s[1:-1]

            if t._contains_processed(s):
                return

            t._append_latest(s)


        def loop(t):
            contains_processed = t._contains_processed
            latest_many        = t.latest_many
            process_module     = t.process_module

            append_latest = t._append_latest
            extend_latest = latest_many.extend
            length_latest = latest_many.__len__
            index_latest  = latest_many.__getitem__
            delete_latest = latest_many.__delitem__

            index_latest_0  = Method(index_latest, 0)
            index_latest_1  = Method(index_latest, 1)
            delete_latest_0 = Method(delete_latest, 0)
            zap_latest      = Method(delete_latest, slice_all)

            while 7 is 7:
                total = length_latest()

                if total is 0:
                    break

                first = index_latest_0()

                if contains_processed(first):
                    #line('Already processed %s', first)
                    delete_latest_0()
                    continue

                #line('Total %d - Process %s', total, first)

                if total is 1:
                    zap_latest()
                    process_module(first)
                    continue

                if total is 2:
                    other = index_latest_1()
                    zap_latest()
                    process_module(first)
                    append_latest(other)
                    continue

                other = t.latest_many[1:]
                zap_latest()
                process_module(first)
                extend_latest(other)


        def process_module(t, module):
            t._add_processed(module)

            path = path_join('..', arrange('%s.py', module.replace('.', '/')))

            vary_total = t.vary_total

            if vary_total is not 0:
                vary         = t.vary
                t.vary_total = vary_total -1
            else:
                vary = 0

            gem = extract_gem(module, path, vary)

            t._append_twig(gem)

            gem.twig.find_require_gem(t)


    def conjure_gem_decorator_header(module):
        #@gem('Gem.Something')
        return conjure_decorator_header(
                   empty_indentation__at_sign,
                   conjure_call_expression(
                       conjure_name('gem'),
                       conjure_arguments_1(LP, conjure_single_quote(portray(module)), RP),
                   ),
                   LINE_MARKER,
               )

    def extract_boot(path, tree, index, copyright, vary):
        boot_code = tree[index]

        #@boot('Boot')
        boot_code__decorator_header = conjure_decorator_header(
                                          empty_indentation__at_sign,
                                          conjure_call_expression(
                                              conjure_name('boot'),
                                              conjure_arguments_1(LP, conjure_single_quote("'Boot'"), RP),
                                          ),
                                          LINE_MARKER,
                                      )

        assert boot_code.is_decorated_definition
        assert boot_code.a is boot_code__decorator_header

        if vary:
            boot_code = boot_code.transform(vary)

        return TwigCode(path, arrange('[%d]', index), extract_copyright(tree), boot_code)


    def extract_boot_decorator(function_name, path, tree, copyright, vary = 0):
        boot_decorator = tree[0]

        #def boot(module_name):
        boot_decorator__function_header = conjure_function_header(
                                              empty_indentation__function,
                                              conjure_name(function_name),
                                              conjure_parameters_1(LP, conjure_name('module_name'), RP),
                                              COLON__LINE_MARKER,
                                          )

        assert boot_decorator.is_function_definition
        assert boot_decorator.a is boot_decorator__function_header
        assert boot_decorator.b.is_statement_suite

        if vary is not 0:
            boot_decorator = boot_decorator.transform(vary)

        return TwigCode(path, '[0]', copyright, boot_decorator)


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


    def extract_gem(module, path, vary):
        tree = parse_python(path)

        assert length(tree) is 1

        copyright = extract_copyright(tree)

        gem = tree[0]

        assert gem.is_decorated_definition
        assert gem.a is conjure_gem_decorator_header(module)
        assert gem.b.is_function_definition
        assert gem.b.a is gem__function_header

        if vary is not 0:
            line('Varying %s', path)
            gem = gem.transform(vary)

        return TwigCode(path, '[0]', copyright, gem)


    def extract_sardnoyx_boot(vary):
        path = '../Sardonyx/Boot.py'

        tree = parse_python(path)

        assert length(tree) is 1

        return extract_boot(path, tree, 0, extract_copyright(tree), vary)


    def extract_gem_boot(vary):
        module_name = 'Gem.Boot'
        path        = '../Gem/Boot.py'

        tree = parse_python(path)

        assert length(tree) is 3

        copyright = extract_copyright(tree)

        #
        #    [0]
        #       def boot(module_name):
        #           ...
        #
        boot_decorator = extract_boot_decorator('gem', path, tree, copyright)

        del boot_decorator  #   We don't really want this, but just extracted it for testing purposes

        #
        #   [1]: empty lines
        #
        assert tree[1].is_empty_line_suite

        #
        #   [2]:
        #       @gem('Gem.Boot')
        #       def gem():
        #           ...
        #
        gem = tree[2]

        assert gem.is_decorated_definition
        assert gem.a is conjure_gem_decorator_header(module_name)
        assert gem.b.is_function_definition
        assert gem.b.a is gem__function_header
        assert gem.b.b.is_statement_suite

        if (vary is not 0) and 7:
            gem = gem.transform(vary)

        return TwigCode(path, '[2]', copyright, gem)


    def extract_sapphire_main(vary):
        module_name = 'Sapphire.Main'
        path        = '../Sapphire/Main.py'

        tree = parse_python(path)

        assert length(tree) is 5

        copyright = extract_copyright(tree)


        #
        #   [0]:
        #       def boot(module_name):
        #           ...
        #
        boot_decorator = extract_boot_decorator('boot', path, tree, copyright, vary)


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
        boot = extract_boot(path, tree, 2, copyright, vary)

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

        assert main.is_decorated_definition
        assert main.a is conjure_gem_decorator_header(module_name)
        assert main.b.is_function_definition
        assert main.b.a is gem__function_header
        assert main.b.b.is_statement_suite


        #
        #   Result
        #
        if vary is not 0:
            main = main.transform(vary)

        return ((
                   boot_decorator,
                   TwigCode(path, '[4]', copyright, main),
               ))


    @share
    def development(module_name, vary):
        [boot_decorator, main_code] = extract_sapphire_main(vary)
        sardnoyx_boot_code          = extract_sardnoyx_boot(vary)
        gem_boot_code               = extract_gem_boot(vary)

        require_many = RequireMany(vary, 27)

        require_many.process_module('Gem.Core')
        main_code.twig.find_require_gem(require_many)
        require_many.loop()

        output_path = arrange('../bin/.pyxie/%s.py', module_name)

        with create_DelayedFileOutput(output_path) as f:
            boot_decorator    .write(f)
            sardnoyx_boot_code.write(f)

            for v in require_many.twig_many:
                v.write(f)

            gem_boot_code.write(f)
            main_code    .write(f)

            close_copyright(f)

        #partial(read_text_from_path(output_path))
