import random

if __name__ == "__main__":
    over = input("Would you like to play a game? Yes or No? ")
    while over != "No":
        game_of_choice = input("Pick a game from the list: Blackjack, War, or Trivia ")
        if game_of_choice == "Trivia":
            print("Welcome to Trivia!")
            userinput = input("Are you ready to play? (yes/no): ")
            score = 0
            total_questions = 10

            if userinput.lower() == "no":
                print("No Game")

            if userinput.lower() == "yes":
                userinput = input("Question 1: What does WWW stand for in a website browser? ")
                if userinput == "world wide web":
                    score += 1
                    print("correct")
                else:
                    print("Incorrect")

                userinput = input("Question 2: What is cynophobia? ")
                if userinput == "fear of dogs":
                    score += 1
                    print("correct")
                else:
                    print("Incorrect")

                userinput = input("Question 3: How many languages are written from right to left? ")
                if userinput == "12":
                    score += 1
                    print("correct")
                else:
                    print("Incorrect")

                userinput = input("Question 4: What was the first toy to be advertised on TV? ")
                if userinput == "Mr.Potato head":
                    score += 1
                    print("correct")
                else:
                    print("Incorrect")

                userinput = input(
                    "Question 5: What was the first feature-length animated movie ever released? (HINT: It was a Disney movie) ")
                if userinput == "Snow White and the Seven Dwarfs":
                    score += 1
                    print("correct")
                else:
                    print("Incorrect")

                userinput = input("Question 6: In little red riding hood, who does the wolf dress up as ? ")
                if userinput == "Grandmother":
                    score += 1
                    print("correct")
                else:
                    print("Incorrect")

                userinput = input("Question 7: What color is a ruby? ")
                if userinput == "Red":
                    score += 1
                    print("correct")
                else:
                    print("Incorrect")

                userinput = input("Question 8: How many colors are in a rainbow? ")
                if userinput == "7":
                    score += 1
                    print("correct")
                else:
                    print("Incorrect")

                userinput = input("Question 9: What country is responsible for creating the Olympic games? ")
                if userinput == "Greece":
                    score += 1
                    print("correct")
                else:
                    print("Incorrect")

                userinput = input("Question 10: How long is New Zealand's ninety mile beach? ")
                if userinput == "55 miles":
                    score += 1
                    print("correct")
                else:
                    print("Incorrect")

            print("Thanks for playing!", "Your score is", score)
            total = (score / total_questions) * 100
            print("total: ", total)
            over = input("Would you like to play a game? Yes or No? ")
            if over == "Yes":
                game_of_choice = input("Pick a game from the list: Blackjack, War, or Trivia ")
            else:
                exit()
            '''
            Sources:
            Help with code base:
            https://www.askpython.com/python/examples/easy-games-in-python
        
            Questions for trivia:
            https://www.quizbreaker.com/trivia-questions
            '''

        if game_of_choice == "War":
            class Card:
                def __init__(self, value, suit):
                    self.value = value
                    self.suit = suit

                def __repr__(self):
                    return f'{self.value} of {self.suit}'


            class Deck:
                def __init__(self):
                    self.cards = []
                    self.suits = ['Diamonds', 'Spades', 'Clubs', 'Hearts']
                    self.values = range(2, 15)

                def create_deck(self):
                    for suit in self.suits:
                        for value in self.values:
                            new_card = Card(value, suit)
                            self.cards.append(new_card)
                            random.shuffle(self.cards)


            player_one = []
            player_two = []


            def start_game():
                new_deck = Deck()
                new_deck.create_deck()
                length = len(new_deck.cards)
                middle = length // 2
                first = new_deck.cards[:middle]
                second = new_deck.cards[middle:]
                player_one.extend(first)
                player_two.extend(second)
                print(player_one)


            def main():
                num1 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
                num2 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
                random.shuffle(num1)
                random.shuffle(num2)
                numb1 = num1[0:1]
                numb2 = num2[0:1]
                # numbers^
                su = ['Diamonds', 'Spades', 'Clubs', 'Hearts']
                sU = ['Diamonds', 'Spades', 'Clubs', 'Hearts']
                random.shuffle(sU)
                random.shuffle(su)
                su1 = su[0:1]
                su2 = sU[0:1]
                # suits^
                w = Card(numb1, su1)
                z = Card(numb2, su2)
                p1 = [w]
                p2 = [z]
                if w.value > z.value:
                    p1.append(z)
                    print("Player 1 takes Player 2's card")
                    print(f'player 1 deck: {p1}')
                    a = input('Want to play again(y/n): ')
                    if a == 'y':
                        main()
                    else:
                        print('The game has ended')
                elif z.value > w.value:
                    p2.append(w)
                    print("Player 2 takes Player 1's card")
                    print(f' Player 2 deck: {p2}')
                    b = input('Want to play again(y/n): ')
                    if b == 'y':
                        main()
                    else:
                        print('The game has ended')
                else:
                    war()
                # this is what MAINLY runs the game
                # compare player's cards after they draw
                # if the cards have the same value=war
                # if player_one>player_two player one gets the card(and vice versa)


            def war():
                nums = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
                sui = ['Diamonds', 'Spades', 'Clubs', 'Hearts']
                random.shuffle(nums)
                random.shuffle(sui)
                s1 = sui[0:1]
                s2 = sui[1:2]
                s3 = sui[2:3]
                tc_2 = nums[0:1]
                tc_3 = nums[1:2]
                qc_2 = nums[2:3]
                qc_3 = nums[3:4]
                # randomizing the values of the 2nd and 3rd card on each hand + randomizing the suits of all cards
                t1 = Card(10, s1)
                t2 = Card(tc_2, s2)
                t3 = Card(tc_3, s3)
                # player 1's cards
                q1 = Card(10, s2)
                q2 = Card(qc_2, s3)
                q3 = Card(qc_3, s1)
                # player 2's cards
                p1 = [t1, t2, t3]
                p2 = [q1, q2, q3]
                # Both Player's Hand
                print(t1)
                print(q1)
                if t1.value == q1.value:
                    print('War has begun!')
                    if t3.value > q3.value:
                        p1.append(p2)
                        print('Player 1 has won the War')
                        print(p1)
                    else:
                        p2.append(p1)
                        print('Player 2 has won the War')
                        print(p2)


            main()
            over = input("Would you like to play a game? Yes or No? ")
            if over == "Yes":
                game_of_choice = input("Pick a game from the list: Blackjack, War, or Trivia ")
            else:
                exit()

        if game_of_choice == "Blackjack":
            blackjack = {'Ace of Hearts': 11, 'Two of Hearts': 2, 'Three of Hearts': 3, 'Four of Hearts': 4,
                         'Five of Hearts': 5,
                         'Six of Hearts': 6, 'Seven of Hearts': 7, 'Eight of Hearts': 8, 'Nine of Hearts': 9,
                         'Ten of Hearts': 10,
                         'Jack of Hearts': 10, 'Queen of Hearts': 10, 'King of Hearts': 10, 'Ace of Spades': 11,
                         'Two of Spades': 2,
                         'Three of Spades': 3, 'Four of Spades': 4, 'Five of Spades': 5, 'Six of Spades': 6,
                         'Seven of Spades': 7,
                         'Eight of Spades': 8, 'Nine of Spades': 9, 'Ten of Spades': 10, 'Jack of Spades': 10,
                         'Queen of Spades': 10,
                         'King of Spades': 10, 'Ace of Diamonds': 11, 'Two of Diamonds': 2, 'Three of Diamonds': 3,
                         'Four of Diamonds': 4,
                         'Five of Diamonds': 5, 'Six of Diamonds': 6, 'Seven of Diamonds': 7, 'Eight of Diamonds': 8,
                         'Nine of Diamonds': 9,
                         'Ten of Diamonds': 10, 'Jack of Diamonds': 10, 'Queen of Diamonds': 10, 'King of Diamonds': 10,
                         'Ace of Clubs': 11,
                         'Two of Clubs': 2, 'Three of Clubs': 3, 'Four of Clubs': 4, 'Five of Clubs': 5,
                         'Six of Clubs': 6, 'Seven of Clubs': 7,
                         'Eight of Clubs': 8, 'Nine of Clubs': 9, 'Ten of Clubs': 10, 'Jack of Clubs': 10,
                         'Queen of Clubs': 10, 'King of Clubs': 10}

            keysa = random.sample(list(blackjack), 2)
            valuea = [blackjack[k] for k in keysa]
            keysb = random.sample(list(blackjack), 2)
            valueb = [blackjack[k] for k in keysb]
            keysd = random.sample(list(blackjack), 2)
            valued = [blackjack[k] for k in keysd]
            clist = ['yes', 'no']
            dlist = []
            elist = dict()
            print("Let's play Blackjack! Try to get the highest number without going over 21.")
            print("Jacks, Queens, and Kings count as 10 points. Aces count as 11.")
            print("Alright, lets begin.")
            print("")
            print("Your cards are", keysa[0], "&", keysa[1], "giving you a total of", sum(valuea))
            print("Player B draws", keysb[0], "&", keysb[1], "giving them a total of", sum(valueb))
            print("Dealer's face up card is", keysd[0])

            # Players hand
            while True:
                q3 = input("Would you like to stay or draw? ")
                if q3 == "stay":
                    print("Your total is", sum(valuea))
                    print("")
                    break

                elif q3 == "draw":
                    keysa1 = random.sample(list(blackjack), 1)
                    valuea1 = [blackjack[k] for k in keysa1]
                    valuea.insert(2, valuea1[0])
                    print("You draw", keysa1[0], "giving you a total of", sum(valuea))
                    print("")

                if (sum(valuea) > 21):
                    print("Oops, you bust.")
                    break

            # PlayerB hand
            while sum(valueb) < 16:
                keysb1 = random.sample(list(blackjack), 1)
                valueb1 = [blackjack[k] for k in keysb1]
                valueb.insert(2, valueb1[0])
                print("Player B decides to draw", keysb1[0], "giving them a total of", sum(valueb))
                if 21 >= sum(valueb) > 14:
                    print("Player B decides to stay, leaving them with", sum(valueb))
                    print("")
                    break
                if 21 < sum(valueb):
                    print("Player B busts.")
                    print("")
                    break
            if sum(valueb) >= 16:
                print("Player B decides to stay, leaving them with", sum(valueb))

            # Dealer hand
            print("Now lets see the dealers hidden card!")
            print("Dealer has", keysd[0], "&", keysd[1], "giving them a total of", sum(valued))
            if sum(valued) <= 16:
                keysd1 = random.sample(list(blackjack), 1)
                valued1 = [blackjack[k] for k in keysd1]
                valued.insert(2, valued1[0])
                print("Dealer draws", keysd1[0], "giving them a total of", sum(valued))
            elif 21 > sum(valued) >= 17:
                print("Dealer stays. They have a total of", sum(valued))
            elif 21 < sum(valued):
                print("The dealer busts, you and Player B win!")
                exit()

            if sum(valued) < sum(valueb) < sum(valuea):
                print("Everyone owes you!")
            elif sum(valueb) < sum(valued) < sum(valuea):
                print("Player B owes the dealer and the dealer owes you.")
            elif sum(valued) < sum(valuea) < sum(valueb):
                print("Everyone owes Player B!")
            elif sum(valuea) < sum(valued) and sum(valueb) < sum(valued):
                print("Everyone owes the dealer!")
            elif sum(valuea) < sum(valued) < sum(valueb):
                print("You owe the dealer and the dealer owes Player B.")
            over = input("Would you like to play a game? Yes or No? ")
            if over == "Yes":
                game_of_choice = input("Pick a game from the list: Blackjack, War, or Trivia ")
            else:
                exit()