import csv
import datetime

# column header - contract file
CONTRACT_HEADER_STUDENT_ID = 6 
CONTRACT_HEADER_EMAIL = 100

# column header - same level file
SAME_HEADER_MAIN_TEACHER = 0
SAME_HEADER_ID = 1
SAME_HEADER_NAME_ENG = 2
SAME_HEADER_NAME_JP = 3
SAME_HEADER_CONTRACT = 5
SAME_HEADER_CONTRACT = 5
SAME_CANT_LEVEL_UP = 12
SAME_COMMENT = 13

# column header - formatted email ready same level file
FORM_HEADER_ID = 0
FORM_HEADER_NAME_JP = 1
FORM_HEADER_NAME_ENG = 2
FORM_HEADER_EMAIL = 3
FORM_HEADER_MAIN_TEACHER = 4
FORM_HEADER_CONTRACT = 5
FORM_HEADER_TEACHER_COMMENT = 6


def create_same_level_list(contract_filepath, same_level_filepath):

    same_level_email_list = []

    print("Starting to read contract file...")
    contract_data = read_file(contract_filepath)
    print("Read contract file successfully...")

    print("Starting to read same level file...")
    same_level_data = read_file(same_level_filepath)
    print("Read same level file successfully...")

    print("Search for student email addresses...")

    # search down the list of data in same level data
    for i in range(len(same_level_data)):
        send_email = False

        # check that the student should be sent an email (not level up and comment)
        cant_level_up = same_level_data[i][SAME_CANT_LEVEL_UP]
        teacher_comment = same_level_data[i][SAME_COMMENT]

        if (cant_level_up == "TRUE"):
            if (teacher_comment != ""):
                send_email = True

        # skip to next student if not considered for email
        if (send_email == False):
            continue

        student_name_JP = same_level_data[i][SAME_HEADER_NAME_JP]
        student_name_ENG = same_level_data[i][SAME_HEADER_NAME_ENG]
        main_teacher = same_level_data[i][SAME_HEADER_MAIN_TEACHER]
        contract = same_level_data[i][SAME_HEADER_CONTRACT]
        comment = same_level_data[i][SAME_COMMENT]

        student_id = same_level_data[i][SAME_HEADER_ID]
        student_email = "Not found"

        # find the matching student data in the contract file
        for k in range(len(contract_data)):
            id_to_compare = contract_data[k][CONTRACT_HEADER_STUDENT_ID]

            # if the matching student id is found, stop looping and record their email address
            if (student_id == id_to_compare):
                print("Found the student ID match.")
                student_email = contract_data[k][CONTRACT_HEADER_EMAIL]
                break

        # create the entry
        item_to_append = [student_id, student_name_JP, student_name_ENG, student_email, contract, main_teacher, comment]
        same_level_email_list.append(item_to_append)
        print(item_to_append)

    print("Finished creating formatted same level list...")
    create_CSV_file(same_level_email_list)


def create_CSV_file(same_level_email_list):

    header = ["Student ID", "Student Name (JP)", "Student Name (Eng)", "Student Email", "Student Contract", "Main Teacher", "Teacher Comment"]

    with open('email_ready_same_level_students.csv', 'w', newline='', encoding='utf-8-sig') as f:

        #f.write('\ufeff') # to write JP char set

        # using csv.writer method from CSV package
        write = csv.writer(f, delimiter=",")
        write.writerow(header)
        write.writerows(same_level_email_list) 

def read_file(filepath):

    new_list = []

    with open(filepath, encoding="utf-8-sig", errors='ignore') as f:
        csv_reader = csv.reader(f)

        # skip the first row
        next(csv_reader)

        # write csv data to a list
        for line in csv_reader:
            new_list.append(line)
    
    return new_list