from pythomata import SimpleDFA
alphabet = {"1", "0"}
states = {"s1", "s2", "s3", "s4", "s5", "s6", "s7", "s8", "s9"}
initial_state = "s1"
accepting_states = {"s9"}
transition_function = {
    "s1": {
        "1" : "s3",
        "0" : "s2"
    },
    "s2": {
        "1" : "s4",
        "0" : "s5"
    },
    "s3": {
        "1" : "s5",
        "0" : "s4"
    },
    "s4": {
        "1" : "s5",
        "0" : "s5"
    },
    "s5": {
        "1" : "s6",
        "0" : "s7"
    },
    "s6": {
        "1" : "s8",
        "0" : "s7"
    },
    "s7": {
        "1" : "s6",
        "0" : "s8"
    },
    "s8": {
        "1" : "s9",
        "0" : "s9"
    },
    "s9": {
        "1" : "s9",
        "0" : "s9"
    },
}
dfa = SimpleDFA(states, alphabet, initial_state, accepting_states, transition_function)
#word = "aaababbba"
word = "abbabaaaabab"
#word = "bbaabbbbbabab"

print(dfa.accepts(word))