import re
from grc_utils import colour_dichrona_in_open_syllables, count_dichrona_in_open_syllables, short_set, syllabifier

input_name = "plutarchus"
hexameter = False

with open(f"macronized/{input_name}.txt", "r", encoding="utf-8") as f:
    macronized_text = f.read()

irrelevant = r"""[‘’'\u0387\u037e\u00b7.,!?;:"()\[\]\{\}<>\-—…\n«»†×⏑⏓– ]"""

lines = []
for line in macronized_text.splitlines():
    line = syllabifier(line)
    for idx, syllable in enumerate(line):
        
        if re.sub(irrelevant, "", syllable)[-1] in short_set | {"^"}:
            line[idx] = "{" + syllable + "}"
        else:
            line[idx] = "[" + syllable + "]"

    lines.append(line)

with open(f"syllabified/{input_name}.txt", "w", encoding="utf-8") as f:
    for line in lines:
        f.write("".join(line) + "\n")

### Visualization ###

for idx, line in enumerate(lines):
    lines[idx] = "".join(line)

final_text = "\n".join(lines).replace("{", "").replace("}", "").replace("[", "").replace("]", "")

print("\n" + colour_dichrona_in_open_syllables(final_text))
print("\nTotal number of open syllables:", count_dichrona_in_open_syllables(final_text))

### Hexameter regex check ###

hexameter_pattern = re.compile(r"(\[.+?\]|\{.+?\}\{.+?\}){11}(\[.+?\]|\{.+?\})")

if hexameter:
    for i, line in enumerate(lines, 1):
        if hexameter_pattern.fullmatch(line):
            print(f"Line {i} ✅ conforms")
        else:
            print(f"Line {i} ❌ does NOT conform")