# Topic: Parser & Building an Abstract Syntax Tree

### Course: Formal Languages & Finite Automata
### Author: Andrei Ceban FAF-211

----

## Objectives:
1. Get familiar with parsing, what it is and how it can be programmed [1].
2. Get familiar with the concept of AST.
3. In addition to what has been done in the 3rd lab work do the following:
   1. In case you didn't have a type that denotes the possible types of tokens you need to:
      1. Have a type __*TokenType*__ (like an enum) that can be used in the lexical analysis to categorize the tokens. 
      2. Please use regular expressions to identify the type of the token.
   2. Implement the necessary data structures for an AST that could be used for the text you have processed in the 3rd lab work.
   3. Implement a simple parser program that could extract the syntactic information from the input text.


## Implementation 

&ensp;&ensp;&ensp;  The objective of the "parse_tokens" function is to analyze a series of tokens and compute the value of the expression they represent. Once the evaluation is done, the code verifies if there are any remaining tokens for further processing. If any tokens are found, it throws an exception indicating that the syntax is invalid.


```python
    def parse_tokens(self):
        rez = self.evaluate_expression()
        if self.pos < len(self.tokens):
            raise Exception(f"Invalid syntax")
        return rez
 ```
 

&ensp;&ensp;&ensp; The objective of the "evaluate_expression" function is to analyze and compute a mathematical expression. It begins by invoking the "term" function to calculate the value of the initial term in the expression. The "expr" function proceeds to evaluate the arithmetic expression from left to right, considering both addition and subtraction operations.

```python
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
 ```
&ensp;&ensp;&ensp;   The objective of the "evaluate_term" function is the same as the objective of "evaluate_expression" method but is specifically designed for handling different arithmetic calculations. It starts by invoking the "evaluate_factors" method to evaluate the initial factor within the term. The "term" method carries out a sequential evaluation of a term in an arithmetic expression, considering multiplication and division operations. It processes the factors from left to right.
```python
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
```

### remove_inaccessible_symbols()
&ensp;&ensp;&ensp;  The "evaluate_factors" function's goal is to evaluate and parse the factors contained in an arithmetic statement. Factors can be either parenthesized subexpressions or numerical numbers. The token indicates a numerical value when it is of the "Digit" type. When the token is of the "LeftP" type, it denotes the start of a parenthesized subexpression. As the location is increased, the code invokes the expr method recursively to evaluate the expression enclosed in parentheses. The next token should be a "RightP" type, indicating the closing parenthesis. If it is not, an exception is raised to indicate a missing closing parenthesis. If the current token does not match either "Digit" or "LeftP", it signifies an invalid syntax. In such cases, the code raises an exception with a descriptive message indicating the invalid token encountered.
```python
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
```


## Results
```
The lexer 
[('(', 'L PAREN'), ('7', 'NUMBER'), ('-', 'MINUS'), ('2', 'NUMBER'), ('*', 'TIMES'), ('(', 'L PAREN'), ('10', 'NUMBER'), ('-', 'MINUS'), ('8', 'NUMBER'), (')', 'R PAREN'), ('+', 'ADDITION'), ('31', 'NUMBER'), (')', 'R PAREN'), ('/', 'DIVIDE'), ('2', 'NUMBER')]

The parser = 17.0

```

## Conclusions
&ensp;&ensp;&ensp; After doing this laboratory work, i understand that normalizing a grammar is the process of converting it into a standard form or normal form, which can make it easier to analyze and manipulate the grammar. Chomsky Normal Form (CNF) is a specific normal form for context-free grammars, which involves converting each production rule to either have two nonterminal symbols or one terminal symbol. 

&ensp;&ensp;&ensp; CNF has several advantages, including simplifying the grammar and making it easier to analyze, parse, or generate sentences in the language. However, converting a grammar to CNF can sometimes be a complex process, and may not always be possible for some grammars. Nevertheless, normalizing a grammar is an important technique in formal language theory, and can be applied to different types of grammars, depending on their characteristics and requirements.

&ensp;&ensp;&ensp; The time complexity of this process is generally O(n^3), where n is the number of nonterminal symbols in the grammar. However, more efficient algorithms can be used to achieve a better time complexity, such as the CYK algorithm, which has a time complexity of O(n^3 * log n) for converting a CFG to CNF.


## References:
[1] [Parser](https://en.wikipedia.org/wiki/Parsing)
