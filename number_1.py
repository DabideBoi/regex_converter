from pythomata import SimpleDFA
def convert(string):
    alphabet = {"a", "b"}
    states = {"s1", "s2", "s3", "s4", "s5", "s6", "s7", "s8", "s9"}
    initial_state = "s1"
    accepting_states = {"s9"}
    transition_function = {
        "s1": {
            "b" : "s3",
            "a" : "s2"
        },
        "s2": {
            "b" : "s3",
            "a" : "s3"
        },
        "s3": {
            "b" : "s5",
            "a" : "s4"
        },
        "s4": {
            "b" : "s5",
            "a" : "s6"
        },
        "s5": {
            "b" : "s7",
            "a" : "s4"
        },
        "s6": {
            "b" : "s5",
            "a" : "s8"
        },
        "s7": {
            "b" : "s8",
            "a" : "s4"
        },
        "s8": {
            "b" : "s9",
            "a" : "s9"
        },
        "s9": {
            "b" : "s9",
            "a" : "s9"
        }
    
    }
    dfa = SimpleDFA(states, alphabet, initial_state, accepting_states, transition_function)
    word = "aaababbba"
    #word = "abbabaaaabab"
    #word = "bbaabbbbbabab"

    print(dfa.accepts(word))