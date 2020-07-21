# Should return
#   - morning
#   - noon
#   - afternoon
#   - evening
#   - night

def get_part_of_day_from_hour(hour):
   if hour <=11:
      return 'Morning'
   elif hour == 12:
      return 'Noon'
   elif hour >= 22:
      return 'Night'
   elif hour > 19:
      return 'Evening'
   elif hour > 12:
      return 'Afternoon'

def is_evening(hour):
   return get_part_of_day_from_hour(hour) == 'Evening'
