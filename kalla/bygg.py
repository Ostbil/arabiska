"""Bygger appen frÃ¥n template.html och data/ord.json.

KÃ¶r i den hÃ¤r mappen:

    python bygg.py

Resultatet hamnar i ../webb/index.html och ../webb/ord.json.
"""
import os, shutil

HERE = os.path.dirname(os.path.abspath(__file__))
WEBB = os.path.join(HERE, "..")

tpl = open(os.path.join(HERE, "template.html"), encoding="utf-8").read()
words = open(os.path.join(HERE, "data", "ord.json"), encoding="utf-8").read().strip()
os.makedirs(WEBB, exist_ok=True)
with open(os.path.join(WEBB, "index.html"), "w", encoding="utf-8") as f:
    f.write(tpl.replace("__WORDS__", words))
shutil.copyfile(os.path.join(HERE, "data", "ord.json"), os.path.join(WEBB, "ord.json"))
print("Klart: ../webb/index.html")

