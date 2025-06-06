from pantopia.real_cost import Externalities, real_cost

def test_real_cost_basic():
    ext = Externalities(carbon=1.0, labor=0.5, resources=0.25, waste=0.25)
    assert real_cost(10.0, ext) == 12.0
