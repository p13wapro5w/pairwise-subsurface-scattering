import pytest
from render import subsurface_scattering as mod

CASES = [
    ("diffusion_zero", "m.diffusion(0.0, 1.0) == approx(1.0)"),
    ("diffusion_decay", "m.diffusion(1.0, 1.0) < m.diffusion(0.0, 1.0)"),
    ("thickness_facing", "m.thickness_along((1.0, 0.0), (1.0, 0.0)) == approx(1.0)"),
    ("thickness_back", "m.thickness_along((1.0, 0.0), (-1.0, 0.0)) == approx(0.0)"),
    ("scatter_separate", "m.scatter_color((1.0, 0.0, 0.0), (0.2, 0.1, 0.05)) == (0.2, 0.1, 0.05)"),
    ("transmit_none", "m.transmittance(1.0, 1.0) == approx(0.0)"),
    ("transmit_full", "m.transmittance(1.0, 0.0) == approx(1.0)"),
    ("curvature_flat", "m.curvature_weight(0.0) == approx(0.0)"),
    ("curvature_abs", "m.curvature_weight(-0.5) == approx(0.5)"),
    ("dedupe_max", "m.shadow_dedupe(0.6, 0.2) == approx(0.6)"),
    ("write_depth_true", "m.write_depth(True, True) is True"),
    ("write_depth_false", "m.write_depth(True, False) is False"),
    ("lut_pair", "m.lut_param(0.5, 2.0) == (0.5, 2.0)"),
    ("world_radius_half", "m.world_radius(10.0, 2.0) == approx(5.0)"),
    ("world_radius_zero", "m.world_radius(0.0, 2.0) == approx(0.0)")
]

@pytest.mark.parametrize("name,expr", CASES, ids=[c[0] for c in CASES])
def test_contract(name, expr):
    assert eval(expr, {"m": mod, "approx": pytest.approx})
