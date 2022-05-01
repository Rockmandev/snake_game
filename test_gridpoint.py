import pytest
from grid import Grid_Point

def test_gridpoint():
    gp = Grid_Point(20, 20, 10)
    assert gp.grid_pos == (20, 20)

def test_gridpoint_window_pos():
    gp = Grid_Point(20, 20, 10)
    assert gp.window_pos == (200, 200)

def test_gridpoint_from_window():
    gp = Grid_Point.from_window(200, 200, 10)
    assert gp.grid_pos == (20, 20)

def test_gridpoint_add():
    gp1 = Grid_Point(20, 20, 10)
    gp2 = Grid_Point(1, 1, 10)
    assert (gp1+gp2).grid_pos == (21, 21)

def test_gridpoint_compare():
    gp1 = Grid_Point(20, 20, 10)
    gp2 = Grid_Point(20, 20, 10)
    assert gp1 == gp2

def test_gridpoint_compare_False():
    gp1 = Grid_Point(20, 20, 10)
    gp2 = Grid_Point(20, 30, 10)
    assert not gp1 == gp2

def test_gridpoint_multiply():
    gp = Grid_Point(20, 20, 10)
    assert (gp * -1) == Grid_Point(-20, -20, 10)

def test_gridpoint_multiply_gridpoints():
    gp1 = Grid_Point(20, 20, 10)
    gp2 = Grid_Point(20, 30, 10)
    with pytest.raises(NotImplementedError):
        gp3 = gp1 * gp2