


#Write a code to find out total number of Odd Values in an Integer Collection
#using python and lambda function.
#Without lambda
'''
def find_odd(L):
    count_odd=0
    for n in L:
        if n%2==1:
            count_odd+=1
    return count_odd



def main():
    L=[]
    for i in range(5):
        n=int(input("Enter an integer : "))
        L.append(n)
    print("Total odd values from the List is : ",find_odd(L))
main()
'''

#With lambda

def find_odd(L):
    odd=list(filter(lambda n:n%2==1,L))
    return len(odd)

def main():
    L=[]
    for i in range(5):
        n=int(input("Enter an integer : "))
        L.append(n)
    print("Total odd values from the List is : ",find_odd(L))
main()


    





