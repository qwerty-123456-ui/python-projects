import random
import os
a=True
user_score=0
while a==True:
    def calc_hand(hand):
        sum=0
        non_aces=[card for card in hand if card!='A' ]
        aces=[card for card in hand if card=='A' ]
        for card in non_aces:
            if card in 'JKQ':
                sum+=10
            else:
                sum+=int(card)

        for card in aces:
            if sum<=10:
                sum+=11
            else:
                sum+=1

        return sum


    cards=[
       '2','3','4','5','6','7','8','9','10','J','K','Q','A',
       '2','3','4','5','6','7','8','9','10','J','K','Q','A',
       '2','3','4','5','6','7','8','9','10','J','K','Q','A',
       '2','3','4','5','6','7','8','9','10','J','K','Q','A'
    ]
    random.shuffle(cards)
    dealer=[]
    player=[]
    player.append(cards.pop())
    dealer.append(cards.pop())
    player.append(cards.pop())
    dealer.append(cards.pop())
    standing=False
    firsthand=True
    # print(dealer,player)

    while True:
        os.system('cls' if os.name=='nt' else 'clear')

        player_score=calc_hand(player)
        dealer_score=calc_hand(dealer)
        if standing:
            print('Dealer cards [{}] ({})'.format(']['.join(dealer),dealer_score))
        else:
            print(f'Dealer cards :[{dealer[0]}][?]')
        print('ur cards [{}] ({})'.format(']['.join(player),player_score))
        if standing:
            if dealer_score>21:
                print('Dealer busted .. U win!!')
                user_score+=100
                print("user score:" ,user_score)
            elif player_score==dealer_score:
                print('Push, nobody wins or loses')
                user_score+=0
                print("user score:" ,user_score)
            elif player_score>dealer_score:
                print('U beat the dealer, u win!')
                user_score+=100
                print("user score:" ,user_score)

            else:
                print('u lose:(')
                user_score-=100
                print("user score:" ,user_score)
            break
        if player_score>21:
            print(' u r busted!!')
            user_score-=100
            print("user score:" ,user_score)
            break
        firsthand=False
        if firsthand and player_score==21:
            print('BlackJack ! U win ')
            user_score+=100
            print("user score:" ,user_score)
            break
        print('what would u like to do?')
        print('[1] Hit')
        print('[2] Stand')
        print('')
        print('Your choice')
        choice=input('Your choice: ')
        print('')

        if choice=='1':
            player.append(cards.pop())
        elif choice=='2':
            standing=True
            while calc_hand(dealer)<=16:
                dealer.append(cards.pop())
    print("to continue:press y")
    c=input()
    if c=='y':
         a=True
    else:
         a=False
