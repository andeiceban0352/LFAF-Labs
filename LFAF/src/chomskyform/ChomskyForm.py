class ChomskyForm:
    # Constructor of ChomskyForm class
    def __init__(self, VN, VT, P):
        self.VT = VT
        self.VN = VN
        self.P = P

    def chomsky_normal_form(self):
        # Step 1: Remove unit productions
        self.remove_unit_productions()

        # Step 2: Remove inaccessible symbols
        self.remove_inaccessible_symbols()

        # Step 3: Convert long productions to Chomsky normal form
        self.convert_long_productions_to_cnf()

        # Step 4: Remove epsilon productions
        self.remove_epsilon_productions()

        # Step 5: Return the resulting grammar
        return self.VN, self.VT, self.P

    def remove_unit_productions(self):
        # Remove unit productions
        reachable = {'S'}
        for symbol in list(self.P):
            productions = list(self.P[symbol])
            for production in productions:
                if len(production) == 1 and production.isupper():
                    self.P[symbol].remove(production)
                    self.P[symbol].update(self.P[production])

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

    def remove_epsilon_productions(self):
        # Remove epsilon productions
        epsilon_productions = []
        for symbol in list(self.P):
            productions = list(self.P[symbol])
            for production in productions:
                if production == 'ε':
                    epsilon_productions.append((symbol, production))
                    self.P[symbol].remove(production)