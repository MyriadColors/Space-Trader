"""
    UI Previewer | RPINerd, 2024
    
    This script is a simple UI previewer for the Space Trader game. It allows you to request a state and see what the current UI would look like.
    
    Usage:
        python ui_preview.py <state>
        
"""

import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import pygame

if __name__ == "__main__":
    pygame.init()
    pygame.font.init()
    pygame.display.set_caption("UI Previewer | RPINerd, 2024")
    screen = pygame.display.set_mode((320, 320))

    from src.constants import INTERNAL_RES
    from src.interface.char_create import CharacterCreation
    from src.interface.renderer import Header, TextRender, TitleBar
    from src.interface.state import State
    from src.interface.system_info import SystemInfo

    game = State(None)
    game.font_sm_bold = pygame.font.Font("assets/fonts/PressStart2P-Regular.ttf", 12)
    game.font_sm = pygame.font.Font("assets/fonts/PressStart2P-Regular.ttf", 8)

    if len(sys.argv) < 2:
        print("Usage: python ui_preview.py <state>")
        sys.exit(1)

    state = sys.argv[1]

    if state == "info":
        state = SystemInfo(game)
    elif state == "char":
        state = CharacterCreation(game)
    else:
        print("Invalid state")
        sys.exit(1)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            state.handle_events(event)

        screen.fill((240, 240, 240))
        state.render(screen)
        pygame.display.flip()
