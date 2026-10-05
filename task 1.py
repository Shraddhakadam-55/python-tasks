#1) WAP Hello World by your_name

print("Hello World ....  Shraddha Kadam")

#2)create 2 variables cost_price and selling_price and calculate the profit or loss

cost_price = int(input("Enter the number 1"))
selling_price =int(input("Enter the number 2"))

if selling_price > cost_price:
    profit = selling_price - cost_price
    print("profit :" , profit)

elif cost_price > selling_price:
    loss = cost_price - selling_price
    print("loss:",loss)

else:
    print("nothing is complete")

#3) WAP to check the number is even or odd

num1 = int(input("enter first number"))

if num1 %2==0:
    print("number is even " ,num1)
elif num1 %2==1:
    print("number is odd",num1)
else:
    print("either even or odd")


#4)WAP age is valid or elegible for voting or not

age = int(input("enter the age"))

if age >18 or age > 150:
    print("elegible for voting",age)

elif age < 18 or age < 150:
    print("not elegible for voting",age)

else:
    print("not for vating")

#5)WAP to find the word 1 and word 2 is anagram

word1 = input("Enter word 1: ")
word2 = input("Enter word 2: ")

if len(word1) != len(word2):
    print("Not anagram")
else:
    for ch in word1:
        if ch in word2:
            word2 = word2.replace(ch, "", 1)
        else:
            print("Not anagram")
            break
    else:
        print("Anagram")    

