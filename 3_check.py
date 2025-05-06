import re
from grc_utils import colour_dichrona_in_open_syllables, count_dichrona_in_open_syllables, short_set, syllabifier

input_name = "enchiridion"
hexameter = False

with open(f"final/{input_name}.txt", "r", encoding="utf-8") as f:
    text = f.read()

text_test = re.sub(r"[\{\}\[\]]", "", text)

print("\n" + colour_dichrona_in_open_syllables(text_test))
print("\nTotal number of open syllables:", count_dichrona_in_open_syllables(text_test))

if hexameter:
    print('\nHexameter regex check\n')

    lines = text.splitlines()

    hexameter_pattern = re.compile(r"(\[.+?\]|\{.+?\}\{.+?\}){11}(\[.+?\]|\{.+?\})")

    for i, line in enumerate(lines, 1):
        if hexameter_pattern.fullmatch(line):
            print(f"Line {i} ✅ conforms")
        else:
            print(f"Line {i} ❌ does NOT conform")