from typing import List
import random

def python_shuffle(array: List[any]) -> List[any]:
    # shuffle the arry using python random shuffle function
    shuffled_list = random.sample(array, len(array))
    return shuffled_list

def api_suffle(array: List[any]) -> List[any]:
    #TODO call the api to shuffle the array 
    return array.copy()


def insert_item(S: List[any], item: any) -> None:
    """_summary_
    
    Example data: S = (D34, D23, D45), item = D12
    
    Step1: Toss (random 0/1) 0=left, 1 right (ex - 0)
    
    Step2: Shuffle S, take first data (ex - D45)
    
    Step3: Place item based on toss in S - (D34, D23, D12, D45) = final

    Args:
        S (List[any]): The list to insert the item into
        item (any): The item to be inserted
    """
    # Step 1: toss (0/1) 0 = left, 1 = right
    toss = random.choice([0, 1])
    
    # Step 2:
    # shuffle currenct S array
    S_shuffled = python_shuffle(S)
    
    # pick the first value
    first = S_shuffled[0]
    
    # Step 3: insert the data
    #find the position to insert
    pos = S.index(first) + toss
    
    #insert the data
    S.insert(pos, item)
    
    

def final_shuffle(S: List[any]) -> List[any]:
    """_summary_
    
            -------Take series of N data - S
        Shuffle using shuffling function
        Take the first data (ex - D45) - S1
        Take second data (ex - D34)
        Toss (random 0/1) 0=left, 1 right (ex -0)
        Place second data based on toss- S2 - (D34, D45)
        Take third data (ex - D23)
        Toss (random 0/1) 0=left, 1 right (ex - 0)
        Shuffle S2, take first data (ex - D45)
        Place based on toss in S2 - (D34, D23, D45) = S3 
        Take 4th data (ex - D12)
        Toss (random 0/1) 0=left, 1 right (ex - 1)
        Shuffle S3, take first data (ex - D23)
        Place based on toss in S3 - (D34, D23, D12, D45) = S4 
        Take 5th data (ex - D39)
        Toss (random 0/1) 0=left, 1 right (ex - 0)
        Shuffle S4, take first data (ex - D45)
        Place based on toss in S4 - (D34, D23, D12, D39, D45) = S5 
        Repeat N times

    Args:
        S (List[any]): the series to shuffle

    Returns:
        List[any]: the final shuffled array
    """
    
    # Shuffle S using the right shuffle function
    shuffled_data = python_shuffle(S)
    
    # Insert the first data item to the result
    res = [shuffled_data[0]]
    
    # Iterate through each data one by one and insert using the rule described above
    # Skip the first value since it is trivialy inserted in the result above
    for idx in range(1, len(shuffled_data)):
        # Get the item at that index
        item = shuffled_data[idx]
        
        # call the insert function for each data point that implements the above logic
        insert_item(res, item)
    
    return res