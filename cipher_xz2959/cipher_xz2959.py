def cipher(text, shift, encrypt=True):
    """
    Encrypt the text using shift coding.

    Args:
        text (str): represent the source text
        shift (int): the shift size
        encrypt (bool): True for encrypt and False for decrypt

    Returns:
        str: represent the cipher

    Examples:

    >>> cipher("hello cipher!", 10)
    rovvy mszroB!
    >>> cipher("hello cipher!", -2)
    fcjjm agnfcp!
    >>> cipher("fcjjm agnfcp!", 2)
    hello cipher!
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = ''
    for c in text:
        index = alphabet.find(c)
        if index == -1:
            new_text += c
        else:
            new_index = index + shift if encrypt == True else index - shift
            new_index %= len(alphabet)
            new_text += alphabet[new_index:new_index + 1]
    return new_text
