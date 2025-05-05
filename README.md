# Norma Syllabarum Graecarum - A Benchmark for grc Syllabification and Weight Labelling

We introduce NSG as a common benchmark for the evaluation and comparison of NLP tools concerning the markup of prosodical features of Ancient Greek (*grc*) corpora. Three prosodical features are marked up explicitly: syllable boundary, syllable weight and vowel length. Derivately, this means that sandhi phenomena and, for verse, metre are also covered.

Short excerpts of about 20 lines from each of the below:
- Homer (*In Solem* 1-19, hexameter)
- Alcman
- Aristophanes (*Acharnenses*)
- Sophocles (*Oedipus Tyrannus* 1-20, iambic trimeter)
- Aeschylus (*Supplices* 1-10, anapests)
- Euripides (*Bacchae* 1-20, iambic trimeter)
- Plato (*Cratylus*, prose)
- Thucydides (prose)
- Dioscorides (elegiac distichs)
- Plutarch
- Epictetus (*Enchiridion* 1.1.1-1.5.1)
- Origenes (*Contra Celsum* 1.1-1.20)
- Nonnus
- Quintus (*Posthomerica* 1-20)

We also include here the marked up corpus of all 79 textually-sound responding songs of Aristophanes, borrowed from my project *Aristophanis Cantica*. In order not to thus schew the benchmark towards comedy, it is recommended to test on the Aristophaean corpus separately.

# Markup Format

The markup is straight-forward: 
- square brackets [] enclose heavy syllables
- curly brackets {} enclose light syllables
- carets ^ follow short ambiguous vowels (α, ι, υ)
- underscores _ follow long ambiguous vowels (α, ι, υ)

With regard to vowel length, the benchmark is designed to test performance of open (light) syllables only. This means that *all* open syllables with ambiguous vowels (α, ι, υ) have them marked with carets or underscores, while this is only *sporadically* true for closed syllables (and in such cases mostly before mute-liquid clusters).

A special challenge present at several points in the epic excerpts are syllables heavy due to having unusually long "final continuants", i.e. lingering onset liquids like ρ, μ, ν, that preempt the onset by starting already in the coda of the preceeding syllable, and which although thus being for all intents and purposes phonologically geminated, are not orthographically doubled, e.g.:
- [Ἠ][ῶ ]**[τε ]**{ῥο}{δό}[πη]{χυ^}{ν ἐ}[ϋπ]{λό}{κα^}[μόν ]{τε }{Σε}[λή][νην] (*In Solem*, 6)

In the same way, epic correption or shortening of long vowels before word-end hiatus:
- [ὃς ][φαί][νει θ][νη][τοῖ]{σι^ }{καὶ } κτλ. (*Ibid*. 8)

We also have an example of a word that avoids the normal rules of syllabification:
- ...[ῇ]**{σι^ }{Σκα^}**[μάν][δρου,] (*Posthomerica*, 10)

# Method