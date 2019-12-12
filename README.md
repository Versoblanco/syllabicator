# Syllabicator

Syllabicator takes a word and returns a list of syllables acording to the given language rules. It is written in Python and works with both 2 and 3 version.

[Installation](#installation)
| [Syntax](#syntax)
| [Supported languages](#supportedlanguages)
| [Contribute](#contribute)

## Installation

At the moment it is only available as a simple function. Hopefully, it will be shortly available in the Python Package Repository. At the moment you can just clone/ copy / download the files and import them for your proyect.

Please, check first [license compatibility](https://www.gnu.org/licenses/license-list.html#GPLCompatibleLicenses)

## Syntax

<code>syllabicator.syllabicate(word, lang)</code>

It takes two arguments:

- <code>word</code> understood as a any iterable sequence of charachters.
- <code>lang</code> is the language expressed by its two letters standards (en, de, it, etc.). Currently it will work only with <code>es</code>

        words = u"hodor" # Input should be always Unicode type
        print(syllabicator.syllabicate(word, es))

        # Output [ho, dor]


## Supported languages

As Spaniard with a degree in Spanish Philology I am actually focused on this language, although the code is structured in order to take other sets of rules as input and should be easily adapted to language that share similar patterns.

More details about implementation for spanish in [LEAME](/LEAME.md) file.

## Contribute

You can contribute by adding a new language.

For each new language you should create two files:
- A plain text or markdown file with a short introduction and information about rules used, references and license.
- A python file named as the language's two letter code defined in the [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) (lowercase).

Please, don't forget the copyright and license notice, and to choose a [compatible license](https://www.gnu.org/licenses/license-list.html#GPLCompatibleLicenses).

*Syllabicator* works iteratively, extracting one syllable and looking for the next one from that point. This method has two major asumptions which limit the potential supported languages:

- The text is read from left to right
- You cannot know word's previous syllables.

The code must contain a function called <code>len_syllable(word)</code> that takes a sequence of Unicode charachters and returns the first syllable lenght, that is, the index of the first letter from second syllable.
