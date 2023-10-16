"""test_general_pos_generator.py"""


from crystal_visualizer.general_pos_generator import GeneralPositionGenerator






def test_can_convert_single_digit_to_float():
    gps = GeneralPositionGenerator
    assert convert_str_to_float("3") == 3.0
