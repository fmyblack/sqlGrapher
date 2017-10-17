from HqlVisitor import HqlVisitor

class VisitorImpl(HqlVisitor):

    def visitJoin_sql(self, ctx):
        join = {}
        join[ctx.FIELD()[0].getText()] = self.visit(ctx.sql(0))
        join[ctx.FIELD()[1].getText()] = self.visit(ctx.sql(1))
        return join

    def visitDerect_sql(self, ctx):
        return self.visitChildren(ctx)

    def visitSingle_sql(self, ctx):
        return ctx.FIELD().getText()