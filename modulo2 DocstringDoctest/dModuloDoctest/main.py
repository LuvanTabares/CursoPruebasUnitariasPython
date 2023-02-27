# Docstring
# __doc__

def palindromo(sentence: str) -> bool:
    """Permite conocer si un string es un palindromo.

    Args:
        sentence (str): String a evaluar.

    Returns:
        bool: True o False.

    Examples:

    >>> palindromo('Anita lava la tina')
    True

    >>> palindromo('CodigoFacilito')
    False

    >>> palindromo('Oso')
    True
    """
    sentence = sentence.lower().replace(' ', '')
    return sentence == sentence[::-1]


# python -m doctest main.py -v
