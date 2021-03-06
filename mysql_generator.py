

# using INSERT IGNORE prevents duplicates in the db
def generate_insert_statement(table_name, column_name, email):
    return "INSERT IGNORE INTO " + table_name + "(" + column_name + ") VALUES(\'" + email + "\');"


def generate_mysql(fn, table_name, column_name):
    input_file = open("email_list_output.txt", "r")
    readable_input_file = input_file.readlines()
    mysql_statement = ""

    if len(readable_input_file) != 0:
        for email in readable_input_file:
            mysql_statement += generate_insert_statement(table_name.rstrip('\n'), column_name.rstrip('\n'), email.rstrip('\n')) + "\n"
    else:
        raise EOFError(fn + ' contained no emails!')

    input_file.close()
    return mysql_statement


