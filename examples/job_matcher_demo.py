"""
job_matcher_demo.py — Exemplo da lógica de matching por área e senioridade.
Usa word-boundaries para evitar falso positivo em keywords.
"""

import re

def classify_area(job_text: str, keywords: list) -> bool:
    for kw in keywords:
        pattern = rf"(?<![a-z0-9+#]){re.escape(kw)}(?![a-z0-9])"
        if re.search(pattern, job_text, re.IGNORECASE):
            return True
    return False

if __name__ == "__main__":
    text = "Estamos contratando Desenvolvedor Python Pleno com Django."
    print("Match Python:", classify_area(text, ["python"]))
    print("Match Go (deve ser False por word-boundary):", classify_area(text, ["go"]))
