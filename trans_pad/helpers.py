from enum import Enum, EnumMeta


class PopUpButtonHelper:
    _objc = None
    _values = dict()

    def __init__(
        self, objc_obj, values: EnumMeta, selected_value: Enum, text_map: dict
    ):
        self._objc = objc_obj
        self._objc.removeAllItems()

        index = 0
        selected_index = 0
        for value in list(values):
            self._objc.addItemWithTitle_(text_map[value])
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
