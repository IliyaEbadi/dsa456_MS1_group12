import csv
def cleanParisData(mydata):
    """
    Prototype stub function.

    Accepts:
        mydata -> list of rows (Paris dataset)

    Purpose:
        In MS2, this function will clean and normalize
        the Paris dataset so that it matches the original schema.

    Returns:
        Cleaned dataset (not implemented in MS1)
    """
    data_p = mydata[:]   # simple copy for prototype

    # Header required for medal tally file (exact order as specified)
    headers = [
        'edition',
        'edition_id',
        'Country',
        'NOC',
        'number_of_athletes',
        'gold_medal_count',
        'silver_medal_count',
        'bronze_medal_count',
        'total_medals'
    ]

    # Creating all 5 required files for MS1 prototype
    create_csv('new_olympic_athlete_bio.csv', headers, data_p)
    create_csv('new_olympic_athlete_event_results.csv', headers, data_p)
    create_csv('new_olympics_country.csv', headers, data_p)
    create_csv('new_olympics_games.csv', headers, data_p)
    create_csv('new_medal_tally.csv', headers, data_p)


def create_csv(filename, headers, data):
    """
    Creates a CSV file with the provided header and data.

    Parameters:
        filename -> name of output file
        headers  -> list of column names
        data     -> list of rows

    MS1 NOTE:
        This function simply creates the required output files.
        No real data processing is performed yet.
    """

    try:
        with open(filename, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)

           
            writer.writerow(headers)

            
            writer.writerows(data)

        print(f"CSV file '{filename}' created successfully.")

    except Exception as e:
        print("Error while creating file:", filename)
        print(e)



# Dummy data used ONLY for MS1 prototype demonstration.
# In MS2, actual dataset files will be read and processed.

all_data = [
    ['Alice', 25, 'New York', 'NOC FOR ALICE', '6', '2', '6', '8', '16'],
    ['Bob', 30, 'London', 'NOC FOR BOB', '6', '3', '4', '7', '14'],
    ['Charlie', 35, 'Paris', 'NOC FOR Charlie', '5', '3', '8', '2', '13'],
    ['David', 28, 'Paris', 'NOC FOR DAVID', '7', '2', '9', '3', '14'],
    ['Eve', 32, 'Tokyo', 'NOC FOR EVE', '6', '2', '6', '8', '16']
]



# Prototype execution

if __name__ == "__main__":
    # Calling prototype cleaning function
    cleanParisData(all_data)

    print("MS1 Prototype execution completed.")
