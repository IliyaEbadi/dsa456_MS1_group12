import csv 
def cleanParisData(mydata):
    data_p = [row for row in mydata] #writing the data into data_p
    headers = ['edition', 'edition_id', 'Country', 'NOC', 'number_of_athletes', 'gold_medal_count', 'silver_medal_count', 'bronze_medal_count', 'total_medals'] #writing the header for the files
    #making each csv file
    create_csv('new_olympic_athlete_bio.csv', headers, data_p)
    create_csv('new_olympic_athlete_event_results.csv', headers, data_p)
    create_csv('new_olympics_country.csv', headers, data_p)
    create_csv('new_olympics_games.csv', headers, data_p)
    create_csv('new_medal_tally.csv', headers, data_p)
def create_csv(filename, headers, data):
    #This function will create a csv file based on the parameters given
    try:
        with open(filename, 'w', newline='', encoding='utf-8') as file:
            w = csv.writer(file)
            w.writerow(headers) #writing the header
            w.writerows(data) #writing the data of all rows
        print(f"CSV file'{filename}' created")
    except Exception as e:
         print (f"Error")
all_data = [
    ['Alice', 25, 'New York', 'NOC FOR ALICE', '6', '2', '6', '8', '16'],
    ['Bob', 30, 'London', 'NOC FOR BOB', '6', '3', '4', '7', '14'],
    ['Charlie', 35, 'Paris', 'NOC FOR Charlie', '5', '3', '8', '2', '13'],
    ['David', 28, 'Paris', 'NOC FOR DAVID', '7', '2', '9', '3', '14'],
    ['Eve', 32, 'Tokyo', 'NOC FOR EVE', '6', '2', '6', '8', '16']
]
cleanParisData(all_data)
            