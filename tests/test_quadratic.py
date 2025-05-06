from quadratic_solver.quadratic import QuadraticEquation

def test_two_solutions():
    eq = QuadraticEquation(1, -3, 2)  # x^2 - 3x + 2 = 0 → x=1, x=2
    solutions = eq.solve()
    assert set(solutions) == {1.0, 2.0}

def test_one_solution():
    eq = QuadraticEquation(1, 2, 1)  # x^2 + 2x + 1 = 0 → x=-1
    solutions = eq.solve()
    assert solutions == (-1.0,)

def test_no_solution():
    eq = QuadraticEquation(1, 0, 1)  # x^2 + 1 = 0 → pas de solution réelle
    assert eq.solve() is None
