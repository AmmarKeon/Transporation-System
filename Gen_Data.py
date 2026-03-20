import random
import uuid

plate = ["MASR", "NASR", "AIU"]
type_v = ["bus", "mini-bus", "limousine"]

def random_data(plate, type_v, number_lines):
    data = ""
    cap_bus = [20, 32, 50, 60]
    cap_minibus = [14, 7]
    cap_limo = 4
    
    plates_res = []
    cap_res = []
    
    while (number_lines != 0):
        data += random.choice(type_v)
        
        if data == "bus":
            data += ","
            
            cap = str(random.choice(cap_bus))
            cap_res.append(cap)
            data += str(cap)
            data += ","
            
            p = random.choice(plate) + (str(number_lines))
            plates_res.append(p)
            data += p
            data += ","
        elif data == "mini-bus":
            data += ","
            
            cap = str(random.choice(cap_minibus))
            cap_res.append(cap)
            data += str(cap)
            data += ","
            
            p = random.choice(plate) + (str(number_lines))
            plates_res.append(p)
            data += p
            data += ","
        else:
            data += ","
            
            cap = str(cap_limo)
            cap_res.append(cap)
            data += str(cap)
            data += ","
            
            p = random.choice(plate) + (str(number_lines))
            plates_res.append(p)
            data += p
            data += ","
        
        print(data)
        
        data = ""
        
        number_lines -= 1
    
    return plates_res, cap_res
        
plates_in_database, cap_for_trips = random_data(plate, type_v, 45)

print("________________________________________________________________________________________________________________________________________________________________________\n")

def random_trip(plates_in_database, cap_for_trips, number_lines):
    journeyType = ["internal", "external"]
    tripType = ["one-way", "round-trip"]
    num_of_stops = [0, 1 , 2, 3]
    year = "2024"
    month = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    days = [num for num in range(1, 31)]
    hours = [num for num in range(1, 23)]
    minu = [num * 10 for num in range(1, 6)]
    
    while (number_lines != 0):
        ext = ["Alexandria", "Cairo", "Loxur", "Aswan", "Giza", "Sharm-Elshikh", "Marsa Matrouh"]
        inter = ["Smouha", "Roushdy", "Bahari", "Shatby", "Gleem", "Mahtet Elraml", "Miami", "Sidi Gaber", "Sidi Bishr", "Montazah"]
        data = ""
        price = 0
        
        id = uuid.uuid1()
        
        data += str(id) + ","
        type_j = random.choice(journeyType)
        
        data += type_j + ","
        
        if type_j == "internal":
            source = random.choice(inter)
            data += source
            data += ","
            inter.remove(source)
            
            dis = random.choice(inter)
            data += dis
            data += ","
            
            price += 200
        else:
            source = random.choice(ext)
            data += source
            data += ","
            ext.remove(source)
            
            dis = random.choice(ext)
            data += dis
            data += ","
            
            price += 400
        
        data += year + ","
        
        data += str(random.choice(month)) + ","
        
        data += str(random.choice(days)) + ","
        
        data += str(random.choice(hours)) + ","
        
        data += str(random.choice(minu)) + ","
        
        no = random.choice(num_of_stops)
        data += str(no) + ","
        price += no * -20
        
        data += plates_in_database[number_lines - 1] + ","
        
        trip_Type = random.choice(tripType)
        data += trip_Type + ","
        
        if trip_Type == "round-trip":
            price *= 2
        
        data += str(price) + ","
        
        data += cap_for_trips[number_lines - 1] + ","
        
        print(data)
        number_lines -= 1
 
random_trip(plates_in_database, cap_for_trips, 45)