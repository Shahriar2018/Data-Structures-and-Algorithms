"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

print("These numbers could be telemarketers: ")

calling_numbers=set()
receving_numbers=set()
text_sending=set()
text_receiving=set()
telemarketers=set()

def telemarketers_list(calls,texts): 
    global calling_numbers,receving_numbers,text_sending,text_receiving,telemarketers  
    m=len(calls)
    n=len(texts)
     
    # making a list of numbers that are calling/reciving 
    for row in range(m): 
        calling_numbers.add(calls[row][0])
        receving_numbers.add(calls[row][1])        
           
           
    # making a list of numbers that are sending/receiving texts
    for row in range(n): 
        text_sending.add(texts[row][0])
        text_receiving.add(texts[row][1])

   #Getting rid of unnecessary numbers

    telemarketers=calling_numbers-receving_numbers-text_sending-text_receiving
    
    telemarketers=sorted(list(telemarketers)) 

    # Printing all the numbers
    
    for i in range(len(telemarketers)):
        print(telemarketers[i])              
                    

    
   
    
    return ""


telemarketers_list(calls,texts)
