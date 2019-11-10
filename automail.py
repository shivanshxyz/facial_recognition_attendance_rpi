import yagmail

receiver = "shivanshyadav00@gmail.com"
body = "Attendence File"
filename = "Attendance\Attendance_2019-08-29_13-09-07.csv"
yag = yagmail.SMTP("mygmail@gmail.com", "mypassword")


yag.send(
    to=receiver,
    subject="Attendance Report",
    contents=body,
    attachments=filename,
)
