from enum import Enum, EnumMeta

from Cocoa import NSLog


class Logger:
    def debug(self, *args):
        NSLog(' '.join(map(str, args)))


class PopUpButtonHelper:
    _objc = None
    _values = None

    def __init__(
        self, objc_obj, values: EnumMeta, selected_value: Enum, text_map: dict
    ):
        self._objc = objc_obj
        self._objc.removeAllItems()
        self._values = dict()

        index = 0
        selected_index = 0
        if isinstance(list(text_map.keys())[0], type(selected_value)):
            text_map_key_type_is_enum = True
        else:
            text_map_key_type_is_enum = False

        for value in list(values):
            if text_map_key_type_is_enum:
                self._objc.addItemWithTitle_(text_map[value])
            else:
                self._objc.addItemWithTitle_(text_map[value.value])
            self._values[index] = value

            if value == selected_value:
                selected_index = index

            index += 1

        self._objc.selectItemAtIndex_(selected_index)
        return

    @property
    def selected_value(self):
        index = self._objc.indexOfSelectedItem()
        return self._values[index]
