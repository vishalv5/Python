# # student
import csv
def create_file(filename):
    with open(filename,"w") as file:
        file.write("Userid,Name,score\n")
        file.write("NO001,Vishal,50\n")
        file.write("NO002,Vishu,40\n")
        file.write("NO003,Vivek,30\n")
        file.write("NO004,ViKas,32\n")


def count_items(filename):
    return_string=""
    create_file(filename)

    with open("student.csv","r") as file:
        reader=csv.DictReader(file)
        for row in reader:
            return_string+= "{}--{}--{}\n".format(row["Userid"],row["Name"],row["score"])
    return return_string

print(count_items("Student.csv"))



