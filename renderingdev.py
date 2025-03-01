import tkinter as tk

from src.constants import BKG_HEX, FRG_HEX, INTERNAL_RES, SCALAR
from src.universe import Universe


def main():

    scaled_res = INTERNAL_RES * SCALAR

    root = tk.Tk()
    root.title("Universe Testing Render")
    root.geometry(f"{scaled_res}x{scaled_res}")
    root.configure(background=BKG_HEX)
    root.resizable(False, False)

    # Make a 15 pixel box anchored to the top of the screen to rep the title bar
    title_bar = tk.Frame(root, height=15 * SCALAR)
    title_bar.configure(background=FRG_HEX)
    title_bar.pack(fill="x", side="top")

    # Make a 26 pixel box anchored to the bottom of the screen to rep the status bar
    status_bar = tk.Frame(root, height=26 * SCALAR)
    status_bar.configure(background=FRG_HEX)
    status_bar.pack(fill="x", side="bottom")

    # Create a canvas to draw the universe on
    universe_canvas = tk.Canvas(root, bg=BKG_HEX, width=154 * SCALAR, height=110 * SCALAR)
    universe_canvas.pack(fill="both", expand=True)

    # Generate a new universe
    test_universe = Universe()

    # Draw a 3x3 pixel square centered on each xy coordinate in the universes' planet dict
    for planet in test_universe.planets.values():
        x = planet.x * SCALAR
        y = planet.y * SCALAR
        universe_canvas.create_rectangle(x - 1, y - 1, x + 1, y + 1, fill=FRG_HEX, outline=FRG_HEX)

    root.mainloop()


if __name__ == "__main__":
    main()
