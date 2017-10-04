#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Parse3')
def gem():
    show = 7


    require_gem('Sapphire.BodyStatement')
    require_gem('Sapphire.DumpToken')
    require_gem('Sapphire.Suite')


    @share
    def parse3_python(path, data, data_lines, data_many):
        data_many.append(end_of_data)

        data_iterator = iterate(data_many)
        next_line     = next_method(data_iterator)

        tree_many   = []
        append_twig = tree_many.append

        variables = [
                        append_twig,        #   0 = append
                        0,                  #   1 = element
                        tree_many,          #   2 = many
                        0,                  #   3 = v
                    ]

        query = variables.__getitem__
        write = variables.__setitem__

        q_append  = Method(query, 0)
        q_element = Method(query, 1)
        q_many    = Method(query, 2)
        qv        = Method(query, 3)

        w_append  = Method(write, 0)
        w_element = Method(write, 1)
        w_many    = Method(write, 2)
        wv        = Method(write, 3)

        w_append_0  = Method(w_append,  0)
        w_element_0 = Method(w_element, 0)
        w_many_0    = Method(w_many,    0)
        wv0         = Method(wv,        0)


        def show_indentation():
            for v in data_many:
                line('+%d %s', v.indentation.total, v.display_token())


        def show_tree():
            with create_StringOutput() as f:
                f.line('===  show_tree  ===')

                for v in tree_many:
                    r = v.dump_token(f)

                    assert not r

            partial(f.result)


        def test_identical_output():
            with create_StringOutput() as f:
                w = f.write

                for v in tree_many:
                    v.write(w)

            if data != f.result:
                with create_DelayedFileOutput('oops.txt') as oops:
                    oops.write(f.result)

                raise_runtime_error('mismatch on %r: output saved in %r', path, 'oops.txt')

            line('Passed#1: Identical dump from parse tree.  Total: %d line%s',
                 length(data_many), (''   if length(data_many) is 0 else   's'))


        def test_count_newlines():
            total = 0

            for v in tree_many:
                v.is_statement                  #   Test this exists
                v.is_statement_header           #   Test this exists

                total += v.count_newlines()

            if total != length(data_lines):
                raise_runtime_error('mismatch on counted lines (counted: %d; expected: %d)',
                                    total, length(parse_context.data_lines))
                                
            line('Passed#2: Total counted lines %d matches input', total)


        def create_append():
            element = q_element()

            if element is none:
                many = []
            else:
                w_element_0()
                many = [element]

            append = many.append

            w_append(many)
            w_many(many)

            return append

 
        def parse_comments_or_empty_lines(first):
            v = qv()

            if v is 0:
                v = next_line()
            else:
                wv0()

            if not v.is_comment__or__empty_line:
                if (first.is_comment_line) and (not v.is_end_of_data):
                    return v.add_comment(first)

                raise_unknown_line()
                (q_append() or create_append())(first)
                return v

            raise_unknown_line()

            #
            #   mixed:        first element of mixed_many
            #   mixed_many:   multiple mixed
            #   indentation:  indentation of comments (or none if processing blank lines)
            #
            if v.is_comment_line:
                indentation = v.indentation

                if (first.is_comment_line) and (first.indentation is indentation):
                    comment_many = [first, v]

                    while 7 is 7:
                        v = next_line()

                        if v.is_comment_line:
                            if indentation is v.indentation:
                                comment_many.append(v)
                                continue

                            indentation = v.indentation
                            break

                        if v.is_empty_line:
                            indentation = none
                            break

                        if v.is_end_of_data:
                            (q_append() or create_append())(conjure_comment_suite(comment_many))
                            return v

                        return v.add_comment(conjure_comment_suite(comment_many))

                    mixed = conjure_comment_suite(comment_many)
                else:
                    mixed = first
            else:
                indentation = none

                if first.is_comment_line:
                    mixed = first
                else:
                    blank_many = [first, v]

                    while 7 is 7:
                        v = next_line()

                        if v.is_empty_line:
                            blank_many.append(v)
                            continue

                        if v.is_comment_line:
                            indentation = v.indentation
                            break

                        (q_append() or create_append())(conjure_empty_line_suite(empty_line_many))
                        return v

                    mixed = conjure_empty_line_suite(empty_line_many)

            mixed_many = none

            while 7 is 7:
                w = next_line()

                if not w.is_comment__or__empty_line:
                    if w.indentation is indentation:
                        if mixed_many is none:
                            (q_append() or create_append())(mixed)




        def parse_decorator_header(decorator_header):
            indentation = decorator_header.indentation

            v = qv()

            if v is 0:
                v = next_line()
            else:
                wv0()

            if v.is_comment__or__empty_line:
                if v.is_comment_line:
                    v = parse_comments_or_empty_lines(v)

                    if v.is_end_of_data:
                        raise_unknown_line()

                    v = v.add_comment(comment)
                else:
                    raise_unknown_line()

            if not v.is_class_decorator_or_function_header:
                raise_runtime_error('decorator_header must be followed by class, decorator, or function header: %r',
                                    decorator_header)

            if indentation is not v.indentation:
                raise_runtime_error('decorator_header (with indentation %d) followed by'
                                        + ' class, decorator, or function header with different indentation: %d',
                                    indentation.total,
                                    v.indentation.total)

            return conjure_decorated_definition(decorator_header, v.parse_header())


        def parse_function_header(function_header):
            return conjure_function_definition(function_header, parse_suite(function_header.indentation))


        def parse_lines():
            while 7 is 7:
                v = qv()

                if v is 0:
                    v = next_line()

                    if v.is_comment__or__empty_line:
                        if v.is_comment_line:
                            v = parse_comments_or_empty_lines(v)
                        else:
                            raise_unknown_line()
                    else:
                        if v.is_end_of_data:
                            wv(v)
                            break
                else:
                    if v.is_comment__or__empty_line:
                        if v.is_comment_line:
                            wv0()
                            v = parse_comments_or_empty_lines(v)
                        else:
                            raise_unknown_line()
                    else:
                        if v.is_end_of_data:
                            break


                if v.indentation.total != 0:
                    raise_runtime_error('unexpected indentation %d (expected 0): %r', v.indentation.total, v)

                if v.is_statement_header:
                    v = v.parse_header()
                else:
                    my_line('v: %r', v)
                    raise_unknown_line()

                #my_line('===  append  ===')
                #v.dump_token()

                append_twig(v)
            else:
                raise_runtime_error('programming error: loop to parse lines did not exit on %r', end_of_data)

            while 7 is 7:
                v = qv()

                if v is 0:
                    v = next_line()
                else:
                    wv0()

                if v.is_end_of_data:
                    break

                append_twig(v)
            else:
                raise_runtime_error('programming error: SECOND loop to parse lines did not exit on %r', end_of_data)


        def parse_suite(previous_indentation):
            previous_append  = q_append()
            previous_element = q_element()
            previous_many    = q_many()

            w_append_0()
            w_element_0()
            w_many_0()

            v = qv()

            if v is 0:
                v = next_line()
            else:
                wv0()

            if v.is_comment__or__empty_line:
                v = parse_comments_or_empty_lines(v)

            if v.is_end_of_data:
                raise_unknown_line()

            indentation = v.indentation

            if indentation.total <= previous_indentation.total:
                raise_runtime_error('missing indentation: %d (expected indentation greater than %d)',
                                    indentation.total, previous_indentation.total)

            if v.is_statement_header:
                v = v.parse_header()

            assert q_element() is 0

            append = q_append()

            if append is 0:
                w_element(v)
            else:
                append(v)

            while 7 is 7:
                w = qv()

                if w is 0:
                    w = next_line()
                else:
                    wv0()

                if w.is_comment__or__empty_line:
                    w = parse_comments_or_empty_lines(w)

                if w.is_end_of_data:
                    wv(w)

                    element = q_element()

                    if element is 0:
                        for v in q_many():
                            dump_token('many[?]', v)

                        raise_unknown_line()

                    assert q_append() is q_many() is 0

                    w_append (previous_append )
                    w_element(previous_element)
                    w_many   (previous_many   )

                    dump_token('suite result', v)

                    return v

                dump_token('v', v)
                dump_token('w', w)
                my_line('w: %r', w)

                raise_unknown_line()


        DecoratorHeader.parse_header = parse_decorator_header
        FunctionHeader .parse_header = parse_function_header


        if show is 5:
            show_indentation()

        parse_lines()
        test_identical_output()
        test_count_newlines()

        if show is 7:
            show_tree()

        #dump_caches('dual-twig')
