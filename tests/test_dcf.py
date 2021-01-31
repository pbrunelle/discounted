import dcf
import numpy as np

def test_create_series_0_steps():
    assert dcf.create_series(1.5, 0.03, 0).tolist() == []

def test_create_series_1_steps():
    assert dcf.create_series(1.5, 0.03, 1).tolist() == [1.5]

def test_create_series_3_steps_positive_rate():
    assert dcf.create_series(2.0, 0.5, 3).tolist() == [2.0, 3.0, 4.5]

def test_create_series_3_steps_negative_rate():
    assert dcf.create_series(2.0, -0.1, 3).tolist() == [2.0, 1.8, 1.62]

def test_pv_series_0():
    assert dcf.pv([], 0.5) == 0.0

def test_pv_series_1():
    assert dcf.pv([10.0], 0.5) == 5.0

def test_pv_series_2():
    assert dcf.pv([10.0, 4.0], 0.5) == 6.0

def test_dcf_2_x_3():
    df = dcf.dcf(8.08, growth_rates=[-0.01, -0.02], discount_rates=[0.00, 0.01, 0.02])
    expected = np.array([[799.9, 395.9], [398.0, 263.1], [263.1, 196.0]])
    assert np.allclose(df.values, expected, atol=0.1)
