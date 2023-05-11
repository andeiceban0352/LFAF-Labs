# Determinism in Finite Automata. Conversion from NFA to DFA. Chomsky Hierarchy.
## Course: Formal Languages & Finite Automata
## Author: Andrei Ceban FAF-211
Variant 8

Q = {q0,q1,q2,q3,q4},

∑ = {a,b},

F = {q3},

δ(q0,a) = q1,

δ(q1,b) = q2,

δ(q2,b) = q0,

δ(q3,a) = q4,

δ(q4,a) = q0,

δ(q2,a) = q3,

δ(q1,b) = q1.


## Theory
A finite automaton is a mechanism used to represent processes of different kinds. It can be compared
to a state machine as they both have similar structures and purpose as well. The word finite signifies the
fact that an automaton comes with a starting and a set of final states. In other words, for process modeled
by an automaton has a beginning and an ending.

Based on the structure of an automaton, there are cases in which with one transition multiple states
can be reached which causes non determinism to appear. In general, when talking about systems theory the
word determinism characterizes how predictable a system is. If there are random variables involved, the
system becomes stochastic or non deterministic.

That being said, the automata can be classified as non-/deterministic, and there is in fact a possibility
to reach determinism by following algorithms which modify the structure of the automaton.
The process of converting a non-deterministic finite automaton (NFA) to a deterministic finite automaton (DFA) is known as the subset construction method. The idea is to construct a DFA whose states represent sets of states of the NFA, where the DFA’s transitions are determined by the transitions of the
NFA.

Determinism is an important concept in the theory of finite automata. A deterministic finite automaton (DFA) is a mathematical model used to recognize regular languages. It consists of a finite set of states, a finite set of input symbols (the alphabet), a transition function that maps each state and input symbol to a unique next state, a start state, and a set of accepting states.

The key property of a DFA is that for each input string, there is exactly one possible sequence of state transitions that the DFA can make. This means that the behavior of a DFA is completely determined by its current state and the input symbol it receives.


## Objectives:
- Understand what an automaton is and what it can be used for.

- Continuing the work in the same repository and the same project, the following need to be added:

  a. Provide a function in your grammar type/class that could classify the grammar based on Chomsky hierarchy.

  b. For this you can use the variant from the previous lab.

- According to your variant number (by universal convention it is register ID), get the finite automaton definition and do the following tasks:

  a. Implement conversion of a finite automaton to a regular grammar.

  b. Determine whether your FA is deterministic or non-deterministic.

  c. Implement some functionality that would convert an NDFA to a DFA.

  d. Represent the finite automaton graphically:
    - You can use external libraries, tools or APIs to generate the figures/diagrams.
    - Your program needs to gather and send the data about the automaton and the lib/tool/API return the visual representation.

## Implementation description
### check_deterministic
&ensp;&ensp;&ensp; This code checks whether the finite automaton represented by the object is deterministic or not. It does so by creating a transition map that maps the current state and input symbol to a set of next states. If any state in the automaton has multiple transitions for the same input symbol, then the automaton is non-deterministic and the method returns false. Otherwise, the automaton is deterministic and the method returns true. The method takes no arguments and returns a boolean value.

```
def check_deterministic(self):
    for state in self.states:
        for symbol in self.alphabet:
            next_states = self.transitions.get((state, symbol), set())
            if len(next_states) != 1:
                return False
    return True
```
### NDFA_to_a_DFA
&ensp;&ensp;&ensp; This code converts a non-deterministic finite automaton NFA to a deterministic finite automaton DFA. It does so by creating a power set of all possible states of the NFA, creating a new DFA transition table, and then using the transition table to create the DFA.
The method creates a power set of all possible states of the NFA by calling the "getPowerSet" method, which returns a set of sets representing all possible combinations of states. The method then creates a new DFA transition table by iterating over all state sets in the power set and creating a set of next states for each symbol in the alphabet by examining the possible transitions from each state in the current state set for each input symbol. Finally, the method creates a new DFA by initializing the new DFA with the transition table, final states, and initial state.

```
def NDFA_to_a_DFA(self):
    if self.check_deterministic():
        return self

    dfa_states = set()
    dfa_F = set()
    dfa_transitions = dict()
    state_queue = [frozenset([self.q0])]
    while state_queue:
        current_states = state_queue.pop(0)
        dfa_states.add(current_states)
        if any(state in self.F for state in current_states):
            dfa_F.add(current_states)
        for symbol in self.alphabet:
            next_states = set()
            for state in current_states:
                next_states |= set(self.transitions.get((state, symbol), set()))
            if next_states:
                next_states = frozenset(next_states)
                dfa_transitions[(current_states, symbol)] = next_states
                if next_states not in dfa_states:
                    state_queue.append(next_states)

    dfa = ChomskyHierarchy(self, self.alphabet, self.F, self.q0, self.transitions)
    dfa.states = dfa_states
    dfa.F = dfa_F
    dfa.transitions = dfa_transitions

return dfa
```

### isRegularGrammar
- The isRegularGrammar() method checks if the right-hand side of every production consists of either a single lowercase letter or two symbols where the first symbol is uppercase and the second is lowercase. If all productions satisfy this condition, then the grammar is regular.


```
def check_Context_sensitive(self, P):

    for symbol, string in P.items():
        for rhs in string:
            if len(rhs) < len(symbol):
                return False
            for i, symbol in enumerate(rhs):
                if symbol in P and i != len(rhs) - 1:
                    if len(rhs) <= len(symbol):
                        return False
    return True


```
### isContextFreeGrammar
- The isContextFreeGrammar() method checks if the left-hand side of every production is a single uppercase letter and the right-hand side consists of either uppercase or lowercase letters. If all productions satisfy this condition, then the grammar is context-free.


```
def check_Context_free(self, P):

    for symbol, string in P.items():
        if len(symbol) != 1 or not symbol.isupper():
            return False
        for rhs in string:
            for symbol in rhs:
                if symbol not in P and not symbol.islower():
                    return False
    return True
```

### isContextSensitiveGrammar
- The isContextSensitiveGrammar() method checks if the length of the left-hand side of every production is less than or equal to the length of the right-hand side. If all productions satisfy this condition, then the grammar is context-sensitive.

```
def check_Regular(self, P):

    for symbol, string in P.items():
        if not symbol.isupper():
            return False
        for rhs in string:
            if len(rhs) == 1 and rhs.islower():
                continue
            elif len(rhs) == 2 and rhs[0].islower() and rhs[1].isupper():
                continue
            else:
                return False
    return True
```



## Results
![Alt text](screenshots/lab2.png)
## Conclusions
&ensp;&ensp;&ensp; After doing this laboratory work,i understand that determinism in finite automata is an important
concept in computer science that refers to the ability of a machine to uniquely determine its next state
based on the current input and state. Deterministic finite automata (DFA) are particularly useful for pattern
recognition and language processing tasks, as they can efficiently recognize regular languages.

The process of converting a non-deterministic finite automaton (NDFA) to a DFA involves transforming the NDFA into a deterministic version of itself, where each input symbol leads to exactly one next state. This conversion is important for simplifying the machine and making it easier to analyze and
understand.

Also, using the Chomsky hierarchy which is a classification of formal languages into four categories
based on their complexity and the types of grammars that can generate them. These categories include regular languages, context-free languages, context-sensitive languages, and recursively enumerable languages.
Each category has its own set of rules and limitations, and understanding these categories can help in the
design and analysis of computational systems.
   
