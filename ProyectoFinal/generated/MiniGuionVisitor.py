# Generated from MiniGuion.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .MiniGuionParser import MiniGuionParser
else:
    from MiniGuionParser import MiniGuionParser

# This class defines a complete generic visitor for a parse tree produced by MiniGuionParser.

class MiniGuionVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MiniGuionParser#program.
    def visitProgram(self, ctx:MiniGuionParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGuionParser#scene.
    def visitScene(self, ctx:MiniGuionParser.SceneContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGuionParser#dialogue.
    def visitDialogue(self, ctx:MiniGuionParser.DialogueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGuionParser#decir_stmt.
    def visitDecir_stmt(self, ctx:MiniGuionParser.Decir_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGuionParser#opcion_stmt.
    def visitOpcion_stmt(self, ctx:MiniGuionParser.Opcion_stmtContext):
        return self.visitChildren(ctx)



del MiniGuionParser