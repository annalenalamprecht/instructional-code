import csv
import math
import sys


# simple hash function, likely to produce collisions
def h(x):
    
    # return first letter's position in the alphabet
    return ord(x[0].upper())-ord("A")


# another rather simple hash function, independent of h(x)
def h_prime(x):
    
    # calculate sum of the letter's alphabet positions
    s = 0
    for char in x:
        s += ord(char.upper())-ord("A")
    
    # return sum mod 29
    return s % 29



################
# MAIN PROGRAM #
################

if __name__ == "__main__":
    
    # initialize a list with 29 None values as (empty) hash table
    # (29: next prime number after 26 == number of characters in alphabet)
    hash_table = [None for x in range(0,29)]
    
    # read input data from CSV file, store as list of dictionaries
    input_data = []
    with open("people.csv") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            input_data.append(row)
    
    # ask user which method should be used
    method = input("Which collision resolution method do you want to use?\n" \
                   "1. no collision resolution\n" \
                   "2. chaining\n" \
                   "3. linear probing\n" \
                   "4. quadratic probing\n" \
                   "5. double hashing\n"\
                   )
        
    # init counter to track total number of collisions
    collision_count = 0
        
    # apply the selected method to fill the hash table
    if method == "1":
        
        # enter data without collision handling
        for record in input_data:
            last_name = record["last name"]
            entry = f"{record['first name']} {record['last name']} ({record['place']})"
            index = h(last_name)
            hash_table[index] = entry
            print(f"Inserted {entry} at index {index}.")
    
    elif method == "2":
        
        # enter data with collision detection and chaining
        for record in input_data:
            last_name = record["last name"]
            entry = f"{record['first name']} {record['last name']} ({record['place']})"
            index = h(last_name)
            
            # if the place in the table is empty, entry becomes first list element
            if hash_table[index] == None:
                hash_table[index] = [entry]
         
            # otherwise the new entry is appended to the list
            else:
                collision_count += 1
                hash_table[index].append(entry)
            
            print(f"Inserted {entry} at index {index}.")
    
    elif method == "3":
        
        # enter data with collision detection and linear probing
        for record in input_data:
            last_name = record["last name"]
            entry = f"{record['first name']} {record['last name']} ({record['place']})"
            index = h(last_name)
          
            # init local collision count
            i = 0
            
            # if the place in the table is free, enter entry directly
            if hash_table[index] == None:
                hash_table[index] = entry
            
            # otherwise perform linear probing until finding a free spot
            else:
                while hash_table[index] != None:
                    collision_count += 1
                    print(f"Collision at index {index} for {entry}.")
                    i += 1
                    index = (h(last_name) + i) % len(hash_table)
                
            hash_table[index] = entry
            print(f"Inserted {entry} at index {index}.")
            
    
    elif method == "4":
        
        # enter data with collision detection and quadratic probing
        for record in input_data:
            last_name = record["last name"]
            entry = f"{record['first name']} {record['last name']} ({record['place']})"
            index = h(last_name)
          
             # init local collision count
            i = 0
            
            # if the place in the table is free, enter entry directly
            if hash_table[index] == None:
                hash_table[index] = entry
            
            # otherwise perform quadratic probing until finding a free spot
            else:
                while hash_table[index] != None:
                    collision_count += 1
                    print(f"Collision at index {index} for {entry}.")
                    i += 1
                    index = ((h(last_name) + ((-1)**(i+1)) * (math.ceil(i/2)**2))) % len(hash_table)
                
            hash_table[index] = entry
            print(f"Inserted {entry} at index {index}.")
    
    elif method == "5":
        
        # enter data with collision detection and double hashing
        for record in input_data:
            last_name = record["last name"]
            entry = f"{record['first name']} {record['last name']} ({record['place']})"
            index = h(last_name)
          
            # init local collision count
            i = 0
            
            # if the place in the table is free, enter entry directly            
            if hash_table[index] == None:
                hash_table[index] = entry
            
            # otherwise perform double hashing until finding a free spot
            else:
                while hash_table[index] != None:
                    collision_count += 1
                    print(f"Collision at index {index} for {entry}.")
                    i += 1
                    index = (h(last_name) +  h_prime(last_name) * i) % len(hash_table)
                
            hash_table[index] = entry
            print(f"Inserted {entry} at index {index}.")
    
    else: 
        print("Invalid input, try again.")
        sys.exit(0)
    
    # print total collision stats
    print()
    print(f"{collision_count} collisions detected in total.")
    
    
    # print final hash table
    print()
    print("Hash table after inserting all data:")
    print()
        
    print("-"*40)
    for i in range(0,len(hash_table)):
        print(f"| {i}\t| {hash_table[i]}")
        print("-"*40)
