list_chair = []
class Bus:
    count_of_chair = 50
    def __init__(self, destination_from, destination_to):
        self.destination_from = destination_from
        self.destination_to = destination_to
# North of the sector * South of the sector * West of the sector * East of the sector

Bus1 = Bus('North of the sector', 'gaza')
Bus2 = Bus('South of the sector', 'gaza')
Bus3 = Bus('West of the sector ', 'gaza')
Bus4 = Bus('East of the sector', 'gaza')
# *************************
Bus5 = Bus('gaza', 'North of the sector')
Bus6 = Bus('gaza', 'South of the sector')
Bus7 = Bus('gaza', 'West of the sector ')
Bus8 = Bus('gaza', 'East of the sector')
def display():
    print('''
    1-from North of the sector to gaza
    2-from South of the sector to gaza
    3-from West of the sector to gaza
    4-from East of the sector to gaza
    5-from  gaza to North of the sector 
    6-from  gaza to South of the sector 
    7-from  gaza to West of the sector 
    8-from  gaza to  East of the sector 
    ''')
Destination = input('If you want to see the destinations,enter Y if not enter N\t:')
if Destination == 'Y' or Destination == 'y':
    display()
else:
    exit()
while True:
    q = input('If you want to reserve a seat, enter Y , if no, enter N\t:')
    if q == 'Y' or q == 'y':
        n = int(input('Enter The number destination'))
        print('How many chairs are left', 50 - len(list_chair))
        num = int(input("Enter The number chair who you want to book : "))
        if num not in list_chair:
            list_chair.append(num)
            print('The operation successfully')
        else:
            print('The chair is reserved ')
    else:
        exit()
    if len(list_chair) == 50:
        exit()
