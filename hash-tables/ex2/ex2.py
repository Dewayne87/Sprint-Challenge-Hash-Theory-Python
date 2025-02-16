#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve,
                        )


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length
    for ticket in tickets:
        hash_table_insert(hashtable,ticket.source,ticket.destination)
    
    key = 'NONE'

    for i in range(length):
        curr_tick = hash_table_retrieve(hashtable, key)
        route[i] = curr_tick
        key = curr_tick
    """
    YOUR CODE HERE
    """
    print(route)
    return route
