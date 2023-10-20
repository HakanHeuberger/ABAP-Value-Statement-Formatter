import sys
import re

def format_abap_code(input_text):
    input_text = input_text.replace("value", "VALUE")
    tokens = re.findall(r"'[^']*'|VALUE #\(|[a-zA-Z_0-9]+|\*|[=)(]", input_text)
    formatted_text = ""
    indentation = 0
    openingbracketflag = False

    for token in tokens:
        if token == "VALUE #(":
            formatted_text += token + "\n"
            indentation += 2
        elif token == ")":
            indentation -= 2
            formatted_text += " " * indentation + token + "\n"
        elif token == "(":
            formatted_text += " " * indentation + token
            indentation += 2
            openingbracketflag = True
        elif token.startswith("="):
            formatted_text += token + " "
        elif token.startswith("'") and token.endswith("'"):
            formatted_text += token + "\n"
        else:
            if openingbracketflag:
                formatted_text += " " + token + " "
                openingbracketflag = False
            else:
                formatted_text += " " * indentation + token + " "

    return formatted_text.strip()


# Test the function
input_text = open("Input.txt", "r").read()
formatted_text = format_abap_code(input_text)
print(formatted_text)
open("Output.txt", "w").write(formatted_text)

