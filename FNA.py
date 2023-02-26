class State:
    def __init__(self, isEnd=False, transition=None, epsilonTransitions=None):
        if transition is None:
            transition = {}
        if epsilonTransitions is None:
            epsilonTransitions = []
        self.isEnd = isEnd
        self.transition = transition
        self.epsilonTransitions = epsilonTransitions

    def __str__(self):
        transition_str = ", ".join(
            f"{char} -> {state}" for char, state in self.transition.items())
        epsilon_str = ", ".join(str(state)
                                for state in self.epsilonTransitions)
        return f"State(transition={{ {transition_str} }}, epsilon={{ {epsilon_str} }}, isEnd={self.isEnd})"
