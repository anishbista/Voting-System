import hashlib
from voters import Voter
from file_handling import read_file, write_file
from candidate_registation import Candidate
from election_schedule import Schedule
from voters import Voter
import time,os
class VotingSystem(Candidate,Schedule,Voter):
    user_id = None

    def login(self):
        print(f"{'Login Form':.^100}")
        Users = read_file("voters.json")
        user_id = input("Enter ID: ")
        password = input("Enter Password: ")
        hashed_input_password = hashlib.sha256(password.encode()).hexdigest()
        if user_id == "admin" and password == "superuser":
            print("Admin Login Successful")
            time.sleep(2)
            return 1
        else:
            for voter_id, user_info in Users.items():
                if (
                    voter_id == user_id
                    and user_info["password"] == hashed_input_password
                ):
                    print("User Login Successful")
                    time.sleep(2)
                    self.user_id = voter_id
                    return 0
        return None
    def admin_help(self):
        print(f"{'Help Panel':-^100}")
        print("1->Adding Election Schedule")
        print("2->Showing Election Schedule")
        print("3->Add Candidate for Election")
        print("4->Add Candidate for Election")
        print("5->Update Candidate of Election")
        print("6->Show Candidate for Election")
        print("7->Exit Out of Voting System")
        print("-"*100)
def clear_terminal():
    if os.name=='posix':
        os.system('clear')
    else:
        os.system('cls')
clear_terminal()
vs = VotingSystem()
usr_type = vs.login()
if usr_type == 1:
    clear_terminal()
    print(f"{'Admin':#^100}")
    while 1:
        vs.admin_help()
        choice=int(input("Enter command:"))
        match choice:
            case 1:
                clear_terminal()
                vs.add_schedule()
            case 2:
                clear_terminal()
                vs.show_schedule()
                time.sleep(1)
            case 3:
                clear_terminal()
                vs.addCandidate()
            case 4:
                clear_terminal()
                vs.updateCandidate()
            case 5:
                clear_terminal()
                vs.deleteCandidate()
            case 6:
                clear_terminal()
                vs.showCandidate()
                time.sleep(1)
            case 7:
                choice=input("Are you sure you want to exit[yes/no]:").lower()
                if choice=='yes' or choice=='y':
                    break
                else:
                    print("Continuing....")
            case 8:
                clear_terminal()
                vs.admin_help()
            case default:
                print("Enter Valid command")
elif usr_type == 0:
    clear_terminal()
    print(f"{'User':#^100}")
    print(vs.user_id)
    # To update voter details
    Voter().update_voter_details(vs.user_id)
    # To delete voter details
    Voter().delete_voter(vs.user_id)
else:
    print("Id or Password didn't match!")
