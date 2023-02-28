import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="admin",
  password="zabai@2020",
  database="helvetas_local"
)

mycursor = mydb.cursor()

tableArray = ["mdl_local_custom_report","mdl_local_attempt_user_list","mdl_local_all_progress_max_percentage","mdl_local_helvetas_examcourse_info","mdl_local_user_enrolled_scorm_courses"]

for i in tableArray:
    query = "check table " + i
    mycursor.execute(query)
    myresult = mycursor.fetchall()
    status = str(myresult[0][3])
    # print(status)
    if status == 'OK':
        repair = "REPAIR TABLE helvetas_local." + i
        mycursor.execute(repair, multi=True)
        print("repaired: ", i)
    else:
        print(i, " is ", status, " and skipped.")

mydb.commit()