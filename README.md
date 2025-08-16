# Norma Syllabarum Graecarum - A Benchmark for grc Syllabification and Weight Labelling

We introduce NSG as a common benchmark for the evaluation and comparison of NLP tools concerning the markup of prosodical features of Ancient Greek (*grc*) corpora. Three prosodical features are marked up explicitly: syllable boundary, syllable weight and vowel length. Derivately, this means that sandhi phenomena and, for verse, metre are also covered.

Short excerpts of about 20 lines from each of the below 14 authors, spanning many periods and genres:

- Homer (*In Solem* 1-19, hexameter) ✅
- Alcman (*Louvre Partheneion* 36-49, mix of aeolic, trochaic and dactylic cola, NB: contains ϝ) ✅
- Aristophanes (*Acharnenses* 1-16, iambic trimeter) ✅
- Sophocles (*Oedipus Tyrannus* 1-20, iambic trimeter) ✅
- Aeschylus (*Supplices* 1-10, anapaests) ✅
- Euripides (*Bacchae* 1-20, iambic trimeter) ✅
- Plato (*Cratylus* 383-384a5, prose) ✅
- Thucydides (*Thucydidis historiae* 1.1.1.1-1.2.2.1, prose) ✅
- Dioscorides (*Anthologia Graeca* 5.55, elegiac distichs) ✅
- Plutarch (*Stoicos absurdiora poetis dicere* 1057.C1-F1, prose) ✅
- Epictetus (*Enchiridion* 1.1.1-1.5.1, prose) ✅
- Origenes (*Contra Celsum* 1.1-1.20, prose) ✅
- Nonnus (*Dionysiaca* 1-20, dactylic hexameter) ✅
- Quintus (*Posthomerica* 1-20, dactylic hexameter) ✅

None of these texts snippets are included in the [Hypotactic](https://github.com/Urdatorn/hypotactic) corpus, which means that a model trained on Hypotactic will not have any unfair advantage.

We also include here the marked-up corpus of all the 78 responding songs of Aristophanes, borrowed from my project [*Aristophanis Cantica*](https://github.com/Urdatorn/aristophanis-cantica). For further details, see that repository. In order not to thus schew the benchmark towards comedy, it is recommended to test on the Aristophanean corpus separately.

## Markup Format

The markup is straight-forward: 
- square brackets [] enclose heavy syllables
- curly brackets {} enclose light syllables
- carets ^ follow short ambiguous vowels (α, ι, υ)
- underscores _ follow long ambiguous vowels (α, ι, υ)

In prose, for ease of comparison we consider the sentence to be the equivalent of the verse line, with the consequence that the final syllable of a sentence will be considered heavy if it ends with a consonant, even though the following sentence begins with a vowel; i.e. a prose *brevis in longo*.

With regard to vowel length, the benchmark is designed to test performance of open (light) syllables only. This means that *all* open syllables with ambiguous vowels (α, ι, υ) have them marked with carets or underscores, while this is only *sporadically* true for closed syllables (and in such cases mostly before mute-liquid clusters).

A special challenge present at several points in the epic excerpts are syllables heavy due to having unusually long "final continuants", i.e. lingering onset liquids like ρ, μ, ν, that preempt the onset by starting already in the coda of the preceeding syllable, and which although thus being for all intents and purposes phonologically geminated, are not orthographically doubled, e.g.:
- [Ἠ][ῶ ]**[τε ]**{ῥο}{δό}[πη]{χυ^}{ν ἐ}[ϋπ]{λό}{κα^}[μόν ]{τε }{Σε}[λή][νην] (*In Solem*, 6)

In the same way, epic correption or shortening of long vowels before word-end hiatus:
- [ὃς ][φαί][νει θ][νη][τοῖ]{σι^ }{καὶ } κτλ. (*Ibid*. 8)

We also have an example of a word that avoids the normal rules of syllabification:
- ...[ῇ]**{σι^ }{Σκα^}**[μάν][δρου,] (*Posthomerica*, 10)

### Stoplist

Since some of the excerpts contain rare proper-name word forms some of which, such as Alcman's Ἀγιδώ, are most likely *hapax legomenon*, we have collected all of these in an stop list, so that they can optionally be excluded from the benchmark.

## Researchers

This benchmark is part of ongoing research projects by Albin Thörn Cleland at Lund university and Eric Cullhed at Uppsala university. Its new syllabified and macronized editions of ancient texts are made available under the copyleft GNU GPL licence.
