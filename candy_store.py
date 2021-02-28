def buying_candy( amount_of_money ):
  if amount_of_money < 1:
    return 0
  elif amount_of_money <= 2:
    value = 1 * amount_of_money
    return value
  elif amount_of_money > 2:
    value = (1 * amount_of_money) + 1
    return value


buying_candy(2)