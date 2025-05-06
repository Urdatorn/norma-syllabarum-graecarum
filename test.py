from grc_macronizer import Macronizer
from grc_utils import colour_dichrona_in_open_syllables

macronizer = Macronizer(no_hypotactic=True)

output = macronizer.macronize("ἐάν οὖν πῃ ἔχεις συμβαλεῖν τὴν Κρατύλου μαντείαν, ἡδέως ἂν ἀκούσαιμι")

print(colour_dichrona_in_open_syllables(output))