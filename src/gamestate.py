import pygame


# Define the possible game states using an Enum
class GameStateID:
    SPLASH = 0
    CMD_MAKE = 1
    PAUSE = 2
    GAME_OVER = 3


# The GameStateManager class manages the game states and handles events, updates, and rendering
class GameStateManager:
    def __init__(self):
        self.screen_width = 1024
        self.screen_height = 1024
        self.native_res = 160
        self.canvas = pygame.Surface((160, 160))
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Space Trader")
        pygame.display.set_icon(pygame.image.load("images/App.ico"))

        self.background_image = pygame.image.load("images/splash.jpg")

        self.current_state = GameStateID.SPLASH

    def start(self):
        while True:
            self.handle_events()
            self.update()
            self.render()

    # Handle any input events
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit_game()
            elif event.type == pygame.KEYDOWN:
                if self.current_state == GameStateID.SPLASH:
                    self.handle_splash_input(event.key)
                elif self.current_state == GameStateID.CMD_MAKE:
                    self.handle_gameplay_input(event.key)
                elif self.current_state == GameStateID.PAUSE:
                    self.handle_pause_input(event.key)
                elif self.current_state == GameStateID.GAME_OVER:
                    self.handle_game_over_input(event.key)

    # Handle input events in the MENU state
    def handle_splash_input(self, key):
        if key == pygame.K_RETURN:  # start gameplay
            self.current_state = GameStateID.CMD_MAKE
        elif key == pygame.K_ESCAPE:  # quit game
            self.quit_game()

    # Handle input events in the CMD_MAKE state
    def handle_gameplay_input(self, key):
        if key == pygame.K_p:  # pause
            self.current_state = GameStateID.PAUSE

    # Handle input events in the PAUSE state
    def handle_pause_input(self, key):
        if key == pygame.K_p:  # resume gameplay
            self.current_state = GameStateID.CMD_MAKE
        elif key == pygame.K_q:  # quit game
            self.quit_game()

    # Handle input events in the GAME_OVER state
    def handle_game_over_input(self, key):
        if key == pygame.K_r:  # restart game
            self.current_state = GameStateID.SPLASH

    # Update the game state
    def update(self):
        if self.current_state == GameStateID.CMD_MAKE:
            # game logic and update here
            pass

    # Render the current state
    def render(self):
        self.screen.fill((0, 0, 0))  # clear screen

        if self.current_state == GameStateID.SPLASH:
            self.render_splash()
        elif self.current_state == GameStateID.CMD_MAKE:
            self.render_gameplay()
        elif self.current_state == GameStateID.PAUSE:
            self.render_pause()
        elif self.current_state == GameStateID.GAME_OVER:
            self.render_game_over()

        pygame.display.flip()  # update screen

    # Render the menu screen
    def render_splash(self):
        self.canvas.blit(self.background_image, (0, 0))
        transform = pygame.transform.scale(self.canvas, (self.screen_width, self.screen_height))
        self.screen.blit(transform, (0, 0))
        pygame.display.flip()
        self.clock.tick(30)

    # Render the gameplay screen
    def render_gameplay(self):
        # render gameplay here
        self.canvas.fill((240, 240, 240))
        pygame.draw.rect(
            self.canvas,
            (0, 0, 0),
            pygame.Rect(1, 1, self.native_res - 2, self.native_res - 2),
            2,
            border_radius=3,
        )
        transform = pygame.transform.scale(self.canvas, (self.screen_width, self.screen_height))
        self.screen.blit(transform, (0, 0))
        pygame.display.flip()
        self.clock.tick(30)
        pass

    # Render the pause screen
    def render_pause(self):
        # render pause here
        pass

    # Render the game over screen
    def render_game_over(self):
        # render game over here
        pass

    # Quit the game
    def quit_game(self):
        pygame.quit()
        quit()


# Entry point of the program
if __name__ == "__main__":
    game_state_manager = GameStateManager()
    game_state_manager.start()
