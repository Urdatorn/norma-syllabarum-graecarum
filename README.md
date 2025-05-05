# Norma Syllabarum Graecarum - A Benchmark for grc Syllabification and Weight Labelling

We introduce NSG as a common benchmark for the evaluation and comparison of NLP tools concerning the markup of prosodical features of Ancient Greek (*grc*) corpora. Three prosodical features are marked up explicitly: syllable boundary, syllable weight and vowel length. Derivately, this means that sandhi phenomena and, for verse, metre are also covered.

Short excerpts from:
- Homer (*In Solem*)
- Alcman
- Aristophanes (*Acharnenses*)
- Sophocles (*Supplices*)
- Aeschylus
- Euripides (*Bacchae*)
- Plato (*Cratylus*)
- Thucydides
- Xenophon (*Anabasis*)
- Plutarch
- Epictetus
- Origenes
- Nonnus

A special challenge present at several points in the epic excerpts are syllables heavy due to having unusually long "final continuants", i.e. lingering onset liquids like ρ, μ, ν, that preempt the onset by starting already in the coda of the preceeding syllable, and which although thus being for all intents and purposes phonologically geminated, are not orthographically doubled, e.g.:
- [Ἠ][ῶ ]**[τε ]**{ῥο}{δό}[πη]{χυ^}{ν ἐ}[ϋπ]{λό}{κα^}[μόν ]{τε }{Σε}[λή][νην] (*In Solem*, 6)

In the same way, epic correption or shortening of long vowels before word-end hiatus:
- [ὃς ][φαί][νει θ][νη][τοῖ]{σι^ }{καὶ } κτλ. (*Ibid*. 8)

We also have an example of a word that avoids the normal rules of syllabification:
- ...[ῇ]**{σι^ }{Σκα^}**[μάν][δρου,] (*Posthomerica*, 10)

# Method