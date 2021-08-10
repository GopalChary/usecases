

#Write a code to find out total number of Upper-case alphabets in a String.

def find_upper(s):
    count_upper=0
    for u in s:
        if u.isupper():
            count_upper+=1
    return count_upper

def main():
    s=input("Enter a string : ")
    print("Total upper case alphabets from the given string is : ",find_upper(s))
main()
