def hotel_cost(nights):
    # Hotel per night is $140
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
      if days >= 7:
          discount = 50
      elif days >= 3:
          discount = 20
      else:
          discount = 0
      return (days * 40) - discount

def trip_cost(city,days):
    return rental_car_cost(days) + hotel_cost(days - 1) + plane_ride_cost(city)