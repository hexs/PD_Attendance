import time
from PD_Attendance import PD_Attendance
from update_git import if_status_change_add_commit_push

while True:
    try:
        attendance.view_state_to_csv()
        if_status_change_add_commit_push()
    except:
        print('except')
        attendance = PD_Attendance()
        attendance.log_in()
    time.sleep(1)
