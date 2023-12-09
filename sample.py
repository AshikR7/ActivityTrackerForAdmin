from activityTracker import Activity_Tracker

def log_In(name,action):
    activity_tracker = Activity_Tracker()
    activity_tracker.log_activity(name,action)
    activity_tracker.view_activity_log()

def log_out(name,action):
    activity_tracker = Activity_Tracker()
    activity_tracker.log_activity(name,action)
    activity_tracker.view_activity_log()

def activating(name,action):
    activity_tracker = Activity_Tracker()
    activity_tracker.log_activity(name,action)
    activity_tracker.view_activity_log()

log_In("ash","logged in")
activating("ash","activated")
log_out("ash","logged out")
