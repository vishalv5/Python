# # student
# import csv
# def create_file(filename):
#     with open(filename,"w") as file:
#         file.write("Userid,Name,score\n")
#         file.write("NO001,Vishal,50\n")
#         file.write("NO002,Vishu,40\n")
#         file.write("NO003,Vivek,30\n")
#         file.write("NO004,ViKas,32\n")


# def count_items(filename):
#     return_string=""
#     create_file(filename)

#     with open("student.csv","r") as file:
#         reader=csv.DictReader(file)
#         for row in reader:
#             return_string+= "{}--{}--{}\n".format(row["Userid"],row["Name"],row["score"])
#     return return_string

# print(count_items("Student.csv"))



# import csv
# with open("student.csv") as file:
#     reader=csv.DictReader(file)
#     for row in reader:
#         # Userid, Name,score= row
#         print("{}--{}--{}".format(row["Userid"],row["Name"],row["score"]))


#
# import os
# print(
# os.path.exists("flowers.csv"))


import os
import sys

# Check that at least one command-line argument is provided
if len(sys.argv) < 2:
    print("ERROR: Missing command-line argument!")
    print("Exiting program...")
    sys.exit(1)

# Access the first command-line argument (sys.argv[1]) and store it in a variable
csv_file = sys.argv[1]

# Check if the file exists
if not os.path.exists(csv_file):
    print(f"{csv_file} does not exist")
    print("Exiting program...")
    sys.exit(1)

# Now you can use the csv_file variable in your script for further processing.
with open(csv_file, 'r') as file:
    content = file.read()
    # Process the file content as needed
