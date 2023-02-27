# Docstring
# __doc__

def palindromo(sentence: str) -> bool:
    """Permite conocer si un string es un palindromo.

    Args:
        sentence (str): String a evaluar.

    Returns:
        bool: True o False.
    """
    sentence = sentence.lower().replace(' ', '')
    return sentence == sentence[::-1]

print(palindromo('Anita Lava la tina'))
print(palindromo('CodigoFacilito'))

#help(palindromo)

