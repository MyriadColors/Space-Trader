""""""

import src.constants as c
from src.universe import GOVERNMENTS, PLANET_NAMES, Planet, Universe

testverse = Universe()


def test_planetcounts():
    assert len(testverse.planets) == len(PLANET_NAMES)
    assert len(testverse.wormholes) == 10


def test_wormholes():
    assert all(isinstance(x, int) for x in testverse.wormholes)
    assert all(x in testverse.planets for x in testverse.wormholes)


def test_planetproperties():
    assert all(isinstance(x, Planet) for x in testverse.planets.values())

    for i in testverse.planets:
        assert testverse.planets[i].name in PLANET_NAMES.values()
        assert testverse.planets[i].size in range(6)
        assert testverse.planets[i].get_govt_type() in GOVERNMENTS.values()
        assert testverse.planets[i].tech_level in range(
            testverse.planets[i].government.minTech, testverse.planets[i].government.maxTech + 1
        )
        assert testverse.planets[i].soci_pressure in range(8)
        assert testverse.planets[i].special_resource in range(13)
        assert testverse.planets[i].x in range(c.GALAXYWIDTH + 1)
        assert testverse.planets[i].y in range(c.GALAXYHEIGHT + 1)


def test_planetpositions():
    for i in testverse.planets:
        for j in testverse.planets:
            if i != j:
                assert testverse.planets[i].get_distance(testverse.planets[j]) >= c.MIN_DISTANCE


def test_universe():
    pass
