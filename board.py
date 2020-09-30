import pygame

from card import Card
from deck import Deck
from player import Player


class Board:
    def __init__(self, player1, player2, deck, card, screen):
        self.player1 = Player(player1)
        self.player2 = Player(player2)
        self.deck = Deck(screen)

        self.screen = screen

    def draw(self):
        pygame.draw.rect(self.screen, [50, 50, 50], (100, 100, 100, 100))
        self.deck.draw()

    def run(self):
        pass
