
# Import all tools and libraries for fastApi and local modules
import requests
from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
import json
from dotenv import load_dotenv
import os

# Local modules
from app import main, get_current_free_classes, find_classes, readFile
from email_side import send_welcome_mail, send_order_conf_mail, send_order_admins


# Initialize .env
load_dotenv()

# Initialize FastAPI App
timetable_api = FastAPI()

# Add CORS allowed sites and local host for debugging
origins = [
    "http://localhost",
    "http://localhost:5000",
    "http://127.0.0.1:5500",
    "https://mysostimetable.web.app",
    "http://localhost:8080",
    "http://localhost:3000",
    "https://hgictuck.shop"
]

timetable_api.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)


# Create an endpoint for searching name and finding it for further processing
@timetable_api.get("/search/{student_name}")
async def root(student_name: str, request: Request):
        key = student_name
        Period = main(key)
        TOKEN = os.getenv('TELEGRAM_BOT_TOKEN_SEARCH')
        send_text = 'https://api.telegram.org/bot' + TOKEN
        + '/sendMessage?chat_id='
        + "1323760864" + '&text=' + key
        response = requests.get(send_text)
        return Period



@timetable_api.get("/")
async def hello():
    return "Welcome to my Timetable API"


@timetable_api.get("/free-classes")
async def free_classes():
    """
    Returns a dictionary, each containing information about a free class.
    Returns:
    List of free classrooms:
    """
    try:
        free_classes = get_current_free_classes()
        return free_classes
    except Exception:
        raise HTTPException(status_code=404, detail="Resource not found")


@timetable_api.get("/process/{string_get}")
async def name_search(string_get: str):
    """
    Given a string input `string_get`, this function searches for
      any matches in
      a set of predefined datasets
    (i.e. `teachers_initials.txt`, `classrooms_initials.txt`,
    `classes_initials.txt`)
      and a JSON file
    (`non_classes.json`)
    that maps non-classroom information to specific strings. T
    he function returns a
      string with all the matches
    found separated by newlines.

    Args:
    - string_get (str): The string to be searched for matches.

    Returns:
    - final_res (str): A string with all the matches found
      separated by newlines.
    """
    try:
        string = str(string_get)
        final_res = find_classes(string)

        return final_res
    except Exception:
        raise HTTPException(status_code=404, detail="Resource not found")


@timetable_api.get("/load/students")
async def load_students():
    """
    Load the list of students from a file.

    Returns:
    List[str]: A list of strings containing the names of the students.
    """
    students = readFile("data/Students.txt")
    if students:
        return students
    else:
        raise HTTPException(status_code=404, detail="Resource not found")


@timetable_api.get("/load/teachers")
async def load_teachers(request: Request):
    """
    Load a dictionary containing teacher information from a JSON file.

    Args:
    request (Request): A FastAPI request object.

    Returns:
    dict: A dictionary containing teacher information.
    """
    with open('data/teachers_dict.json') as f:
        teachers_dict = json.load(f)

    if teachers_dict:
        return teachers_dict
    else:
        raise HTTPException(status_code=404, detail="Resource not found")


# This is a seperate API. Send email for TUCKSHOP

@timetable_api.get("/send_welc_mail/{user_name}/{user_email}")
async def send_welcome_email(user_name: str, user_email: str):
    """
    Sends a welcome email to the user with the given name and email address.

    Args:
        user_name (str): The name of the user.
        user_email (str): The email address of the user.

    Returns:
        str: A success message indicating that the email has been sent.
    """
    try:
        send_welcome_mail(user_email, user_name)

        return "Successfully sent email"
    except Exception:
        raise HTTPException(status_code=404, detail="Resource not found")


@timetable_api.get("/send_order_conf/{user_name}/{user_email}")
async def send_order_confirmation(user_name: str, user_email: str,):
    """
    Sends an order confirmation email to the user with the
    given name and email address,
    and sends a notification to the admins via Telegram.
    Args:
        user_name (str): The name of the user who made the order.
        user_email (str): The email address of the user who made the order.

    Returns:
        str: A success message indicating that the email
        and notification have been sent.
    """

    try:
        send_order_conf_mail(user_email, user_name)
        send_order_admins(user_email, user_name)
        admins = ["1323760864", "847457679"]
        message = f"{user_name} just ordered something right now"
        TOKEN = os.getenv('TELEGRAM_BOT_TOKEN_TUCKSHOP')
        for admin in admins:
            send_text = 'https://api.telegram.org/bot' + TOKEN
            + '/sendMessage?chat_id='
            + admin + '&text=' + message
            response = requests.get(send_text)
        return "Mail sent Successfully"
    except Exception:
        raise HTTPException(status_code=404, detail="Resource not found")
