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

    def search_voter(self, voter_id):
        voter = self.voter.get(voter_id)
        if voter:
            print("Voter Details:")
            for key, value in voter.items():
                print(f"{key}:{value}")
        else:
            print("Voter ID not found.")

    def update_voter_details(self, voter_id):
        print(
            "What details do you want to update?\n 1.Name\n 2.Date of Birth\n 3.Address\n 4.Password"
        )
        choice = input("Enter your choice: ")

        match choice:
            case "1":
                new_name = input("Enter new name: ")
                self.voter[voter_id]["name"] = new_name
            case "2":
                new_dob = input("Enter new date of birth (YYYY-MM-DD format): ")
                if self.eligibility(new_dob):
                    self.voter[voter_id]["Date of birth"] = new_dob
                else:
                    print("Only 18+ can cast vote")
            case "3":
                new_address = input("Enter new address: ")
                self.voter[voter_id]["address"] = new_address
            case "4":
                new_password = input("Enter new password: ")
                if self.validate_password(new_password):
                    hashed_password = self.hash_password(new_password)
                    self.voter[voter_id]["password"] = hashed_password
                else:
                    print(
                        "Error: Password should contain at least one lowercase, uppercase, digit, and special characters and be at least 8 characters long."
                    )
            case _:
                print("Invalid choice")
        write_file(self.voter, File_Name)
        print("Details updated successfully")

    def delete_voter(self, voter_id):
        del self.voter[voter_id]
        write_file(self.voter, File_Name)
        print("Voter deleted successfully")


# Voter().add_voter()
