import requests
from bs4 import BeautifulSoup

class VTOPSession:
    def __init__(self):
        self.session = requests.Session()
        self.base_url = "https://vtop.vitap.ac.in/vtop/"

        self.logged_in = False
        self.cookies = None

    def login(self, username, password, captcha):
        login_page = self.base_url + "login"
        post_url = self.base_url + "authenticate"

        payload = {
            "username": username,
            "password": password,
            "captchaStr": captcha
        }

        r = self.session.post(post_url, data=payload)

        if "Student Profile" in r.text:
            self.logged_in = True
            self.cookies = self.session.cookies.get_dict()
            return True
        else:
            return False

    def get_attendance(self):
        if not self.logged_in:
            return {"error": "Not logged in"}

        url = self.base_url + "student/attendance"
        r = self.session.get(url)
        soup = BeautifulSoup(r.text, "html.parser")

        # Extract attendance data (example)
        return {"attendance": "Data scraped here"}

    def get_marks(self):
        if not self.logged_in:
            return {"error": "Not logged in"}

        url = self.base_url + "student/marks"
        r = self.session.get(url)
        soup = BeautifulSoup(r.text, "html.parser")

        return {"marks": "Data scraped here"}

    def get_timetable(self):
        if not self.logged_in:
            return {"error": "Not logged in"}

        url = self.base_url + "student/timetable"
        r = self.session.get(url)
        soup = BeautifulSoup(r.text, "html.parser")

        return {"timetable": "Data scraped here"}
