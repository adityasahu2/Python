import random
from enum import Enum

# Enum for Suit class
class Suit(Enum):
    HEARTS = "Hearts"
    DIAMONDS = "Diamonds"
    CLUBS = "Clubs"
    SPADES = "Spades"

# Card class
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    
    def __repr__(self):
        return f"{self.rank} of {self.suit.value}"

# Deck class
class Deck:
    def __init__(self):
        self.cards = [Card(suit, rank) for suit in Suit for rank in 
                      ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]]
        self.shuffle()
    
    def shuffle(self):
        random.shuffle(self.cards)
    
    def draw_card(self):
        return self.cards.pop() if self.cards else None

# Hand class
class Hand:
    def __init__(self):
        self.cards = []
    
    def add_card(self, card):
        self.cards.append(card)
    
    def get_value(self):
        value, ace_count = 0, 0
        for card in self.cards:
            if card.rank in ["Jack", "Queen", "King"]:
                value += 10
            elif card.rank == "Ace":
                ace_count += 1
                value += 11
            else:
                value += int(card.rank)
        while value > 21 and ace_count:
            value -= 10
            ace_count -= 1
        return value
    
    def __repr__(self):
        return f"{self.cards} (Total: {self.get_value()})"

# Player class
class Player:
    def __init__(self, name):
        self.name = name
        self.hand = Hand()
    
    def hit(self, deck):
        self.hand.add_card(deck.draw_card())
    
    def is_busted(self):
        return self.hand.get_value() > 21
    
    def __repr__(self):
        return f"{self.name}: {self.hand}"

# Dealer class (inherits from Player)
class Dealer(Player):
    def play(self, deck):
        while self.hand.get_value() < 17:
            self.hit(deck)

# Blackjack game class
class BlackjackGame:
    def __init__(self, player_names):
        self.deck = Deck()
        self.players = [Player(name) for name in player_names]
        self.dealer = Dealer("Dealer")
    
    def deal_initial_cards(self):
        for _ in range(2):
            for player in self.players:
                player.hit(self.deck)
            self.dealer.hit(self.deck)
    
    def play(self):
        print("\n--- Starting Blackjack Game ---")
        self.deal_initial_cards()
        for player in self.players:
            while not player.is_busted():
                print(player)
                move = input(f"{player.name}, do you want to hit or stand? (h/s): ").lower()
                if move == 'h':
                    player.hit(self.deck)
                else:
                    break
        self.dealer.play(self.deck)
        self.show_results()
    
    def show_results(self):
        print("\n--- Game Results ---")
        for player in self.players:
            if player.is_busted():
                print(f"{player.name} busted!")
            elif self.dealer.is_busted() or player.hand.get_value() > self.dealer.hand.get_value():
                print(f"{player.name} wins!")
            elif player.hand.get_value() < self.dealer.hand.get_value():
                print(f"{player.name} loses.")
            else:
                print(f"{player.name} ties with the dealer.")
        print(f"Dealer: {self.dealer.hand}")

# Running the game
if __name__ == "__main__":
    player_names = input("Enter player names (comma-separated): ").split(', ')
    game = BlackjackGame(player_names)
    game.play()
