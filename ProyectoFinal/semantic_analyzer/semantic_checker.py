# semantic_analyzer/semantic_checker.py

class SemanticChecker:
    def __init__(self):
        self.scenes = set()
        self.errors = []

    def analyze(self, ast):
        self.scenes = set()
        self.errors = []
        self._collect_scenes(ast)
        self._validate_references(ast)
        return self.errors

    def _collect_scenes(self, ast):
        for scene in ast["scenes"]:
            name = scene["id"]
            if name in self.scenes:
                self.errors.append(f"Escena duplicada: {name}")
            self.scenes.add(name)

    def _validate_references(self, ast):
        for scene in ast["scenes"]:
            for d in scene["dialogues"]:
                if d["type"] == "opcion" and d["target"] not in self.scenes:
                    self.errors.append(
                        f"Escena referenciada no existe: {d['target']} en escena {scene['id']}"
                    )
