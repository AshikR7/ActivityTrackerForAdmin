
import datetime
class Activity_Tracker:
    def __init__(self):
        self.activity_log = []

    def log_activity(self, user, action):
        timestamp = datetime.datetime.now()
        log_entry = {
            'timestamp': timestamp,
            'user': user,
            'action': action
        }
        self.activity_log.append(log_entry)

    def view_activity_log(self):
        for entry in self.activity_log:
            print(f"{entry['timestamp']} - User '{entry['user']}' performed '{entry['action']}'")

activity_tracker = Activity_Tracker()

activity_tracker.log_activity("Admin", "Logged in")
activity_tracker.log_activity("Admin","Change settings")
activity_tracker.log_activity("Admin", "Logged out")

activity_tracker.view_activity_log()