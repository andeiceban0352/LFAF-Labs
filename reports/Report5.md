# Topic: Chomsky Normal Form

### Course: Formal Languages & Finite Automata
### Author: Andrei Ceban FAF-211

----

## Objectives:
1. Learn about Chomsky Normal Form (CNF) [1].
2. Get familiar with the approaches of normalizing a grammar.
3. Implement a method for normalizing an input grammar by the rules of CNF.
    1. The implementation needs to be encapsulated in a method with an appropriate signature (also ideally in an appropriate class/type).
    2. The implemented functionality needs executed and tested.
    3. A BONUS point will be given for the student who will have unit tests that validate the functionality of the project.
    4. Also, another BONUS point would be given if the student will make the aforementioned function to accept any grammar, not only the one from the student's variant.



## Theory
&ensp;&ensp;&ensp; Chomsky Normal Form (CNF) is a specific form of a context-free grammar (CFG), which is a set of production rules that define a formal language. In CNF, each production rule is of the form:
    A → BC or A → a
where A, B, and C are nonterminal symbols (symbols that can be replaced by a sequence of symbols) and a is a terminal symbol (a symbol that cannot be replaced).   

&ensp;&ensp;&ensp; To convert a grammar to Chomsky normal form, a sequence of simple transformations is applied in a certain order; this is described in most textbooks on automata theory. The presentation here follows Hopcroft, Ullman (1979), but is adapted to use the transformation names from Lange. Each of the following transformations establishes one of the properties required for Chomsky normal form.

&ensp;&ensp;&ensp; Normalizing a grammar is the process of converting it into a standard form or normal form, which can make it easier to analyze and manipulate the grammar. There are different types of normal forms depending on the type of grammar being used. Normalizing a grammar can be useful for several reasons, such as simplifying the grammar, making it easier to generate or parse sentences in the language, and for theoretical analysis of the grammar's properties.

&ensp;&ensp;&ensp; Chomsky Normal Form (CNF) is a normal form for context-free grammars, as explained in the previous answer. Another normal form for context-free grammars is Greibach Normal Form (GNF), where each production rule is of the form:

A → aB1B2...Bk

where A is a nonterminal symbol, a is a terminal symbol, and B1, B2, ..., Bk are nonterminal symbols. In other words, the right-hand side of each production rule starts with a single terminal symbol followed by any number of nonterminal symbols.



## Implementation 

&ensp;&ensp;&ensp; This piece of code searches for epsilon productions within a grammar. Epsilon productions refer to production rules that map a non-terminal symbol to an empty string. The code performs the following steps for each non-terminal symbol in the grammar:

It retrieves all the production rules associated with the symbol using the expression 'P[symbol]'. This expression returns a set of strings representing all the possible productions for that non-terminal.

It iterates through each production rule for the given non-terminal symbol using the loop 'for production in productions'.

For each production rule, it checks if the current production is an epsilon production by comparing the value of 'production' to the string 'ε'.

If the current production is an epsilon production, the code adds the tuple '(symbol, production)' to a list called 'epsilon_productions'. This tuple signifies that the non-terminal symbol can produce an empty string.

Furthermore, the code removes the epsilon production from the set of productions for that non-terminal using 'P[symbol].remove(production)'. This step ensures that the grammar adheres to Chomsky normal form, which disallows epsilon productions.

```python
        epsilon_productions = []
        for symbol in list(self.P):
            productions = list(self.P[symbol])
            for production in productions:
                if production == 'ε':
                    epsilon_productions.append((symbol, production))
                    self.P[symbol].remove(production)
 ```
 

&ensp;&ensp;&ensp; The given code loops through every symbol in the grammar and obtains the group of productions connected to that symbol. It examines each production and determines if it includes an empty string (epsilon). When an epsilon string is found, the code generates a fresh production by substituting the empty string with nothing. This new production is subsequently appended to the group of productions associated with the same symbol.

```python
    for symbol in list(self.P):
            productions = list(self.P[symbol])
            for production in productions:
                for epsilon in epsilon_productions:
                    new_production = production.replace(epsilon[0], '')
                    if new_production != production:
                        self.P[symbol].add(new_production)
 ```
&ensp;&ensp;&ensp;  This code is a part of an algorithm used to find the set of all unreachable nonterminals in a context-free grammar. The algorithm uses a set reachable to keep track of all the nonterminals that are reachable from the start symbol of the grammar. The while loop keeps iterating until no new nonterminals are added to reachable in an iteration. The changed variable is used to keep track of whether any new nonterminals were added to reachable in the current iteration. In each iteration, the loop goes through all the nonterminals in the grammar, and for each nonterminal nonterm, it checks whether it is already in reachable. If it is, then it looks at each of its production rules prod, and for each symbol in the production rule, it checks whether it is a nonterminal.
```python
    # Find reachable symbols
    changed = True
    while changed:
        changed = False
        for nonterm, productions in self.P.items():
            if nonterm in reachable:
                for prod in productions:
                    for symbol in prod:
                        if symbol in self.VN:
                            if symbol not in reachable:
                                reachable.add(symbol)
                                changed = True
    
    # Remove symbols that are not reachable from the start symbol
    inaccessible = self.VN - reachable
    for nonterm in inaccessible:
        del self.P[nonterm]
        self.VN.remove(nonterm)
```

