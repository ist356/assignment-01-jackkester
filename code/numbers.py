'''
Write a python program to input integer values until a 0 is entered.
For each input integer if its odd, store in a dictionary under the key 'odd' 
and if its even, store in a dictionary under the key 'even'.

After a zero is entered, print the dictionary.

For example, if the input is:
2 3 5 4 6 0 

The output should be:
{'odd': [3, 5], 'even': [2, 4, 6]}
'''
odd_list = []
even_list = []
while True:
    
    num = int(input("Input a number: "))
    if num == 0:
        dictionary = {'odd': odd_list, 'even': even_list}
        print(dictionary)
        break
        
    
    if num % 2 == 0:
        #count_even += 1
        even_list.append(num)
    elif num % 2 == 1:
        #count_odd += 1
        odd_list.append(num)


    



    