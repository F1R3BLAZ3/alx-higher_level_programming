#!/usr/bin/python3

def text_indentation(text):
    """
    Prints the given text with 2 new lines after each occurrence of '.', '?', and ':' characters.

    Args:
        text (str): The text to be processed and printed.

    Raises:
        TypeError: If text is not a string.

    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punctuation = ['.', '?', ':']
    result = ''
    i = 0
    while i < len(text):
        result += text[i]
        if text[i] in punctuation:
            result += '\n\n'
        i += 1

    print(result.strip())
