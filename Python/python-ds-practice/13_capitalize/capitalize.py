def capitalize(phrase):
    """Capitalize first letter of first word of phrase.

        >>> capitalize('python')
        'Python'

        >>> capitalize('only first word')
        'Only first word'
    """

    return phrase[:1].upper() + phrase[1:]
    
    # apparently can use capitalize function for phrase --> return phrase.capitalize()