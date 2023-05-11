import random
from LFAF.src.automaton import FiniteAutomaton

class Grammar:
    # Constructor of Grammar class
    def __init__(self, VN, VT, P):
        self.VT = VT
        self.VN = VN
        self.P = P

    # Generate the strings
    def generate_string(self):
        # Start of the string
        string = "S"
        # Set of final states
        final_state = " "

        # Create a random string
        while string[-1] not in final_state:
            arr = []
            #go trough items and get the keys and values
            for key, value in self.P.items():
                if key == string[-1]:
                    #move the value in array
                    arr += value
            if not arr:
                return None
            production = random.choice(arr)
            #Reverse string, count backwards
            string = string[:-1] + production
        return string

    # Convert from grammar to finite automaton, sending all the params with self
    def from_grammar_to_finite_automaton(self):
        # Initiate finite set of states
        Q = set(self.VN)
        # Initiate the alphabet with all the characters
        Sigma = set(self.VT)
        # Initiate the initial state from the list
        q0 = "S"
        # Initiate the set of final states from the list
        F = "X"
        # Initiate the transition function
        arr = {}
        for key, value in self.P.items():
            for symbol in value:
                if (key, symbol[0]) in arr :
                    arr[(key, symbol[0])].append(symbol[1:])
                else:
                    arr[(key, symbol[0])] = [symbol[1:]]
        print("Automation :", arr)

        # Call the constructor of Finite Automaton with all the params
        return FiniteAutomaton.FiniteAutomaton(Q, Sigma, arr, q0, F)

    def check_Grammar(self, P):
        if self.check_Context_free(P):
            return "Type context free"
        if self.check_Context_sensitive(P):
            return "Type context sensitive"

        if self.check_Regular(P):
            return "Type regular"

        if self.check_Unrestricted(P):
            return "Type unrestricted"

        return "Not in Chomsky Hierarchy"

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

    def check_Context_free(self, P):

        for symbol, string in P.items():
            if len(symbol) != 1 or not symbol.isupper():
                return False
            for rhs in string:
                for symbol in rhs:
                    if symbol not in P and not symbol.islower():
                        return False
        return True

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

    def check_Unrestricted(self, P):
        return True