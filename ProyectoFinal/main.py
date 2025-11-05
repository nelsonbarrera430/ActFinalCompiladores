# main.py
import sys, os
from antlr4 import FileStream, CommonTokenStream
sys.path.append("generated")

from semantic_analyzer.semantic_checker import SemanticChecker
from codegen.py_generator import PyGenerator

try:
    from MiniGuionLexer import MiniGuionLexer
    from MiniGuionParser import MiniGuionParser
    from MiniGuionVisitor import MiniGuionVisitor
except:
    print("❌ Ejecuta ANTLR primero (ver instrucciones más abajo).")
    sys.exit(1)


class ASTBuilder(MiniGuionVisitor):
    def visitProgram(self, ctx):
        return {"scenes": [self.visit(x) for x in ctx.scene()]}

    def visitScene(self, ctx):
        return {
            "id": ctx.ID().getText(),
            "dialogues": [self.visit(x) for x in ctx.dialogue()],
        }

    def visitDecir_stmt(self, ctx):
        return {"type": "decir", "text": ctx.STRING().getText()}

    def visitOpcion_stmt(self, ctx):
        return {
            "type": "opcion",
            "text": ctx.STRING().getText(),
            "target": ctx.ID().getText(),
        }


def compile_file(filename):
    """Compila un archivo fuente y genera el código Python + logs en output.txt"""
    input_stream = FileStream(filename, encoding="utf-8")
    lexer = MiniGuionLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = MiniGuionParser(tokens)
    tree = parser.program()

    ast = ASTBuilder().visit(tree)

    checker = SemanticChecker()
    errors = checker.analyze(ast)

    # abrir archivo de salida (log)
    with open("output.txt", "w", encoding="utf-8") as log:
        log.write("=== COMPILACIÓN MiniGuion ===\n")
        log.write(f"Archivo de entrada: {filename}\n\n")

        if errors:
            log.write("❌ ERRORES SEMÁNTICOS DETECTADOS:\n")
            for e in errors:
                log.write(" - " + e + "\n")
            print("❌ Errores semánticos encontrados (ver output.txt)")
            return

        # Generar el código Python
        generator = PyGenerator()
        py_code = generator.generate(ast)

        with open("output_program.py", "w", encoding="utf-8") as f:
            f.write(py_code)

        log.write("✅ Código generado correctamente.\n")
        log.write("Archivo generado: output_program.py\n")
        print("✅ Código Python generado en output_program.py")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python main.py input.txt")
    else:
        compile_file(sys.argv[1])
