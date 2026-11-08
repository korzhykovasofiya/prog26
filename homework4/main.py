from wer import wer
import json
from pathlib import Path

with open("homework4/text1.txt", encoding="utf-8") as file:
    reference = file.read()

with open("homework4/text2.txt", encoding="utf-8") as file:
    hypothesis = file.read()

wer_value, S, D, I, N = wer(reference, hypothesis)

result = {"WER": wer_value, "S": S, "D": D, "I": I, "N": N}
with open("homework4/result.json", "w", encoding="utf-8") as f:
    json.dump(result, f, ensure_ascii=False, indent=2)