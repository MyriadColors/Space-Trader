"""
    Space Trader (PalmOS) | RPINerd, 06/27/24

    An early strategy RPG game for PalmOS, Space Trader is a game where you are a
    freelance captain, buying and selling goods to make a profit, fending off pirates,
    dealing with sector police, and occasionally ending up on intergalactic quests.

    You can travel to different planets, each with their own economy for trade. You can
    also upgrade your ship, hire crew, and take on missions to make money.

    The game is over when you run out of money, your ship is destroyed or you
    retire with the spoils of your adventures.
"""

import pygame

from src.game import Game


def main():
    """ """

    space_trader = Game()
    while space_trader.running:
        space_trader.run()
    pygame.quit()


if __name__ == "__main__":
    main()
