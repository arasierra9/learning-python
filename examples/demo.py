def hotel_cost(nights):
    return 140 * nights


def plane_ride_cost(city):
    if city == "Charlotte":
        return 183
    elif city == "Tampa":
        return 220
    elif city == "Pittsburgh":
        return 222
    elif city == "Los Angeles":
        return 475

def rental_car_cost(days):
    if days >= 7: discount = 50
    elif days >= 3: discount = 20
    else: discount = 0
    return (days * 40) - discount