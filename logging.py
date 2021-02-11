
# Importing what is needed
import os
import datetime



# Function used to log.
def Logging(def_msg):
    # Making sure the logging folder is present. If not it will be created.
    if os.path.exists(LogPath):
        pass
    else:
        os.makedirs(LogPath)

    # Setting the full log path.
    full_log_path = LogPath + "/" + LogFile

    # Pulling time at the moment.
    current_time = datetime.datetime.now().strftime("%m-%d-%Y %H:%M:%S")

    # Logging to the Console
    print(def_msg)
    print(current_time)
    print('')

    # Logging to File
    with open(full_log_path, "a") as logfile:
        logfile.write('----------------------------------------------------------\n')
        logfile.write(str(current_time) + " " + str(def_msg) + "\n")

