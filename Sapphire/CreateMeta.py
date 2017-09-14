#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.CreateMeta')
def gem():
    @share
    def create_Meta_WithNewlines(Meta, constructor):
        r = Meta.Meta_WithNewlines = Type(
                                         arrange('%sWithNewline', Meta.__name__),
                                         ((Meta,)),
                                         {
                                             '__slots__' : ((
                                                 'newlines',                 #   Integer { > 0 }
                                                 'ends_in_newline',          #   Boolean
                                             )),

                                             '__init__' : constructor,
                                         },
                                     )

        return r


    @share
    def create_Meta_Many(Meta, constructor):
        r = Meta.Meta_Many = Type(
                                 arrange('%s_Many', Meta.__name__),
                                 ((Meta,)),
                                 {
                                     '__slots__' : ((
                                         'newlines',                 #   Integer { > 1 }
                                     )),

                                     '__init__' : constructor
                                 },
                             )

        return r
