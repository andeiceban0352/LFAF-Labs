import re

# Define regex patterns for numbers and operators
TOKENS = {
    (r"\s+", None),
    (r"\(", "L PAREN"),
    (r"\)", "R PAREN"),
    (r"\d+", "NUMBER"),
    (r"\+", "ADDITION"),
    (r"\-", "MINUS"),
    (r"\*", "TIMES"),
    (r"/", "DIVIDE"),
    (r"\!", "NOT"),
    (r"\%", "RATIO"),
    (r"\^", "POWER"),
}

class Lexer:

    def __init__(self, input):
        self.input_text = input

    def get_tokens(self):
        tokens = []
        position = 0

        while position < len(self.input_text):
            for character, character_type in TOKENS:

                #to compile a regular expression pattern into a regex pattern object
                regex = re.compile(character)

                # Match the next token based on its regex pattern
                match = regex.match(self.input_text, position)

                #chech if exist any matches
                if match:
                    if character_type:
                        token = (match.group(), character_type)
                        print(token)
                        tokens.append(token)
                    break # put the element in the list and break to go to the next element
            if not match:
                # If we didn't match any token, raise an error
                raise Exception(f"Invalid token ")
            else:
                # If we found a divide operator token, add it to the list and move the position forward
                position = match.end()
        return tokens



