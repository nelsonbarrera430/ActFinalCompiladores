# codegen/py_generator.py

class PyGenerator:
    def generate(self, ast):
        code = ["# Archivo generado automáticamente\n"]

        for scene in ast["scenes"]:
            name = scene["id"]
            code.append(f"def {name}():")
            for d in scene["dialogues"]:
                if d["type"] == "decir":
                    code.append(f'    print({d["text"]})')
                elif d["type"] == "opcion":
                    code.append(f'    op = input({d["text"]} + " -> ")')
                    code.append(f'    if op == {d["text"]}:')
                    code.append(f'        {d["target"]}()')
            code.append("")

        first = ast["scenes"][0]["id"]
        code.append(f"if __name__ == '__main__':")
        code.append(f"    {first}()")

        return "\n".join(code)
