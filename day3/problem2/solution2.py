max_boat_load = int(input())
adults = int(input())
kids = int(input())
current_load = adults*75 + kids*30

if current_load < max_boat_load:
    print("Boat is stable")
else:
    print('Boat will sink')
