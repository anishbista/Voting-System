import hashlib
from voters import Voter
from file_handling import read_file, write_file


class VotingSystem:
    user_id = None

    def login(self):
        Users = read_file("voters.json")
        user_id = input("Enter ID: ")
        password = input("Enter Password: ")
        hashed_input_password = hashlib.sha256(password.encode()).hexdigest()
        if user_id == "admin" and password == "superuser":
            print(f"{'Admin Login Successful':*^100}")
            return 1
        else:
            for voter_id, user_info in Users.items():
                if (
                    voter_id == user_id
                    and user_info["password"] == hashed_input_password
                ):
                    print(f"{'User Login Successful':*^100}")
                    self.user_id = voter_id
                    return 0
        return None


vs = VotingSystem()
usr_type = vs.login()
if usr_type == 1:
    print("Admin module")
elif usr_type == 0:
    print("User module")
    print(vs.user_id)
    # To update voter details
    Voter().update_voter_details(vs.user_id)
    # To delete voter details
    Voter().delete_voter(vs.user_id)
else:
    print("Id or Password didn't match!")
