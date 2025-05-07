from grc_utils import colour_dichrona_in_open_syllables, all_vowels, syllabifier, normalize_word
import unicodedata

# macronizer = Macronizer(no_hypotactic=True)

# output = macronizer.macronize("ἐάν οὖν πῃ ἔχεις συμβαλεῖν τὴν Κρατύλου μαντείαν, ἡδέως ἂν ἀκούσαιμι")

# print(colour_dichrona_in_open_syllables(output))


print(all_vowels)
decomposed = unicodedata.normalize('NFKD', "Οἰδίπους ἔχει")
print(syllabifier(decomposed))

macronisandum = "ἐπολέμησαν"