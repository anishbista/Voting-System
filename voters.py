import uuid
import re
import hashlib
from datetime import datetime
from file_handling import read_file, write_file

File_Name = "voters.json"


class Voter:
    voter = read_file(File_Name)

    def validate_password(self, password):
        if re.match(
            r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@$%&*?])[A-Za-z\d@$!%*?&]{8,}$",
            password,
        ):
            return True

    def hash_password(self, password):
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        return hashed_password

    def eligibility(self, dob):
        try:
            dob_date = datetime.strptime(dob, "%Y-%m-%d")
            current_date = datetime.now()
            age_diff = (current_date - dob_date).days // 365
            if age_diff >= 18:
                return True
        except ValueError:
            print("Invalid date format. Please enter the date in YYYY-MM-DD format.")

    def add_voter(self):
        name = input("Enter Full Name: ")
        dob = input("Enter the date of birth(YYYY-MM-DD format): ")
        address = input("Enter address: ")
        password = input("Enter the password: ")
        unique_id = str(uuid.uuid4())[-7:]
        if self.eligibility(dob):
            if self.validate_password(password):
                hashed_password = self.hash_password(password)
                self.voter[unique_id] = {
                    "name": name,
                    "Date of birth": dob,
                    "address": address,
                    "password": hashed_password,
                }
                write_file(self.voter, File_Name)

                print("Voter added successfully")
            else:
                print(
                    "Error: Password should contain at least one lowercase,uppercase,digit and special characters and at least  8 characters"
                )
        else:
            print("Only 18+ can cast vote")


Voter().add_voter()