### remove_inaccessible_symbols()
&ensp;&ensp;&ensp; This function is designed to eliminate nonterminal symbols that cannot be reached from the starting symbol of a grammar, as well as discard productions that cannot be reached from the starting symbol. The code examines nonterminal symbols that are not reachable from the starting symbol by iterating through each symbol in the 'inaccessible' set and deleting all associated productions from the 'P' dictionary. The nonterminal symbol is also removed from the 'V_N' set. Additionally, the code identifies productions that are unreachable from the starting symbol. It iterates through each nonterminal symbol in the 'P' dictionary and generates a new set of productions that only includes those with symbols that are either reachable or terminals. This new set replaces the original set of productions for that nonterminal symbol.
```python
def remove_inaccessible_symbols(self):
    # Find reachable symbols
    reachable = {'S'}
    changed = True
    while changed:
        changed = False
        for nonterm, productions in self.P.items():
            if nonterm in reachable:
                for prod in productions:
                    for symbol in prod:
                        if symbol in self.VN:
                            if symbol not in reachable:
                                reachable.add(symbol)
                                changed = True
    
    # Remove symbols that are not reachable from the start symbol
    inaccessible = self.VN - reachable
    for nonterm in inaccessible:
        del self.P[nonterm]
        self.VN.remove(nonterm)
```

### convert_long_productions_to_cnf()
&ensp;&ensp;&ensp; The function goes through each symbol in the production rules of the grammar, one by one. For every symbol, it checks whether any of its productions consist of more than two symbols. If a production exceeds two symbols, the program generates new intermediate symbols to divide the production into smaller segments. To name these intermediate symbols, the code starts with 'X' and appends an increasing index number. Subsequently, for each symbol in the production that has more than two symbols, the code introduces an intermediate symbol and includes it in the production rule. This intermediate symbol serves as a replacement for the original symbol in the production rule. Finally, the code removes the original production rule with more than two symbols and substitutes it with a new production rule that employs the intermediate symbols. Consequently, the resulting grammar will contain only two symbols on the right-hand side of each production rule.

```python
def convert_long_productions_to_cnf(self):
    # Convert long productions to Chomsky normal form
    new_symbol_index = 0
    for symbol in list(self.P):
        productions = list(self.P[symbol])
        for production in productions:
            if len(production) > 2:
                new_symbol = f'X{new_symbol_index}'
                new_symbol_index += 1
                self.P[new_symbol] = set()
                self.P[new_symbol].add(production[0])
                for i in range(1, len(production) - 1):
                    intermediate_symbol = f'X{new_symbol_index}'
                    new_symbol_index += 1
                    self.P[intermediate_symbol] = set()
                    self.P[intermediate_symbol].add(production[i])
                    self.P[new_symbol].add(intermediate_symbol)
                    self.VN.add(intermediate_symbol)
                self.P[new_symbol].add(production[-1])
                self.P[symbol].remove(production)
                self.P[symbol].add(new_symbol)
                self.VN.add(new_symbol)
```

### remove_epsilon_productions()
&ensp;&ensp;&ensp; This function removes epsilon productions from a context-free grammar. It iterates over all non-terminals and their productions, and removes any production that consists only of the empty string (ε). It also keeps track of the removed productions in a list.

```python
def remove_epsilon_productions(self):
    # Remove epsilon productions
    epsilon_productions = []
    for symbol in list(self.P):
        productions = list(self.P[symbol])
        for production in productions:
            if production == 'ε':
                epsilon_productions.append((symbol, production))
                self.P[symbol].remove(production)
```

## Results
```
Grammar in Chomsky normal form:

VN :  {'X5', 'X6', 'B', 'X7', 'X1', 'X9', 'X4', 'X10', 'X3', 'X0', 'X2', 'X11', 'X8', 'S', 'A'}
VT :  {'d', 'a'}
P :  {'S': {'X0', 'dB', 'dS', 'd'}, 'A': {'d', 'dS', 'X4'}, 'B': {'aS', 'a', 'dS', 'X8', 'd'}, 'X0': {'B', 'a', 'X1', 'X3', 'X2'}, 'X1': {'A'}, 'X2': {'d'}, 'X3': {'A'}, 'X4': {'X5', 'X6', 'B', 'a', 'X7'}, 'X5': {'A'}, 'X6': {'d'}, 'X7': {'A'}, 'X8': {'B', 'a', 'X9', 'X10', 'X11'}, 'X9': {'A'}, 'X10': {'d'}, 'X11': {'A'}}

```

## Conclusions
&ensp;&ensp;&ensp; After doing this laboratory work, i understand that normalizing a grammar is the process of converting it into a standard form or normal form, which can make it easier to analyze and manipulate the grammar. Chomsky Normal Form (CNF) is a specific normal form for context-free grammars, which involves converting each production rule to either have two nonterminal symbols or one terminal symbol. 

&ensp;&ensp;&ensp; CNF has several advantages, including simplifying the grammar and making it easier to analyze, parse, or generate sentences in the language. However, converting a grammar to CNF can sometimes be a complex process, and may not always be possible for some grammars. Nevertheless, normalizing a grammar is an important technique in formal language theory, and can be applied to different types of grammars, depending on their characteristics and requirements.

&ensp;&ensp;&ensp; The time complexity of this process is generally O(n^3), where n is the number of nonterminal symbols in the grammar. However, more efficient algorithms can be used to achieve a better time complexity, such as the CYK algorithm, which has a time complexity of O(n^3 * log n) for converting a CFG to CNF.


## References:
[1] [Chomsky Normal Form Wiki](https://en.wikipedia.org/wiki/Chomsky_normal_form)
