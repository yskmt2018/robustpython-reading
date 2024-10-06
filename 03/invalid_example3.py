def get_restaurant_name(city: str) -> str:
    """国や地域によってレストランの名前を変える"""
    if city in ITALY_CITIES:
        return "Trattoria Viafore"
    if city in GERMANY_CITIES:
        return "Pat's Kantine"
    if city in US_CITIES:
        return "Pat's Place"
    return None


if get_restaurant_name('Boston'):
    print('Location Found')

ITALY_CITIES = []
GERMANY_CITIES = []
US_CITIES = []
