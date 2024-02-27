import random
# generate function to generate random list of dictionary
def generate_random_dict():
    random_dict=[]
    random_dict_list=random.randint(2,10)
    #print(random_dict_list)
    for _ in range(random_dict_list):
        new_dict={}
        #print(new_dict)
        num_keys=random.randint(1,5)
        #print(num_keys)
        for _ in range(num_keys):
            key=chr(random.randint(97,122))
            #print(key)
            value=random.randint(1,100)
            #print(value)
            new_dict[key]=value
        random_dict.append(new_dict)
        #print(random_dict)
    return random_dict
random_list_of_dicts = generate_random_dict()

#print the random list of dictionaries
print("random list of dictionaries:")
print(random_list_of_dicts)

