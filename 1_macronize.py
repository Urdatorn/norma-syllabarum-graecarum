from grc_macronizer import Macronizer
from grc_utils import colour_dichrona_in_open_syllables

input_name = "oedipus"

with open(f"raw/{input_name}.txt", "r", encoding="utf-8") as f:
    text = f.read()

macronized_text = Macronizer(no_hypotactic=True).macronize(text)

with open(f"macronized/{input_name}.txt", "w", encoding="utf-8") as f:
    f.write(macronized_text)

print("\n" + colour_dichrona_in_open_syllables(macronized_text))