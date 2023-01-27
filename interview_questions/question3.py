"""
# Function to get keys of dictionary in reverse sorted order of values.
(Note: Feel free to use python builtin functions)
"""


def get_values(data):
    # get the values in reverse sorted order
    values = sorted(list(data.values()), reverse=True) 

    # get the keys corresponding to values
    keys = [] 
    for value in values: 
        for key in data.keys(): 
            if value == data[key]: 
                keys.append(key) 
  
    return keys


if __name__ == '__main__':
    case1 = get_values({'a':1234, 'b':111, 'c':2345})
    print(case1)
    assert case1 == ['c', 'a', 'b']
    case2 = get_values({'a':5, 'b':10, 'c':-2, 'd': 0, 'e': 0 })
    print(case2)
    case2 == ['b', 'a', 'd',  'e',  'c']
    print('Success')
