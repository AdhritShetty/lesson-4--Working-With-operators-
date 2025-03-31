#Taking the total amount as the input of the user
amount=int(input("please enter amount for withdrawal:"))

#calculating the number of notes of different denominations
note_1=amount//100
note_2=(amount%100)//50
note_3=((amount %100)%50)//10

print("notes of 100 rupee",note_1)
print("notes of 50 rupee",note_2)
print("notes of 10 rupees",note_3)
