# Docstring
# __doc__

def palindromo(sentence: str) -> bool:
    """
    Permite conocer si un string es palindromo.

    Args:
        sentence: string
    Returns:
        bool
    """
    sentence = sentence.lower().replace(' ', '')
    return sentence == sentence[::-1]

print(palindromo('Anita Lava la tina'))
print(palindromo('CodigoFacilito'))

#help(palindromo)

