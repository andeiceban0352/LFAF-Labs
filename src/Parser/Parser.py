class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    # Parse a sequence of tokens and evaluate the expression
    def parse_tokens(self):
        rez = self.evaluate_expression()
        if self.pos < len(self.tokens):
            raise Exception(f"Invalid syntax")
        return rez

    #Parse and evaluate the ADDITION and MINUS expressions
    def evaluate_expression(self):
        rez = self.evaluate_term()
        while self.pos < len(self.tokens):
            if self.tokens[self.pos][1] == "ADDITION":
                self.pos += 1
                rez += self.evaluate_term()
            elif self.tokens[self.pos][1] == "MINUS":
                self.pos += 1
                rez -= self.evaluate_term()
            else:
                break
        return rez

    # Parse and evaluate the TIMES and DIVIDE expressions
    def evaluate_term(self):
        rez = self.evaluate_factors()
        while self.pos < len(self.tokens):
            if self.tokens[self.pos][1] == "TIMES":
                self.pos += 1
                rez *= self.evaluate_factors()
            elif self.tokens[self.pos][1] == "DIVIDE":
                self.pos += 1
                rez /= self.evaluate_factors()
            else:
                break
        return rez

    # Parse and evaluate the NUMBER and R,L PAREN expressions
    def evaluate_factors(self):
        if self.tokens[self.pos][1] == "NUMBER":
            result = float(self.tokens[self.pos][0])
            self.pos += 1
            return result
        elif self.tokens[self.pos][1] == "L PAREN":
            self.pos += 1
            result = self.evaluate_expression()
            if self.tokens[self.pos][1] != "R PAREN":
                raise Exception(f"Missing closing parenthesis")
            self.pos += 1
            return result
        else:
            raise Exception(f"Invalid syntax")
