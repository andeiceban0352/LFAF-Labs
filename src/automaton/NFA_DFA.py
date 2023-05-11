class NFA_DFA:
    #initiate the constructor to set the parameters
    def __init__(self, states, alphabet, F, q0, transitions):
        self.states = states
        self.alphabet = alphabet
        self.F = F
        self.q0 = q0
        self.transitions = transitions

    #Determine whether your FA is deterministic or non-deterministic
    def check_deterministic(self):
        for state in self.states:
            for symbol in self.alphabet:
                next_states = self.transitions.get((state, symbol), set())
                if len(next_states) != 1:
                    return False
        return True

    #Implement some functionality that would convert an NDFA to a DFA
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

    # Implement conversion of a finite automaton to a regular grammar.
    def finite_to_grammar(self):
        product = dict()
        for state in self.states:
            for symbol in self.alphabet:
                next_states = self.transitions.get((state, symbol), set())
                for next_state in next_states:
                    if next_state in self.F:
                        if state not in product:
                            product[state] = set()
                        product[state].add(symbol)
                    else:
                        if next_state not in product:
                            product[next_state] = set()
                        product[next_state].add(symbol + state)
        start_symbol = self.q0
        if start_symbol in product:
            product['S'] = product[start_symbol]
            del product[start_symbol]
            for state in self.states:
                for symbol in self.alphabet:
                    next_states = self.transitions.get((state, symbol), set())
                    for next_state in next_states:
                        if state in product and symbol + state in product[state]:
                            if next_state not in product:
                                product[next_state] = set()
                            product[next_state].add(symbol + 'S')
        else:
            start_symbol = 'S'
            product[start_symbol] = set()
            for FF in self.F:
                product[start_symbol].add('eps' + FF)

        return start_symbol, product