from grammar import Grammar
from automaton import NFA_DFA
from chomskyform import ChomskyForm
from Parser import Parser
from lexer import lexer as getLexer


#Lab 1 -----------------------------------------------------------------------------------------------------
# Set of terminal symbols
# VT = {'a', 'b', 'c', 'd', 'e'}

# Set of non-terminal symbols
# VN = {'S', 'D', 'E', 'J'}

# Set of productions, rules or transitions
# P = {"S": ["aD"],"D": ["dE", "bJ", "aE"],"J": ["cS"],"E": ["eX", "aE"],"X": " " }

# Initiate the grammar calling the constructor with all 3 params
# grammar = Grammar.Grammar(VN, VT, P)

# Initiate the finite automaton
# finite_automaton = grammar.from_grammar_to_finite_automaton()

# Generate 5 string
# word_1 = grammar.generate_string()
# word_2 = grammar.generate_string()
# word_3 = grammar.generate_string()
# word_4 = grammar.generate_string()
# word_5 = grammar.generate_string()

# Print the strings including the  validation
# print("word_1 = {x} ".format(x = word_1) + " | " + str(finite_automaton.check_string(word_1)))
# print("word_2 = {x} ".format(x = word_2) + " | " + str(finite_automaton.check_string(word_2)))
# print("word_3 = {x} ".format(x = word_3) + " | " + str(finite_automaton.check_string(word_3)))
# print("word_4 = {x} ".format(x = word_4) + " | " + str(finite_automaton.check_string(word_4)))
# print("word_5 = {x} ".format(x = word_5) + " | " + str(finite_automaton.check_string(word_5)))


#Lab 2 -----------------------------------------------------------------------------------------------------
#Clasify grammar for Lab1
#grammar = Grammar.Grammar(VN, VT, P)
# classify the grammar based on Chomsky hierarchy
# get_classify = grammar.check_Grammar(P)

# print(f"Grammar clasification LAB1 :  {get_classify}")

# states = ['q0', 'q1', 'q2', 'q3', 'q4']
# alphabet = ['a', 'b']
# F = ['q3']
# start_state = 'q0'
# transitions =  {('q0', 'a'): {'q1'},
#                 ('q1', 'b'): {'q1','q2'},
#                 ('q2', 'b'): {'q0'},
#                 ('q3', 'a'): {'q4'},
#                 ('q4', 'a'): {'q0'},
#                 ('q2', 'a'): {'q3'},}

# Get the constructor with farams to  check the automation
# Automation = NFA_DFA.NFA_DFA(states, alphabet, F, start_state, transitions)

# Check if automaton is deterministic
# is_deterministic = Automation.check_deterministic()
# print(f"Is automaton deterministic? {is_deterministic}")
#
# # Convert NDFA to DFA
# dfa = Automation.NDFA_to_a_DFA()
# print(f" The states: {dfa.states}")
# print(f" The transition function: {dfa.transitions}")
# print(f" The initial state: {dfa.q0}")
# print(f" The final states: {dfa.F}")
#
# # Convert automaton to regular grammar
# grammar = Automation.finite_to_grammar()
# print(f"Regular grammar productions: {grammar}")


#Lab 3 -----------------------------------------------------------------------------------------------------

# Lexer running

# input = "(((40 ^ 2) + (80 / 2)  - (18 -5) * 4 ) % 67)"
# lexer = getLexer.Lexer(input)
# print("Token list : ")
# print("The generated tokens are : ",lexer.get_tokens())


#Lab 4 -----------------------------------------------------------------------------------------------------
# Varianta 8
# VN = {'S', 'A', 'B', 'C'}
# VT = {'a','d'}
# P = {
#     'S': {'dB', 'A'},
#     'A': {'d', 'dS', 'aAdAB'},
#     'B': {'a', 'aS', 'A', 'ε'},
#     'C': {'Aa'}
# }
#
# ChomskyForm.ChomskyForm(VN, VT, P).chomsky_normal_form()
#
# print("VN : " , VN)
# print("VT : ", VT)
# print("The product is : ", P)

#Lab 5 -----------------------------------------------------------------------------------------------------
Lexer = getLexer.Lexer("(7 - 2 * (10 - 8) + 31 ) /2")

tokens = Lexer.get_tokens()
parser = Parser.Parser(tokens)
prser = parser.parse_tokens()

print("The lexer", tokens)
print("The parser" , prser)

