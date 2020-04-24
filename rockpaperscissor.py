import random
a=True
while a:
    choice=input("Enter ur choice :").lower()
    choices=["rock",'paper','scissors']
    # computer_choice=choices[random.randint(0,len(choices)-1)]
    computer_choice=random.choice(choices)
    print("computer choice is ",computer_choice)
    if choice==computer_choice:
        print("it is a tie")
    elif choice=='rock':
        if computer_choice=='paper':
            print('u lose ')
        else:
            print('u win')
    elif choice=='paper':
        if computer_choice=='scissors':
            print('u lose ')
        else:
            print('u win')
    elif choice=='scissors':
        if computer_choice=='rock':
            print('u lose ')
        else:
            print('u win')
    elif choice=='exit':
        a=False
    else:
        print('Invalid choice')
    print()