import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from constants import Activity
from universe import Universe

if __name__ == "__main__":
    print(Activity.ABSENT)
    testverse = Universe()

    print(testverse.planets)
