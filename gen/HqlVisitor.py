# Generated from /Users/fmyblack/pythonproject/hql_grapher/grammer/Hql.g4 by ANTLR 4.7
from antlr4 import *

# This class defines a complete generic visitor for a parse tree produced by HqlParser.

class HqlVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by HqlParser#join_sql.
    def visitJoin_sql(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HqlParser#derect_sql.
    def visitDerect_sql(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HqlParser#single_sql.
    def visitSingle_sql(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HqlParser#where_stat.
    def visitWhere_stat(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HqlParser#group_stat.
    def visitGroup_stat(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HqlParser#join_stat.
    def visitJoin_stat(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HqlParser#cmp_stat.
    def visitCmp_stat(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HqlParser#select_stat.
    def visitSelect_stat(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HqlParser#fuction_stat.
    def visitFuction_stat(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HqlParser#if_stat.
    def visitIf_stat(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HqlParser#minus_stat.
    def visitMinus_stat(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HqlParser#value_stat.
    def visitValue_stat(self, ctx):
        return self.visitChildren(ctx)


