import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.universe import Universe

if __name__ == "__main__":
    testverse = Universe()

    for i in testverse.planets:
        print(f"{i}: {testverse.planets[i]}")
