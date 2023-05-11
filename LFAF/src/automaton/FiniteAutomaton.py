class FiniteAutomaton:
    # Constructor of Finite_Automaton class
    def __init__(self, Q, Sigma, arr, q0, F):
        self.Q = Q
        self.Sigma = Sigma
        self.arr = arr
        self.q0 = q0
        self.F = F

    # Check the word if is valid
    def check_string(self, word):
        index = 0
        # Set the current state to the initial state
        Q0 = self.q0

        # For each character in the word, find the next state using the arr function
        for character in word:
            if ((Q0[0], character) in self.arr) and (index != len(word)-1):
                Q0 = self.arr[(Q0[0], character)]
            elif index == len(word) - 1:
                if len(Q0) > 1:
                    # If the current state is in the set of final states (X), return True, else return False
                    if Q0[len(Q0)-1] in self.F:
                        return True
                    else:
                        return False
                else:
                    if Q0[0] in self.F:
                        return True
                    else:
                        return False
            index = index + 1