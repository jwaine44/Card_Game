from classes import deck
from classes.deck import Deck

class Game:
    def __init__(self):
        self.player1 = Player()
        self.player2 = Player()
        self.pile = []

    def run_game(self):
        while len(self.player1.deck.cards) > 0:
            self.pile_add()
            self.compare()
        if len(self.player1.hoard) > len(self.player2.hoard):
            print("YOU WIN")
        elif len(self.player1.hoard) < len(self.player2.hoard):
            print("GET REKT")
        else:
            print("IT'S A TIE")

# This is where we display cards against each other
    def pile_add(self):
        self.pile.append(self.player1.get_hand())
        self.pile.append(self.player2.get_hand())

# Compares 2 card values to determine weight, rewards accordingly
    def compare(self):
        input("Press enter to start next round")
        self.pile[len(self.pile) - 2].card_info()
        self.pile[len(self.pile) - 1].card_info()
        if self.pile[len(self.pile) - 2].point_val > self.pile[len(self.pile) - 1].point_val:
            for card in self.pile:
                self.player1.hoard.append(card)
            print("Player 1 wins this round!")
            self.pile.clear()
        elif self.pile[len(self.pile) - 2].point_val < self.pile[len(self.pile) - 1].point_val:
            for card in self.pile:
                self.player2.hoard.append(card)
            print("Player 2 wins this round!")
            self.pile.clear()
        else:
            if len(self.player1.deck.cards) >= 1:
                self.pile_add()
                print("Draw again")
                self.compare()
            else:
                self.pile.clear()
                print("No more cards left. Cards are discarded.")

def menu():
    playVal = get_play_val()
    if playVal == "2":
        return
    elif playVal == "1":
        game = Game()
        game.run_game()
        menu()
    else:
        restart_menu()

def restart_menu():
    print(f"Invalid input, try again!")
    menu()

def get_play_val():
    return input(f"WAR. LETS PLAY?\n 1) YEA!\n 2) nah.\n")

class Player:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.hoard = []

    def get_hand(self):
        return self.deck.cards.pop(0)


menu()