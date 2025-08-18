'''
The songs of Aristophanes have only syllabification, like

[Ἦ] [πόλ]{λ' ἄ}[ελ]{πτ' ἔ}[νεσ]{τι}[ν ἐν] [τῷ] {μα}[κρῷ] {βί}[ῳ], [φεῦ],
{ἐ}[πεὶ] {τί}[ς ἄν] {πο}[τ' ἤλ]{πι}[σ', ὦ Σ][τρυ]{μό}[δω]{ρ', ἀ}[κοῦ][σαι]

and we need to automatically extract macron info and write the markup (^ for short and _ for long dichrona).
'''

import re
from grc_utils import DICHRONA, is_diphthong, short_set, short_vowel, vowel, word_with_real_dichrona

def heavy_syll(syll):
    """Check if a syllable is heavy (either ends on a consonant or contains a long vowel/diphthong)."""
    
    closed = not vowel(syll[-1])
    
    substrings = [syll[i:i+2] for i in range(len(syll) - 1)]
    has_diphthong = any(is_diphthong(substring) for substring in substrings)

    has_long = not short_vowel(syll) # short_vowel does not include short dichrona
    
    return closed or has_diphthong or has_long

def open_syll(syll):
    """Check if a syllable is open (ends on a vowel)."""

    return vowel(syll[-1])

def mark_open_sylls(text):
    """
    For each syllable in `text`:
      - If heavy [ ] and open_syll + word_with_real_dichrona → add "_"
      - If light { } and open_syll + word_with_real_dichrona → add "^"
    """
    def replacer(match):
        left, content, right = match.groups()
        if open_syll(content) and word_with_real_dichrona(content):
            if left == "[":   # heavy
                content += "_"
            elif left == "{": # light
                content += "^"
        return f"{left}{content}{right}"

    # Regex captures opening bracket, contents, closing bracket
    pattern = re.compile(r"(\[|\{)(.*?)(\]|\})")
    return pattern.sub(replacer, text)

def process_file(input_path, output_path):
    with open(input_path, "r", encoding="utf-8") as input_file, \
         open(output_path, "w", encoding="utf-8") as output_file:

        for line in input_file:
            new_line = mark_open_sylls(line.rstrip("\n"))
            output_file.write(new_line + "\n")


process_file("final/norma_aristophanis_canticorum.txt", "final/norma_aristophanis_canticorum_macrons.txt")
