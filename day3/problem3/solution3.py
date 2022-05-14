electric_unit = int(input())

if electric_unit <= 200:
    print(f'Rs.{round(electric_unit*0.5)}')
elif electric_unit > 200 and electric_unit <= 400:
    print(f'Rs.{round(electric_unit*0.65+100)}')
elif electric_unit > 400 and electric_unit <= 600:
    print(f'Rs.{round(electric_unit*0.80+200)}')
else:
    print(f'Rs.{round(electric_unit*1.25+425)}')
