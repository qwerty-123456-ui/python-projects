import random
a=True
while a:
    choice=input("Enter ur choice :").lower()
    choices=["rock",'paper','scissors']
    # computer_choice=choices[random.randint(0,len(choices)-1)]
    computer_choice=random.choice(choices)
    print("computer choice is ",computer_choice)
    choice_dict={'rock':0,'paper':1,'scissors':2}
    choice_index=choice_dict.get(choice,3)
    computer_index=choice_dict.get(computer_choice)
    result_matrix=[[0,2,1],[1,0,2],[2,1,0],[3,3,3]]
    result_idx=result_matrix[choice_index][computer_index]
    # print(result_idx)
    result_messages=['it is a tie','u win','u lose','invalid choice']
    result=result_messages[result_idx]
    print(result)
    print()