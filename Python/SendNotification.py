import smtplib
import mysql.connector

###########################################################################
def Email(user, task):
        sender = 'code.way.2016@gmail.com'
        to = [user]
        subject = 'Pending task'
        body = 'You have pending tasks: \n\n%s' % (task)
        message = 'Subject: %s \n\n %s' % (subject, body)
        try:
                server_ssl = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                server_ssl.ehlo()
                server_ssl.login('code.way.2016@gmail.com', 'Code@Way')
                server_ssl.sendmail(sender, to, message)
                server_ssl.close()
                print('sent')
        except:
                print("Something is wrong")
        return
###########################################################################

conn = mysql.connector.connect(host="localhost",user="root", passwd="root", database="split_task")

cur = conn.cursor()
cur.execute("SELECT email,group_concat(TASK_NAME) FROM split_task.task_status INNER JOIN split_task.customers_auth ON task_status.LOGIN_ID=customers_auth.uid INNER JOIN split_task.task_master ON task_status.TASK_ID = task_master.TASK_ID WHERE task_status.STATUS='Pending' and DUE_DATE=CURDATE() group by email;")
rows = cur.fetchall()
for row in rows:
        user = row[0]
        task = row[1]
        Email(user,task)
cur.close()
conn.close()

