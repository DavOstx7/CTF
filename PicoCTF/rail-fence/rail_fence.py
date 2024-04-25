from typing import Dict, List, Tuple

FIRST_RAIL_NUMBER = 1
GO_UP = 1
GO_DOWN = -1
VALUE_INDEX = 1


class RailFence:
    def __init__(self, number_of_rails: int):
        assert number_of_rails > 1
        self.number_of_rails = number_of_rails

    @property
    def __last_rail_number(self) -> int:
        return self.number_of_rails

    def _get_number_of_chars_at_each_rail(self, ciphertext: str) -> Dict[int, int]:
        number_of_chars_at_each_rail = {rail_number: 0 for rail_number in range(1, self.number_of_rails + 1)}
        current_rail_number = FIRST_RAIL_NUMBER
        go_direction = GO_UP
        for _ in range(len(ciphertext)):
            number_of_chars_at_each_rail[current_rail_number] += 1
            if go_direction == GO_UP and current_rail_number == self.__last_rail_number:
                go_direction = GO_DOWN
            elif go_direction == GO_DOWN and current_rail_number == FIRST_RAIL_NUMBER:
                go_direction = GO_UP
            current_rail_number += go_direction
        return number_of_chars_at_each_rail

    def _get_ciphered_chars_at_each_rail(self, ciphertext: str) -> Dict[int, str]:
        ciphered_chars_at_each_rail = {rail_number: "" for rail_number in range(1, self.number_of_rails + 1)}
        number_of_chars_at_each_rail = self._get_number_of_chars_at_each_rail(ciphertext)
        current_rail = FIRST_RAIL_NUMBER
        current_number_of_chars = number_of_chars_at_each_rail[current_rail]
        for cipher_char in ciphertext:
            if current_number_of_chars == 0:
                current_rail += 1
                current_number_of_chars = number_of_chars_at_each_rail[current_rail]

            ciphered_chars_at_each_rail[current_rail] += cipher_char
            current_number_of_chars -= 1
        return ciphered_chars_at_each_rail

    def encrypt(self, message: str) -> str:
        chars_at_each_rail = {rail_number: "" for rail_number in range(1, self.number_of_rails + 1)}
        current_rail_number = FIRST_RAIL_NUMBER
        go_direction = GO_UP
        for char in message:
            chars_at_each_rail[current_rail_number] += char
            if go_direction == GO_UP and current_rail_number == self.__last_rail_number:
                go_direction = GO_DOWN
            elif go_direction == GO_DOWN and current_rail_number == FIRST_RAIL_NUMBER:
                go_direction = GO_UP
            current_rail_number += go_direction
        sorted_chars_at_each_rail: List[Tuple[int, str]] = list(
            sorted(chars_at_each_rail.items(), key=lambda key_and_value_pair: key_and_value_pair[VALUE_INDEX])
        )
        return "".join(chars_at_rail for rail_number, chars_at_rail in sorted_chars_at_each_rail)

    def decrypt(self, ciphertext: str) -> str:
        ciphered_chars_at_each_rail = self._get_ciphered_chars_at_each_rail(ciphertext)
        message = ""
        current_rail_number = FIRST_RAIL_NUMBER
        first_rail_index, middle_rails_index, last_rail_index = 0, 0, 0
        go_direction = GO_UP
        for _ in range(len(ciphertext)):
            ciphered_chars = ciphered_chars_at_each_rail[current_rail_number]
            if go_direction == GO_UP and current_rail_number == self.__last_rail_number:
                go_direction = GO_DOWN
                message += ciphered_chars[last_rail_index]
                last_rail_index += 1
                middle_rails_index += 1
            elif current_rail_number == FIRST_RAIL_NUMBER:
                if go_direction == GO_DOWN:
                    go_direction = GO_UP
                    middle_rails_index += 1
                message += ciphered_chars[first_rail_index]
                first_rail_index += 1
            else:
                message += ciphered_chars[middle_rails_index]
            current_rail_number += go_direction
        return message

