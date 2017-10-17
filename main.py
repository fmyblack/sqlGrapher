# coding: utf-8
#!/usr/bin/env python
import os
import sys
import pprint
from antlr4 import *
# from HqlLexer import HqlLexer
# from HqlParser import HqlParser
# from VisitorImpl import VisitorImpl
from gen import *

import test

def g(path):
    lexer = HqlLexer.HqlLexer(FileStream(path))
    token_stream = CommonTokenStream(lexer)
    parser = HqlParser.HqlParser(token_stream)
    tree = parser.sql()

    visitor = VisitorImpl.VisitorImpl()
    result = visitor.visit(tree)

    pp = pprint.PrettyPrinter(indent=4)
    # pp.pprint(result)
    # test.plotSubTree(result, None, 1, 0, 12)
    test.draw(result)

if __name__ == "__main__":
    g('/Users/fmyblack/Library/Application Support/Sublime Text 2/Packages/sqlGrapher/test.hql')
# listener = ListenerImpl()
# walker = ParseTreeWalker()
# walker.walk(listener, tree)
