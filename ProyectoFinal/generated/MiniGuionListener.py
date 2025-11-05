# Generated from MiniGuion.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .MiniGuionParser import MiniGuionParser
else:
    from MiniGuionParser import MiniGuionParser

# This class defines a complete listener for a parse tree produced by MiniGuionParser.
class MiniGuionListener(ParseTreeListener):

    # Enter a parse tree produced by MiniGuionParser#program.
    def enterProgram(self, ctx:MiniGuionParser.ProgramContext):
        pass

    # Exit a parse tree produced by MiniGuionParser#program.
    def exitProgram(self, ctx:MiniGuionParser.ProgramContext):
        pass


    # Enter a parse tree produced by MiniGuionParser#scene.
    def enterScene(self, ctx:MiniGuionParser.SceneContext):
        pass

    # Exit a parse tree produced by MiniGuionParser#scene.
    def exitScene(self, ctx:MiniGuionParser.SceneContext):
        pass


    # Enter a parse tree produced by MiniGuionParser#dialogue.
    def enterDialogue(self, ctx:MiniGuionParser.DialogueContext):
        pass

    # Exit a parse tree produced by MiniGuionParser#dialogue.
    def exitDialogue(self, ctx:MiniGuionParser.DialogueContext):
        pass


    # Enter a parse tree produced by MiniGuionParser#decir_stmt.
    def enterDecir_stmt(self, ctx:MiniGuionParser.Decir_stmtContext):
        pass

    # Exit a parse tree produced by MiniGuionParser#decir_stmt.
    def exitDecir_stmt(self, ctx:MiniGuionParser.Decir_stmtContext):
        pass


    # Enter a parse tree produced by MiniGuionParser#opcion_stmt.
    def enterOpcion_stmt(self, ctx:MiniGuionParser.Opcion_stmtContext):
        pass

    # Exit a parse tree produced by MiniGuionParser#opcion_stmt.
    def exitOpcion_stmt(self, ctx:MiniGuionParser.Opcion_stmtContext):
        pass



del MiniGuionParser