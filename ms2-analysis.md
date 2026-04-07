- Describe the assumptions and decisions you made. Example, how did you reconcile data for Paris Olympics with Other data? How did you handle missing data?

We have created a  create_csv class with Filename, header, and data as the parameters. We used the open function to create a CSV by calling the filename parameter that holds the name of the CSV file,  used ‘w’ to open this file in write mode and set its name to file. We would use the csv.writer to create an object called writer with writerow and write rows to create headers and fill our data. If this was successful, we will print on our console CSV (Your file name) created successfully. How we handled missing data is by using the try function. If any of these functions above fail, we have an exception clause that will print on our console “error while creating file: (your file name). As well as print the error that has happened.
- Describe the data structures you used in your application and whether you wrote your own or used a built in python data structure
    - Describe the general way the data is manipulated by your program
    - Why did you choose the data structure you chose? How did you use it?
      - Example, if you used a dictionary, what is the key?  what did it give you?  what was the cost of using it? How fast is it to find the information that you need? etc.
