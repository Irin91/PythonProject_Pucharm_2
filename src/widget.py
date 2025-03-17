def get_mask_card_number(user_card_number: str) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску"""
    return f"{user_card_number[:4]} {user_card_number[4:6]}** **** {user_card_number[12:]}"

def get_mask_account(user_card_number: str) -> str:
    """Функция принимает на вход номер счета и возвращает его маску"""
    return f"**{user_card_number[-4:]}"

def mask_account_card(card_or_account: str) -> str:
    """ Функция принимает строку, содержащую тип и номер карты или счета"""
    card_or_account_string = card_or_account.split()
    if "Счет" in card_or_account_string:
        return f"Счет {get_mask_account(card_or_account_string[1])}"
    elif "Maestro" in card_or_account_string:
        return f"Maestro {get_mask_account(card_or_account_string[1])}"
    elif "Visa" in card_or_account_string:
        card_numbers = []
        card_name = []
        for i in card_or_account_string:
            if i.isdigit():
                card_numbers.append(i)
            if i.isalpha():
                card_name.append(i)
        str_card_numbers = "".join(card_numbers)
        return f" {card_name [0]} {card_name[1]} {get_mask_card_number(str_card_numbers)}"


def get_date(current_date: str) -> str:
    """ Функция, которая меняет формат даты """
    date_format_change = datetime.strptime(current_date, format: "YYYY-MM-DDTOO:MM:SS.SSSSSS")
    return date_format_change.strftime("DD.MM.YYYY")


print(get_date("2024-03-11T02:26:18.671407"))
print(mask_account_card("Visa Platinum 8990922113665229"))














