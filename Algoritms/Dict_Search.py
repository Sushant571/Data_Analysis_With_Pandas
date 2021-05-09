dict_1 = {
    1: {"Name" : "Sushant", 'Age' : 13,'Class':8,'Section' : 'C','School' : 'Delhi Public School'},
    2:{"Name" : "Harjot", 'Age' : 13,'Class':8,'Section' : 'D','School' : 'Maurya School'},
    3:{"Name" : "Abhimanyu", 'Age' : 8,'Class':3,'Section' : 'E','School' : 'Maurya School'}
    }
def get_student_details(roll_number):
     return dict_1[roll_number]

if __name__ == "__main__":
    try:
       student_details = get_student_details(3)
       print(student_details.get('Age'))
    except KeyError:
        print("Student Not Found..")
