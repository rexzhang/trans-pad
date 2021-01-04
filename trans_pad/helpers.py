from enum import Enum, EnumMeta
from typing import Optional, Union

from Cocoa import NSLog


class Logger:
    def debug(self, *args):
        NSLog(' '.join(map(str, args)))


class PopUpButtonHelper:
    _objc = None
    _values = None

    def __init__(
        self, objc_obj,
        values: Union[EnumMeta, dict, list, tuple], selected_value: any,
        text_map: Optional[dict] = None
    ):
        self._objc = objc_obj
        self._objc.removeAllItems()
        self._values = list()

        if isinstance(values, EnumMeta) and isinstance(selected_value, Enum):
            self._init_from_enum(
                values=values, selected_value=selected_value, text_map=text_map
            )

        elif isinstance(values, dict):
            self._init_from_dict(
                values=values, selected_value=selected_value, text_map=text_map
            )

        elif isinstance(values, (list, tuple)):
            self._init_from_list(
                values=values, selected_value=selected_value, text_map=text_map
            )
        else:
            raise Exception(
                type(values), values, type(selected_value), selected_value
            )

        return

    def _init_from_enum(
        self, values: EnumMeta, selected_value: Enum, text_map: Optional[dict]
    ) -> None:
        index = 0
        if text_map and isinstance(
            list(text_map.keys())[0], type(selected_value)
        ):
            text_map_key_type_is_enum = True
        else:
            text_map_key_type_is_enum = False

        for value in list(values):
            title = None
            if text_map:
                if text_map_key_type_is_enum:
                    title = text_map[value]
                else:
                    title = text_map[value.value]

            self._append_pop_up_button_item(
                value=value, title=title, index=index,
                selected_value=selected_value
            )
            index += 1

        return

    def _init_from_dict(
        self, values: dict, selected_value: any, text_map: Optional[dict]
    ) -> None:
        index = 0
        for value in values.keys():
            if text_map is None:
                title = value
            else:
                title = text_map[value]

            self._append_pop_up_button_item(
                value=value, title=title, index=index,
                selected_value=selected_value
            )
            index += 1

        return

    def _init_from_list(
        self, values: Union[list, tuple],
        selected_value: any, text_map: Optional[dict]
    ) -> None:
        index = 0
        for value in values:
            if text_map is None:
                title = value
            else:
                title = text_map[value]

            self._append_pop_up_button_item(
                value=value, title=title, index=index,
                selected_value=selected_value
            )
            index += 1

        return

    def _append_pop_up_button_item(
        self, index: int, value: any, title: Optional[str], selected_value: any
    ) -> None:
        self._values.append(value)

        if title is None:
            title = value
        self._objc.addItemWithTitle_(title)

        if value == selected_value:
            self._objc.selectItemAtIndex_(index)

    @property
    def selected_value(self):
        index = self._objc.indexOfSelectedItem()
        return self._values[index]
