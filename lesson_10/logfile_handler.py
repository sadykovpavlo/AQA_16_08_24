# Function to open log file and return last log
def log_file_return_last_log(file_path: str):
    with open(file_path) as file:
        file = file.readlines()
        return file[-1]


