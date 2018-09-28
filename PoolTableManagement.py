
from datetime import datetime
import json
now = datetime.now()
table_list = []
occupied_table_list = []
unoccupied_table_list = []

#---------------------------------------------------------------
class PoolTable:
    def __init__(self, number):
        self.number = number
        self.status = 'unoccupied'
        self.start_date_time = datetime.now()
        self.end_date_time = datetime.now()
        self.playing_duration = 0
        self.cost = 0
    # def __repr__(self):
    #     return 'Table {0}'.format(self.number)

#---------------------------------------------------------------
class OccupiedTable(PoolTable):
    def __init__(self, number, start_date_time, end_date_time, playing_duration, cost):
        super().__init__(number)
        self.status = 'occupied'
        self.start_date_time = datetime.now()
        self.end_date_time = datetime.now()
        self.playing_duration = 0
        self.cost = 0

    def __repr__(self):
        return 'Table {0}, status: {1}, start time : {2}, end time : {3}, duration : {4},cost :{5}'.format(self.number,self.status, self.start_date_time,self.end_date_time, self.playing_duration, self.cost)

    def open_table(self):
        start_time = datetime.now()
        self.start_date_time = start_time
        occupied_table_list.append(table)
        print(occupied_table_list)


    def close_table(self):
        while True:
            close_table = input('Enter table number to close the table or q to exit: ')

            if close_table == 'q':
                break

            for i in range(0,len(occupied_table_list)):

                if close_table == occupied_table_list[i].number:
                    print("table is closed")
                    end_date_time = datetime.now()
                    occupied_table_list[i].end_date_time = end_date_time
                    duration = end_date_time - occupied_table_list[i].start_date_time
                    occupied_table_list[i].playing_duration = duration
                    occupied_table_list[i].status = 'unoccupied'
                    occupied_table_list[i].playing_duration = duration
                    minutes = (duration.seconds / 60)
                    hours = minutes / 60
                    cost = 30 * hours
                    occupied_table_list[i].cost = cost   #hard mode
                    if(duration.seconds >= 3600):
                        game_hour = float(duration.seconds / 3600)
                        occupied_table_list[i].playing_duration = game_hour #hard mode
                    print(occupied_table_list[i])
                    break



    def status_table(self):
        for table in occupied_table_list:
            if(table.status != 'occupied'):
                unoccupied_table_list.append(table.number)
                print(unoccupied_table_list)

#-----------------------------------------------------------------
is_occupied = False

while True:

    assign_table = input('Enter the table number to assign or q to exit: ')
    if(assign_table == 'q'):
        break


    for i in range(0,len(occupied_table_list)):
        if(occupied_table_list[i].number == assign_table):
            print('Oopps! Please enter a valid table number to open:')
            is_occupied = True
            break
        else:
            is_occupied = False

    if(is_occupied == False):
        table = OccupiedTable(assign_table,0,0,0,0)
        table.open_table()
        table.status = 'occupied'
        table.status_table()
table.close_table()


for i in range(1,13):
    pool_table = PoolTable(str(i))
    table_list.append(pool_table)

for item in table_list:
    if(item.number == table.number and item.status != table.status):
        table_list.append(table)
        table_list.remove(item)


print(table_list)

#------------------------json-file---------------------------------

pool_table_json = []
class PoolTableJson:
    def __init__(self):
        self.number = ""
        self.start_game_time = ""
        self.end_game_time = ""
        self.game_time = ""
        self.game_cost = ""
    def asDictionary(self):
        return self.__dict__

for table in table_list:
    game_table = PoolTableJson()
    game_table.number = table.number
    game_table.start_game_time = table.start_date_time.isoformat()
    game_table.end_game_time = table.end_date_time.isoformat()
    game_table.game_time = str(table.playing_duration)
    game_table.game_cost = table.cost
    pool_table_json.append(game_table.asDictionary())
with open ('pool_table_game.json', 'w') as object_file:
    json.dump(pool_table_json, object_file)
