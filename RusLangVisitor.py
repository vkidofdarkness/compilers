# Generated from RusLang.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .RusLangParser import RusLangParser
else:
    from RusLangParser import RusLangParser

# This class defines a complete generic visitor for a parse tree produced by RusLangParser.

class RusLangVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by RusLangParser#program.
    def visitProgram(self, ctx:RusLangParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RusLangParser#globalStatement.
    def visitGlobalStatement(self, ctx:RusLangParser.GlobalStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RusLangParser#varDeclaration.
    def visitVarDeclaration(self, ctx:RusLangParser.VarDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RusLangParser#varList.
    def visitVarList(self, ctx:RusLangParser.VarListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RusLangParser#statement.
    def visitStatement(self, ctx:RusLangParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RusLangParser#assignmentStatement.
    def visitAssignmentStatement(self, ctx:RusLangParser.AssignmentStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RusLangParser#printStatement.
    def visitPrintStatement(self, ctx:RusLangParser.PrintStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RusLangParser#ifStatement.
    def visitIfStatement(self, ctx:RusLangParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RusLangParser#иначеЕслиPart.
    def visitИначеЕслиPart(self, ctx:RusLangParser.ИначеЕслиPartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RusLangParser#иначеPart.
    def visitИначеPart(self, ctx:RusLangParser.ИначеPartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RusLangParser#whileStatement.
    def visitWhileStatement(self, ctx:RusLangParser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RusLangParser#blockStatement.
    def visitBlockStatement(self, ctx:RusLangParser.BlockStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RusLangParser#expr.
    def visitExpr(self, ctx:RusLangParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RusLangParser#orExpr.
    def visitOrExpr(self, ctx:RusLangParser.OrExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RusLangParser#andExpr.
    def visitAndExpr(self, ctx:RusLangParser.AndExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RusLangParser#equalityExpr.
    def visitEqualityExpr(self, ctx:RusLangParser.EqualityExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RusLangParser#relationalExpr.
    def visitRelationalExpr(self, ctx:RusLangParser.RelationalExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RusLangParser#additiveExpr.
    def visitAdditiveExpr(self, ctx:RusLangParser.AdditiveExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RusLangParser#multiplicativeExpr.
    def visitMultiplicativeExpr(self, ctx:RusLangParser.MultiplicativeExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RusLangParser#atom.
    def visitAtom(self, ctx:RusLangParser.AtomContext):
        return self.visitChildren(ctx)



del RusLangParser