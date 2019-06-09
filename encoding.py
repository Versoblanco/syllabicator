# !/usr/bin/env python
# -*- coding: utf-8 -*-


def get_encoding():
    """Get declared encoding from text source."""
    # TODO: Create real function
    encoding = 'utf-8'
    return encoding


def decode_str(text):
    """Get declared encoding from text source and return decoded text."""
    if type(text) is str:
        text = text.decode(get_encoding())
    return text
