# Generated from RusLang.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .RusLangParser import RusLangParser
else:
    from RusLangParser import RusLangParser

# This class defines a complete listener for a parse tree produced by RusLangParser.
class RusLangListener(ParseTreeListener):

    # Enter a parse tree produced by RusLangParser#program.
    def enterProgram(self, ctx:RusLangParser.ProgramContext):
        pass

    # Exit a parse tree produced by RusLangParser#program.
    def exitProgram(self, ctx:RusLangParser.ProgramContext):
        pass


    # Enter a parse tree produced by RusLangParser#globalStatement.
    def enterGlobalStatement(self, ctx:RusLangParser.GlobalStatementContext):
        pass

    # Exit a parse tree produced by RusLangParser#globalStatement.
    def exitGlobalStatement(self, ctx:RusLangParser.GlobalStatementContext):
        pass


    # Enter a parse tree produced by RusLangParser#varDeclaration.
    def enterVarDeclaration(self, ctx:RusLangParser.VarDeclarationContext):
        pass

    # Exit a parse tree produced by RusLangParser#varDeclaration.
    def exitVarDeclaration(self, ctx:RusLangParser.VarDeclarationContext):
        pass


    # Enter a parse tree produced by RusLangParser#varList.
    def enterVarList(self, ctx:RusLangParser.VarListContext):
        pass

    # Exit a parse tree produced by RusLangParser#varList.
    def exitVarList(self, ctx:RusLangParser.VarListContext):
        pass


    # Enter a parse tree produced by RusLangParser#statement.
    def enterStatement(self, ctx:RusLangParser.StatementContext):
        pass

    # Exit a parse tree produced by RusLangParser#statement.
    def exitStatement(self, ctx:RusLangParser.StatementContext):
        pass


    # Enter a parse tree produced by RusLangParser#assignmentStatement.
    def enterAssignmentStatement(self, ctx:RusLangParser.AssignmentStatementContext):
        pass

    # Exit a parse tree produced by RusLangParser#assignmentStatement.
    def exitAssignmentStatement(self, ctx:RusLangParser.AssignmentStatementContext):
        pass


    # Enter a parse tree produced by RusLangParser#printStatement.
    def enterPrintStatement(self, ctx:RusLangParser.PrintStatementContext):
        pass

    # Exit a parse tree produced by RusLangParser#printStatement.
    def exitPrintStatement(self, ctx:RusLangParser.PrintStatementContext):
        pass


    # Enter a parse tree produced by RusLangParser#ifStatement.
    def enterIfStatement(self, ctx:RusLangParser.IfStatementContext):
        pass

    # Exit a parse tree produced by RusLangParser#ifStatement.
    def exitIfStatement(self, ctx:RusLangParser.IfStatementContext):
        pass


    # Enter a parse tree produced by RusLangParser#иначеЕслиPart.
    def enterИначеЕслиPart(self, ctx:RusLangParser.ИначеЕслиPartContext):
        pass

    # Exit a parse tree produced by RusLangParser#иначеЕслиPart.
    def exitИначеЕслиPart(self, ctx:RusLangParser.ИначеЕслиPartContext):
        pass


    # Enter a parse tree produced by RusLangParser#иначеPart.
    def enterИначеPart(self, ctx:RusLangParser.ИначеPartContext):
        pass

    # Exit a parse tree produced by RusLangParser#иначеPart.
    def exitИначеPart(self, ctx:RusLangParser.ИначеPartContext):
        pass


    # Enter a parse tree produced by RusLangParser#whileStatement.
    def enterWhileStatement(self, ctx:RusLangParser.WhileStatementContext):
        pass

    # Exit a parse tree produced by RusLangParser#whileStatement.
    def exitWhileStatement(self, ctx:RusLangParser.WhileStatementContext):
        pass


    # Enter a parse tree produced by RusLangParser#blockStatement.
    def enterBlockStatement(self, ctx:RusLangParser.BlockStatementContext):
        pass

    # Exit a parse tree produced by RusLangParser#blockStatement.
    def exitBlockStatement(self, ctx:RusLangParser.BlockStatementContext):
        pass


    # Enter a parse tree produced by RusLangParser#expr.
    def enterExpr(self, ctx:RusLangParser.ExprContext):
        pass

    # Exit a parse tree produced by RusLangParser#expr.
    def exitExpr(self, ctx:RusLangParser.ExprContext):
        pass


    # Enter a parse tree produced by RusLangParser#orExpr.
    def enterOrExpr(self, ctx:RusLangParser.OrExprContext):
        pass

    # Exit a parse tree produced by RusLangParser#orExpr.
    def exitOrExpr(self, ctx:RusLangParser.OrExprContext):
        pass


    # Enter a parse tree produced by RusLangParser#andExpr.
    def enterAndExpr(self, ctx:RusLangParser.AndExprContext):
        pass

    # Exit a parse tree produced by RusLangParser#andExpr.
    def exitAndExpr(self, ctx:RusLangParser.AndExprContext):
        pass


    # Enter a parse tree produced by RusLangParser#equalityExpr.
    def enterEqualityExpr(self, ctx:RusLangParser.EqualityExprContext):
        pass

    # Exit a parse tree produced by RusLangParser#equalityExpr.
    def exitEqualityExpr(self, ctx:RusLangParser.EqualityExprContext):
        pass


    # Enter a parse tree produced by RusLangParser#relationalExpr.
    def enterRelationalExpr(self, ctx:RusLangParser.RelationalExprContext):
        pass

    # Exit a parse tree produced by RusLangParser#relationalExpr.
    def exitRelationalExpr(self, ctx:RusLangParser.RelationalExprContext):
        pass


    # Enter a parse tree produced by RusLangParser#additiveExpr.
    def enterAdditiveExpr(self, ctx:RusLangParser.AdditiveExprContext):
        pass

    # Exit a parse tree produced by RusLangParser#additiveExpr.
    def exitAdditiveExpr(self, ctx:RusLangParser.AdditiveExprContext):
        pass


    # Enter a parse tree produced by RusLangParser#multiplicativeExpr.
    def enterMultiplicativeExpr(self, ctx:RusLangParser.MultiplicativeExprContext):
        pass

    # Exit a parse tree produced by RusLangParser#multiplicativeExpr.
    def exitMultiplicativeExpr(self, ctx:RusLangParser.MultiplicativeExprContext):
        pass


    # Enter a parse tree produced by RusLangParser#atom.
    def enterAtom(self, ctx:RusLangParser.AtomContext):
        pass

    # Exit a parse tree produced by RusLangParser#atom.
    def exitAtom(self, ctx:RusLangParser.AtomContext):
        pass



del RusLangParser