fav_dishes = {"Monday":"Biryani",
              "Tuesday":"Tikka",
              "Wednesday":"Korma",
              "Thursday":"Pasta",
              "Friday":"Pizza",
              "Saturday":"Jack Daniels",
              "Sunday":"Nimbu"}

dishes_cooked = {"Monday":"Pizza",
              "Tuesday":"Tikka",
              "Wednesday":"Aloo",
              "Thursday":"Pasta",
              "Friday":"Biryani",
              "Saturday":"Jack Daniels",
              "Sunday":"Nimbu"}
print("\n\nFavorite Dishes that you will get this week are:-\n")
for key,val in fav_dishes.items():
    if val == dishes_cooked[key]:
        print("{:^10}:{:^10}".format(key,val))