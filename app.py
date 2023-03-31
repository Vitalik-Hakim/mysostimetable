import datetime
import calendar
import json
import pytz
tz = "Africa/Accra"


# Define a function to read text file that contains students and return names


def readFile(fileName):
    fileObj = open(fileName, "r")  # opens the file in read mode
    words = fileObj.read().splitlines()  # puts the file into an array
    fileObj.close()
    return words


def find_classes(string_returned):
    string = string_returned

    with open('data/non_classes.json') as f:
        mappings = json.load(f)

    string = string_returned.strip().replace("\\n", "")
    if string in mappings:
        res = mappings[string]
        final_res = "\n".join(res)
        return final_res

    teachers = readFile("data/teachers_initials.txt")
    classrooms = readFile("data/classrooms_initials.txt")
    classes = readFile("data/classes_initials.txt")

    string = string.replace(".", "")

    new_list = []
    for i in classes:
        i = i.strip()
        if i in string:
            new_list.append(i)
    for i in classrooms:
        i = i.strip()
        if i in string:
            new_list.append(i)
    for i in teachers:
        i = i.strip()
        if i in string:
            new_list.append(i)
    final_res = "\n".join(new_list)

    return final_res


def get_current_free_classes():

    with open('data/CLASSES.txt', 'r') as file2:
        names = file2.readlines()
        names = map(lambda s: s.strip(), names)

    my_date = datetime.datetime.now(pytz.timezone(tz))
    today = calendar.day_name[my_date.weekday()]  # 'Wednesday'

    days = {"Monday": 1, "Tuesday": 2, "Wednesday": 3, "Thursday": 4,
            "Friday": 5}

    today = days.get(today, 5)

    def get_sec(time):
        secs = sum(int(x) * 60 ** i for i, x in enumerate(reversed(time.split(':'))))
        return secs
    get_now = str(datetime.datetime.now().time())

    now_list = get_now.split(".")
    now_time = now_list[0]
    curr_time1 = get_sec(now_time)

    # Find the current period function
    periods = [(18000, 28200), (28200, 30900), (30900, 33600), (33600, 34800),
            (34800, 37500), (37500, 40200), (40200, 42900), (42900, 45300),
            (45300, 48000), (48000, 50700), (50700, 53400), (53400, 56100)]

    for period_start, period_end in periods:
        if period_start <= curr_time1 < period_end:
            int_period = str(periods.index((period_start, period_end))+1)
            break
    else:
        int_period = '12'

    # Free Classes function
    Free_classes = []
    free_count = []
    period_free = {}
    with open('data/final_class.json', 'r+') as file:
        data = json.load(file)    
        for name in names:
            status = data['CLASSES'][name][today][int_period] 
            if status == "FREE":
                Free_classes.append(name)
                for i in range(int(int_period), 13):
                    status = data['CLASSES'][name][today][f'{i}']
                    if status == "FREE":
                        free_count.append(name)
                    else:
                        period_free[name] = str(i)
                        break

    period_time_db = {
        '1': "5:00",
        '2': '7:50',
        '3': '8:35',
        '4': '9:20',
        '5': '9:40',
        '6': '10:25',
        '7': '11:10',
        '8': '11:55',
        '9': '12:35',
        '10': '13:20',
        '11': '14:05',
        '12': '14:50',
    }
    return [Free_classes, period_free, period_time_db]


