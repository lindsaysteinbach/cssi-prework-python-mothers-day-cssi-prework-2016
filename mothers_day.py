def mothers_day():
  return "Happy Mother's Day, Mom!"

def better_mothers_day(name):
  return "Happy Mother's Day, {input_name}!".format(input_name=name)

def best_mothers_day(name="Mom"):
  return "Happy Mother's Day, {input_name}!".format(input_name=name)

def holiday_greeting(recipient="Mom", sender="Your Favorite Child", holiday="Mother's Day"):
  return "Happy {input_holiday}, {input_to}! - From {input_from}".format(input_to=recipient, input_from=sender, input_holiday=holiday)

