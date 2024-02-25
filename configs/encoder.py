import hashlib

def encode_text(text = "None"):
    """This function will encode any text to unique number

    Args:
        text (str, optional): text. Defaults to "None".

    Returns:
        _type_: int
    """
    sha_encoder = hashlib.sha256()
    sha_encoder.update(text.encode("utf-8"))
    encoding = sha_encoder.hexdigest()
    id = 0
    for i in range(len(encoding)):
        coef = 1+i/10
        id = id + ord(encoding[i])*coef
    return int(id)
