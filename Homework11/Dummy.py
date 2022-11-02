table = {
    "SLEEP" : {"HIT" : "MAKE"},
    "MAKE" : {"TIMER10", "SLEEP"},
}


cur_state = "SLEEP"
next_state = table[cur_state]["HIT"]
