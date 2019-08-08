#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve,
                        )


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)
    if length < 2:
        return None

    for i,weight in enumerate(weights):
        hash_table_insert(ht,weight,i)

    for i,weight in enumerate(weights):
    
        node = hash_table_retrieve(ht,limit - weight)
        if node is not None:
            if node > i:
                answer = (node,i)
            elif node < i:
                answer = (i,node)
    
    """
    YOUR CODE HERE
    """

    return answer


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
