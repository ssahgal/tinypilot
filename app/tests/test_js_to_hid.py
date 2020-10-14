import unittest

from hid.keycodes import azerty
from hid.keycodes import qwerty
from js_to_hid import convert
from request_parsers import keystroke


class ConvertJsToHIDTest(unittest.TestCase):

    def test_converts_simple_qwerty_keystroke(self):
        modifiers, hid_keycode = convert(
            keystroke.Keystroke(left_meta_modifier=False,
                                left_alt_modifier=False,
                                left_shift_modifier=False,
                                left_ctrl_modifier=False,
                                right_alt_modifier=False,
                                key='a',
                                key_code=65), 'qwerty')
        self.assertEqual(0, modifiers)
        self.assertEqual(qwerty.KEYCODE_A, hid_keycode)

    def test_converts_shifted_keystroke(self):
        modifiers, hid_keycode = convert(
            keystroke.Keystroke(left_meta_modifier=False,
                                left_alt_modifier=False,
                                left_shift_modifier=True,
                                left_ctrl_modifier=False,
                                right_alt_modifier=False,
                                key='A',
                                key_code=65), 'qwerty')
        self.assertEqual(0x02, modifiers)
        self.assertEqual(qwerty.KEYCODE_A, hid_keycode)

    def test_converts_keystroke_with_all_modifiers_pressed(self):
        modifiers, hid_keycode = convert(
            keystroke.Keystroke(left_meta_modifier=True,
                                left_alt_modifier=True,
                                left_shift_modifier=True,
                                left_ctrl_modifier=True,
                                right_alt_modifier=True,
                                key='A',
                                key_code=65), 'qwerty')
        self.assertEqual(0x4f, modifiers)
        self.assertEqual(qwerty.KEYCODE_A, hid_keycode)

    def test_converts_left_ctrl_keystroke(self):
        modifiers, hid_keycode = convert(
            keystroke.Keystroke(left_meta_modifier=False,
                                left_alt_modifier=False,
                                left_shift_modifier=False,
                                left_ctrl_modifier=True,
                                right_alt_modifier=False,
                                key='Control',
                                key_code=17), 'qwerty')
        self.assertEqual(0x01, modifiers)
        self.assertEqual(qwerty.KEYCODE_LEFT_CTRL, hid_keycode)

    def test_converts_simple_azerty_keystroke(self):
        modifiers, hid_keycode = convert(
            keystroke.Keystroke(left_meta_modifier=False,
                                left_alt_modifier=False,
                                left_shift_modifier=False,
                                left_ctrl_modifier=False,
                                right_alt_modifier=False,
                                key='a',
                                key_code=65), 'azerty')
        self.assertEqual(0, modifiers)
        self.assertEqual(azerty.KEYCODE_A, hid_keycode)