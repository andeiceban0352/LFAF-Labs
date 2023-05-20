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

&ensp;&ensp;&ensp; This piece of code searches for epsilon productions within a grammar. Epsilon productions refer to production rules that map a non-terminal symbol to an empty string. The code performs the following steps for each non-terminal symbol in the grammar:


```python
    def parse_tokens(self):
        rez = self.evaluate_expression()
        if self.pos < len(self.tokens):
            raise Exception(f"Invalid syntax")
        return rez
 ```
 

&ensp;&ensp;&ensp; The given code loops through every symbol in the grammar and obtains the group of productions connected to that symbol. It examines each production and determines if it includes an empty string (epsilon). When an epsilon string is found, the code generates a fresh production by substituting the empty string with nothing. This new production is subsequently appended to the group of productions associated with the same symbol.

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
&ensp;&ensp;&ensp;  This code is a part of an algorithm used to find the set of all unreachable nonterminals in a context-free grammar. The algorithm uses a set reachable to keep track of all the nonterminals that are reachable from the start symbol of the grammar. The while loop keeps iterating until no new nonterminals are added to reachable in an iteration. The changed variable is used to keep track of whether any new nonterminals were added to reachable in the current iteration. In each iteration, the loop goes through all the nonterminals in the grammar, and for each nonterminal nonterm, it checks whether it is already in reachable. If it is, then it looks at each of its production rules prod, and for each symbol in the production rule, it checks whether it is a nonterminal.
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
&ensp;&ensp;&ensp; This function is designed to eliminate nonterminal symbols that cannot be reached from the starting symbol of a grammar, as well as discard productions that cannot be reached from the starting symbol. The code examines nonterminal symbols that are not reachable from the starting symbol by iterating through each symbol in the 'inaccessible' set and deleting all associated productions from the 'P' dictionary. The nonterminal symbol is also removed from the 'V_N' set. Additionally, the code identifies productions that are unreachable from the starting symbol. It iterates through each nonterminal symbol in the 'P' dictionary and generates a new set of productions that only includes those with symbols that are either reachable or terminals. This new set replaces the original set of productions for that nonterminal symbol.
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
