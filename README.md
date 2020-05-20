# Syllabicator [![Build Status](https://travis-ci.com/Versoblanco/syllabicator.svg?branch=master)](https://travis-ci.com/Versoblanco/syllabicator)

Syllabicator takes a word and returns a list of syllables acording to the given language rules. It also finds tonic und atonic syllables. It is written in Python and works with both 2 and 3 version.

[Installation](#installation)
| [Syntax](#syntax)
| [Supported languages](#supported_languages)
| [Contribute](#contribute)

## Installation

At the moment it is only a simple function. Hopefully, it will be shortly available in the Python Package Repository and with some kind of user interface. At the moment you can just clone/ copy / download the files and import them for your project.

Please, check first [license compatibility](https://www.gnu.org/licenses/license-list.html#GPLCompatibleLicenses)

## Syntax

        syllabicator.syllabicate(word, lang)
        stress.tonic(word, lang)
        stress.tonic(word, lang)

They take the same arguments:

- <code>word</code> understood as a any iterable sequence of characters.
- <code>lang</code> is the language expressed by its two letters standard (en, de, it, etc.). Currently it will work only with Spanish <code>es</code>

        # Syllabicate

        >>> import syllabicator
        >>> import lang.es as es
        >>> word = u"hodor"     # Input should be unicode. Default in Python 3
        >>> print(syllabicator.syllabicate(word,es))
        [u'ho', u'dor']

        # Tonics and atonics

        >>> import syllabicator
        >>> import lang.es as es
        >>> import stress
        >>> word = u"esdrújula"
        >>> print(stress.tonic(word, es))
        drú
        >>> print(stress.atonic(word,es))
        [u'es', u'ju', u'la']


## Supported languages

I am only focused on Spanish, although the code is structured in order to take other sets of rules as a parameter and should be easily adapted to language that share similar patterns. Contributors for other languages are wellcomed.

More details about implementation for Spanish in [LEAME](/LEAME.md) file.

## Contribute

You can contribute by adding a new language.

For each new language you should create two files:
- A plain text or markdown file with a short introduction and information about rules used, references and license.
- A python file named as the language's two letter code defined in the [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) (lowercase).

Please, don't forget the copyright and license notice, and to choose a [compatible license](https://www.gnu.org/licenses/license-list.html#GPLCompatibleLicenses).

*Syllabicator* works iteratively, extracting one syllable and looking for the next one from that point. This method has two major asumptions which limit the potential supported languages:

- The text is read from left to right
- You cannot know word's previous syllables.

The code must contain a function called <code>len_syllable(word)</code> that takes a sequence of Unicode characters and returns the first syllable lenght, that is, the index of the first letter from second syllable.
