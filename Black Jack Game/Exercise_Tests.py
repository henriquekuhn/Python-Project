#Checking the number of ones in sublists of a DICTIONARY
hand = {'a': [1, 2, 3], 'b': [1, 2]}
num_of_ones_dict = sum(sublist.count(1) for sublist in hand.values() if isinstance(sublist, list))
print(f'number of ones {num_of_ones_dict}')

#Checking the number of ones in a LIST
hand = [1, 2, 3, 1]
num_of_ones_list = hand.count(1)
print(f'number of ones {num_of_ones_list}')