import itertools
import random
import string
import time

ONE_LETTER_LIMIT = 40000
TWO_LETTERS_LIMIT = 2000
THREE_LETTERS_LIMIT = 100
SEQUENCE_LIMIT = 1000000


def check_key(key, sequence_last):
    # triple key
    two_last_first = sequence_last + key[:1]
    last_two_first = sequence_last[-1] + key[:2]
    
    # double key
    last_first = sequence_last[-1] + key[0]
    firs_two = key[:2]
    last_two = key[-2:]
    
    # check triple values
    key_amount = occurrence_3.get(key)
    two_last_first_amount = occurrence_3.get(two_last_first)
    last_two_first_amount = occurrence_3.get(last_two_first)

    if key_amount is None:
        key_amount = occurrence_3.setdefault(key, 0)

    if two_last_first_amount is None:
        two_last_first_amount = occurrence_3.setdefault(two_last_first, 0)

    if last_two_first_amount is None:
        last_two_first_amount = occurrence_3.setdefault(last_two_first, 0)

    if key_amount >= THREE_LETTERS_LIMIT or two_last_first_amount >= THREE_LETTERS_LIMIT or last_two_first_amount >= THREE_LETTERS_LIMIT:
        return False

    #check double values
    last_first_amount = occurrence_2.get(last_first)
    firs_two_amount = occurrence_2.get(firs_two)
    last_two_amount = occurrence_2.get(last_two)

    if last_first_amount is None:
        last_first_amount = occurrence_2.setdefault(last_first, 0)

    if firs_two_amount is None:
        firs_two_amount = occurrence_2.setdefault(firs_two, 0)

    if last_two_amount is None:
        last_two_amount = occurrence_2.setdefault(last_two, 0)

    if last_first_amount >= TWO_LETTERS_LIMIT or firs_two_amount >= TWO_LETTERS_LIMIT or last_two_amount >= TWO_LETTERS_LIMIT:
        return False

    # single key
    first_amount = occurrence_1.get(key[0])
    second_amount = occurrence_1.get(key[1])
    third_amount = occurrence_1.get(key[2])

    if first_amount >= ONE_LETTER_LIMIT or second_amount >= ONE_LETTER_LIMIT or third_amount >= ONE_LETTER_LIMIT:
        return False

    # counters increment
    occurrence_3[key] += 1
    occurrence_3[two_last_first] += 1
    occurrence_3[last_two_first] += 1
    occurrence_2[last_first] += 1
    occurrence_2[firs_two] += 1
    occurrence_2[last_two] += 1
    occurrence_1[key[0]] += 1
    occurrence_1[key[1]] += 1
    occurrence_1[key[2]] += 1

    return True


letters = string.ascii_lowercase
permutation_2 = list(itertools.permutations(letters, 2))
permutation_3 = list(itertools.permutations(letters, 3))

occurrence_1 = {''.join(key): 0 for key in letters}
occurrence_2 = {''.join(key): 0 for key in permutation_2}
occurrence_3 = {''.join(key): 0 for key in permutation_3}

sequence = ['abc']
sequence_counter = 0

permutation_3_random = permutation_3[:]
random.shuffle(permutation_3_random)

while sequence_counter < SEQUENCE_LIMIT:
    for key in permutation_3_random:
        sequence_last = sequence[-1][1:]
        add_key = ''.join(key)

        if check_key(add_key, sequence_last):
            sequence.append(''.join(add_key))
            break

    sequence_counter += 3

sequence = ''.join(sequence[1:])

adjust = len(sequence) - SEQUENCE_LIMIT
sequence = sequence[:-adjust]

print(sequence)
print(len(sequence))
