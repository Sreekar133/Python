vehicles = {'dream': 'Honda 250T',
            'roadster': 'BMW R1100',
            'er5': 'Kawasaki ER5',
            'can-am':'Bombardier Can-am 250',
            'virago': 'Yamaha xv250',
            'tenere': 'Yamaha XT650',
            'jimny': 'Suzuki Jimny 1.5',
            'fiesta': 'Ford Fiesta Ghia 1.4'}

vehicles["starfighter"] = "Lockheed F-104"
vehicles["learjet"] = "Bombardier Learjet 75"
vehicles["toy"] = "glider"
vehicles["f1"] = "f1"
# for key in vehicles:
#     print(key,vehicles[key],sep=":")

for key,values in vehicles.items():
    print(key,values,sep=",")

