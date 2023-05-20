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


## Theory
&ensp;&ensp;&ensp; Parsing, syntax analysis, or syntactic analysis is the process of analyzing a string of symbols, either in natural language, computer languages or data structures, conforming to the rules of a formal grammar. The term parsing comes from Latin pars (orationis), meaning part (of speech).

&ensp;&ensp;&ensp; The term has slightly different meanings in different branches of linguistics and computer science. Traditional sentence parsing is often performed as a method of understanding the exact meaning of a sentence or word, sometimes with the aid of devices such as sentence diagrams. It usually emphasizes the importance of grammatical divisions such as subject and predicate.

&ensp;&ensp;&ensp; Within computational linguistics the term is used to refer to the formal analysis by a computer of a sentence or other string of words into its constituents, resulting in a parse tree showing their syntactic relation to each other, which may also contain semantic and other information (p-values).[citation needed] Some parsing algorithms may generate a parse forest or list of parse trees for a syntactically ambiguous input.

&ensp;&ensp;&ensp; The term is also used in psycholinguistics when describing language comprehension. In this context, parsing refers to the way that human beings analyze a sentence or phrase (in spoken language or text) "in terms of grammatical constituents, identifying the parts of speech, syntactic relations. This term is especially common when discussing which linguistic cues help speakers interpret garden-path sentences.

&ensp;&ensp;&ensp; Within computer science, the term is used in the analysis of computer languages, referring to the syntactic analysis of the input code into its component parts in order to facilitate the writing of compilers and interpreters. The term may also be used to describe a split or separation.

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
&ensp;&ensp;&ensp; In conclusion, the laboratory work on parsers and lexers has provided valuable insights into the fundamental concepts and techniques used in language processing. Through the implementation and utilization of both lexer and parser components, we have gained a deeper understanding of how programming languages are analyzed and interpreted.

&ensp;&ensp;&ensp;  The lexer, or lexical analyzer, played a crucial role in the laboratory work by breaking down the input program into a sequence of tokens. It effectively identified and categorized the different components such as keywords, identifiers, operators, and literals, which served as the building blocks for further analysis. By implementing the lexer, we were able to appreciate the importance of tokenization and how it facilitates subsequent parsing.

&ensp;&ensp;&ensp;  The parser, on the other hand, took the token stream produced by the lexer and organized it into a structured representation, typically an abstract syntax tree (AST). Through the application of parsing algorithms like LL(1), LR(1), or recursive descent, we were able to handle the grammar rules and enforce syntactic correctness. The parser acted as a vital component in the language processing pipeline, enabling the analysis and manipulation of the input program's structure.

&ensp;&ensp;&ensp; Working on the laboratory assignment allowed us to apply our theoretical knowledge in a practical context. We implemented both the lexer and parser, grasping the challenges involved in designing efficient algorithms that can handle various grammatical constructs and error handling scenarios. This hands-on experience was invaluable in reinforcing our understanding of how lexers and parsers work in tandem to process programming languages.




## References:
[1] [Parser](https://en.wikipedia.org/wiki/Parsing)
