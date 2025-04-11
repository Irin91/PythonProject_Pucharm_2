from datetime import datetime


def mask_account_card(card_number: str) -> str:
    """ Функция принимает строку, содержащую тип и номер карты или счета"""
    account = "Счет"
    if account in card_number:
        return f"Счет **{card_number[-4:]}"
    else:
        list_card_name = card_number.split()
        card_name = []
        for i in list_card_name:
            if i.isalpha():
                card_name += i
            elif i.isdigit():
                card_numbers = i
        return f"{"".join(card_name)} {card_numbers[0:4]} {card_numbers[4:6]}** **** {card_numbers[-4:]}"


def get_date(current_date: str) -> str:
    """ Функция, которая меняет формат даты """
    date_format_change = datetime.strptime(current_date, "%Y-%m-%dT%H:%M:%S.%f")
    return date_format_change.strftime("2024-03-11T02:26:18.671407")


if __name__ == "__main__":
    print(mask_account_card("Visa 1234567890123456"))  # Visa 1234 56** **** 3456
    print(mask_account_card("МИР 1234567890123456"))  # МИР 1234 56** **** 3456
    print(mask_account_card("Maestro Electron 1234567890123456"))  # Maestro Electron 1234 56** **** 3456
    print(mask_account_card("Счет 12345678901234567890"))  # Счет **7890
    print(get_date("2024-03-11T02:26:18.671407"))
