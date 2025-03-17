def get_mask_card_number(user_card_number: str) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску"""
    return f"{user_card_number[:4]} {user_card_number[4:6]}** **** {user_card_number[12:]}"

def get_mask_account(user_card_number: str) -> str:
    """Функция принимает на вход номер счета и возвращает его маску"""
    return f"**{user_card_number[-4:]}"


