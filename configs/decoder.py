import numpy as np

def decode_text(in_text, secret=1):
    """This function will decode encoded text

    Args:
        in_text (str, optional): Encoded text
        secret (int, optional): Secret number. Defaults to 1.

    Returns:
        _type_: str
    """
    
    out_text = ""
    letters = []
    temp_text = ""
    texts = []
    is_negative = False
    in_text += 'A'
    if in_text[0] == "-":
        is_negative = True
    for i in range(len(in_text)):

        if i == 0 and is_negative:
            continue
        if in_text[i].isalpha():

            texts.append(temp_text)
            if i > 1:
                temp_text = ""
        temp_text += in_text[i]

    for i in range(len(texts)):
        letters.append("")

    if is_negative:
        letters[1] += "-"
    for i in range(len(texts)):
        if "-" in texts[i]:
            letters[i + 1] += "-"
        letters[i] += texts[i].replace("-", "")
    letters.pop(0)

    decrypted = []
    for i in range(len(letters)):
        is_negative = False
        temp_text = ""
        if letters[i][0] == "-":
            is_negative = True
            letters[i] = letters[i].replace("-", "")
        character = letters[i][0]

        letters[i] = letters[i].replace(character, "")

        character = ord(character)

        ans = np.sqrt(int(letters[i]) - secret)

        if is_negative:
            ans = -1 * ans

        decrypted.append(chr(int(ans) + int(character)))

    ans = ""
    for i in decrypted:
        ans += i
    return ans