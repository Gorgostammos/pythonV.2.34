#oppgave1.1


import blackjack as bmj

print(bmj.full_deck)
def print_header():
    print("====BlackJack====")
    print()


def should_user_try_again():
    answer = input("\nDo you want to try again(Y/N)?  ")
    return answer.upper() == 'Y'

       #oppgave1.1b

should_still_run = True
print()
while should_still_run:
    print_header()

    player = bmj.get_new_shuffled_deck()
    player_card1 = bmj.get_card_value(card=player[0])
    player_card2 = bmj.get_card_value(card=player[1])
    player_card_v = player_card1 + player_card2

    new_player_card = bmj.get_new_shuffled_deck()
    player_new_card1 = bmj.get_card_value(card=new_player_card[0])
    player_new_card2 = bmj.get_card_value(card=new_player_card[1])
    new_player_card_v = player_new_card1 + player_new_card2


    dealer = bmj.get_new_shuffled_deck()
    dealer_card1 = bmj.get_card_value(card=dealer[0])
    dealer_card2 = bmj.get_card_value(card=dealer[1])
    dealer_card_v = dealer_card1 + dealer_card2







    print(f"The player card is: {player[0]} - {player_card1} and {player[1]} - {player_card2} "
          f"and the value og the card is {player_card_v}")


    print()
    if player_card_v == 21:
        print('BlackJack')
    elif player_card_v < 21:
        print('1 = Hit')
        print('2 = stand')
    command = input("Pick a command: ")

    if command == '1':
        print('you chose Hit')
        print()
        print(f"The new card the player got is : {new_player_card[0]} - {player_new_card1} and {new_player_card[1]} - "
              f"{player_new_card2} and the value og the card is {new_player_card_v}")
        print()
        print(f"The dealer hand is: {dealer[0]} {dealer_card1} and {dealer[1]} {dealer_card2} "
              f"and the dealer cards have a value of {dealer_card_v}")
    if new_player_card_v > 21:

        print('bustet')

    if command == '2':
        print("you piced Stand")
        print()
        print(f"The player card is: {player[0]} - {player_card1} and {player[1]} - {player_card2} "          
              f"and the value og the card is {player_card_v}")
        print()

        print(f"The dealer hand is: {dealer[0]} {dealer_card1} and {dealer[1]} {dealer_card2} "              
              f"and the dealer cards have a value of {dealer_card_v}")
    if dealer_card_v > 21:
         print()
         print("bustet, The player have won")
         print()
    if player_card_v > dealer_card_v:
        print()
        print("The palyer have more card value then the dealeren, The player have won")
        print()
    if dealer_card_v > player_card_v:
        print()
        print("The dealeren have more card value then the palyer,the player have lost and the Hus have won")
        print()
    if player_card_v == dealer_card_v:
        print()
        print("It´s a draw no one wins")
        print()


    should_still_run = should_user_try_again()






#oppgave1.2D
#jeg skjønnet ikke hvordan man kunne løste dette oppgaven

#oppgave1.3








