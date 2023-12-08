import datetime
class Activity_Tracker:
    def __init__(self):
        self.activity_log = []

    def log_activity(self, admin_name, action):
        timestamp = datetime.datetime.now()
        log_entry = {
            'timestamp': timestamp,
            'admin': admin_name,
            'action': action
        }
        self.activity_log.append(log_entry)

    def view_activity_log(self):
        for entry in self.activity_log:
            print(f"{entry['timestamp']} - Admin Name '{entry['admin']}' performed '{entry['action']}'")

activity_tracker = Activity_Tracker()

activity_tracker.log_activity("Ashik", "Logged in")
activity_tracker.log_activity("Ashik","Change settings")
activity_tracker.log_activity("Ashik", "Logged out")
activity_tracker.view_activity_log()