def main(searched_user):

    with open('data/file.json', 'r+') as file:
        jsondata = json.load(file)
        file.seek(0)
        json.dump(jsondata, file, indent=4)

    # Find if the name is in the database
    # read txt file
    filetxt = open("data/Students.txt")

    data = filetxt.readlines()

    def searchName(name, text):
        name = name.upper()
        string = name
        # reversing words in a given string
        s = string.split()[::-1]
        initialised_list = []
        for i in s:
            # apending reversed words to l
            initialised_list.append(i)
        # printing reverse words
        r_name = " ".join(initialised_list)
        index = text.find(name)
        index2 = text.find(r_name)
        if (index >= 0):
            return 1
        elif (index2 >= 0):
            return 1
        else:
            return 0

    for i in data:
        if (searchName(searched_user, i)):
            key = i
            break
        else:
            key = "UNKNOWN"
            continue
    key = key.strip()
    students = "STUDENTS"

    # get time

    curr_time = jsondata[students][key][0]['1']
    curr_time = curr_time.split("\n")

    def get_sec(time):
        """
        This function takes a time string in the format of "HH:MM:SS" and 
        returns the number of seconds since midnight. It is used to convert
        the current time into seconds for later use in the
        get_schedule_period function.

        Args:
        time (str): A string representing the time in the format of "HH:MM:SS"

        Returns:
        int: The number of seconds since midnight
        represented by the input time string.
        """
        secs = sum(int(x) * 60 ** i for i, x in enumerate(reversed(time.split(':'))))
        return secs

    get_now = str(datetime.datetime.now().time())

    now_list = get_now.split(".")
    now_time = now_list[0]
    curr_time1 = get_sec(now_time)

    # curr_time1 = 28200 #fixedtime

    my_date = datetime.datetime.now(pytz.timezone(tz))
    today = calendar.day_name[my_date.weekday()]  # 'Wednesday'

    days = {"Monday": 1, "Tuesday": 2, "Wednesday": 3, "Thursday": 4,
            "Friday": 5}

    today = days.get(today, 5)

    if key in jsondata[students]:
        # curr_time = int(curr_time)
        curr_time1 = int(curr_time1)

    def get_schedule_period(jsondata, students, key, today, curr_time):
        """
        Returns a list of schedule data for the four periods including the
        current period based on the current time.

        Args:
        - jsondata (dict): A dictionary containing the schedule data.
        - students (str): A string representing the student for whom to get the
        schedule data.
        - key (str): A string representing the key for the schedule data.
        - today (str): A string representing the current date in YYYY-MM-DD
        format.
        - curr_time (str): A string representing the current time in HH:MM:SS
        format.

        Returns:
        - list: A list of schedule data for the four periods including the
         current period, where each element in the list
        represents the schedule data for a period. If data for a period is
        missing, the corresponding element in the
        list will be None. If no schedule data is found, returns 'Not found'.
        """
        # Define start and end times for each period
        periods = [(18000, 28200), (28200, 30900), (30900, 33600),
                    (33600, 34800),
                    (34800, 37500), (37500, 40200),
                    (40200, 42900), (42900, 45300),
                    (45300, 48000), (48000, 50700),
                    (50700, 53400), (53400, 56100)]

        # Find the index of the current period based on the current time
        curr_time = int(curr_time)
        period_index = None
        for i, period in enumerate(periods):
            if curr_time in range(*period):
                period_index = i
                break
        if period_index is None:
            return None

        # Determine the periods to return data for
        period_numbers = [str(period_index + n) for n in range(4)]
        period_numbers += ['0'] * (4 - len(period_numbers))

        # Get the data for each period and return as a list
        data_list = []
        for period_number in period_numbers:
            data = jsondata[students][key][today].get(period_number, None)
            data_list.append(data)
        data_list += [periods[period_index][0], periods[period_index+1][0], 
                      periods[period_index+2][0], periods[period_index+3][0],
                      jsondata[students][key][0]['0']]

        # Adjust times if any periods are missing
        # indexes = [i for i, x in enumerate(data_list) if not x]
        # if indexes == [1]:
        #     data_list[5] += 2700
        # elif indexes == [2]:
        #     data_list[6] += 2700
        # elif indexes == [3]:
        #     data_list[7] += 2700

        return data_list

    schedule_data = get_schedule_period(jsondata, students, key, today, curr_time1)
    if schedule_data is not None:
        return schedule_data
    else:
        return 'Not found'
