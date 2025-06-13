import re
import filetype

def validate_email(email):
    if len(email) > 100:
        return False
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, email) is not None

def validate_celular(celular):
    nuevo_celular = ""
    for i in range(len(celular)):
        if i == 4:
            nuevo_celular += "."
        nuevo_celular += celular[i]
    celular_regex = r'^\+\d{3}\.\d{8}$'
    return re.match(celular_regex, nuevo_celular) is not None

def validate_text_input(text, max_length=1000, min_length=-1):
    prohibited_patterns = [
        r'<.*?>',  # Etiquetas HTML
        r'(?:--|;|/\*|\*/)',  # SQL Injection
        r'(?:\bSELECT\b|\bINSERT\b|\bUPDATE\b|\bDELETE\b|\bDROP\b|\bALTER\b)',  # SQL Keywords
        r'(?:\bUNION\b|\bALL\b|\bWHERE\b|\bLIKE\b|\bOR\b|\bAND\b)',  # SQL Logical Operators
        r'(?:\bEXEC\b|\bEXECUTE\b|\bDECLARE\b|\bCAST\b)',  # SQL Execution Keywords
        r'(?:\bINTO\b|\bVALUES\b|\bSET\b)',  # SQL Clauses
        r'javascript:',  # Bloquea intentos de usar "javascript:" en enlaces
    ]
    for pattern in prohibited_patterns:
        if re.search(pattern, text, re.IGNORECASE):
            return False
    if len(text) > max_length or len(text) < min_length:
        return False
    return True

def validate_conf_img(img):
    ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}
    ALLOWED_MIMETYPES = {"image/jpeg", "image/png", "image/jpg"}

    # check if a file was submitted
    if img is None:
        return False

    # check if the browser submitted an empty file
    if img.filename == "":
        return False
    
    # check file extension
    ftype_guess = filetype.guess(img)
    if ftype_guess.extension not in ALLOWED_EXTENSIONS:
        return False
    # check mimetype
    if ftype_guess.mime not in ALLOWED_MIMETYPES:
        return False
    return True
