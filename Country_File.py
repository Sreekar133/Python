input_filename = "country_info.txt"
countries = {}
current_choice = None
with open(input_filename) as country_file:
    country_file.readline()
    for row in country_file:
        data = row.strip('\n').split('|')
        country, capital, code, code3, dialing, timezone, currency = data
        #print(country,capital,code,code3,dialing,timezone,currency,sep='\n\t')

        country_dict = {"country" : country,
                        "capital" : capital,
                        "code" : code,
                        "code3" : code3,
                        "dialing" : dialing,
                        "timezone" : timezone,
                        "currency" : currency,
                        }
        #print(country_dict)
        countries[capital.casefold()]=country_dict
        #capital[capital.casefold()]=country_dict

#print(countries)
# while True:
#     current_choice = input("please enter the country ").casefold()
#     # if current_choice == "antartica":
#         #print("There is no capital city")
#     if current_choice in countries:
#         country_dict = countries[current_choice]
#         print(country_dict['capital'])
#     elif current_choice == "quit":
#             break


while True:
    capital_choice = ' '
    if capital_choice in countries:
        country_dict = countries[capital]
        print(country_dict)
