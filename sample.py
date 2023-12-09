from activityTracker import Activity_Tracker

def log_In(name,action):
    # log In method is defined here
    
    activity_tracker = Activity_Tracker()
    activity_tracker.log_activity(name,action)
    activity_tracker.view_activity_log()

def log_out(name,action):
    # log Out method is defined here
    
    activity_tracker = Activity_Tracker()
    activity_tracker.log_activity(name,action)
    activity_tracker.view_activity_log()

def activating(name,action):
    # activating method is defined here
    
    activity_tracker = Activity_Tracker()
    activity_tracker.log_activity(name,action)
    activity_tracker.view_activity_log()

log_In("ash","logged in")
activating("ash","activated")
log_out("ash","logged out")
