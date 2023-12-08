import hashlib
from voters import Voter
from file_handling import read_file, write_file
from candidate_registation import Candidate
from election_schedule import Schedule
from voters import Voter
from voting import Voting
from result import vote_result
import time, os


class VotingSystem(Candidate, Schedule, Voter, Voting, vote_result):
    user_id = None
    user_address = None

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
                    self.user_address = user_info["address"]
                    return 0
        return None

    def admin_help(self):
        print(f"{'Help Panel':-^100}")
        print("1->Adding Election Schedule")
        print("2->Showing Election Schedule")
        print("3->Add Candidate for Election")
        print("4->Update Candidate of Election")
        print("5->Delete Candidate for Election")
        print("6->Show Candidate for Election")
        print("7->Generate Voting Result")
        print("8->Show Voting Result")
        print("9->Exit Out of Voting System")
        print("-" * 100)

    def voter_help(self):
        print(f"{'Help Panel':-^100}")
        print("1->Search Detail of Voter")
        print("2->Update Detail of Voter")
        print("3->Delete Voter")
        print("4->Cast a vote")
        print("5->Exit Out of Voting System")
        print("-" * 100)


def clear_terminal():
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")


clear_terminal()
vs = VotingSystem()
usr_type = vs.login()
if usr_type == 1:
    clear_terminal()
    print(f"{'Admin':#^100}")
    while 1:
        vs.admin_help()
        choice = int(input("Enter command:"))
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
                clear_terminal()
                vs.generate_result()
                time.sleep(1)
            case 8:
                clear_terminal()
                vs.show_result()
                time.sleep(1)
            case 9:
                Echoice = input("Are you sure you want to exit[yes/no]:").lower()
                if Echoice == "yes" or Echoice == "y":
                    break
                else:
                    print("Continuing....")
            case default:
                print("Enter Valid command")
elif usr_type == 0:
    clear_terminal()
    print(f"{'User':#^100}")
    while 1:
        vs.voter_help()
        choice = int(input("Enter command:"))
        match choice:
            case 1:
                clear_terminal()
                vs.search_voter(vs.user_id)
            case 2:
                clear_terminal()
                vs.update_voter_details(vs.user_id)
                time.sleep(1)
            case 3:
                clear_terminal()
                vs.delete_voter(vs.user_id)
                time.sleep(1)
                break
            case 4:
                clear_terminal()
                vs.show_candidate(vs.user_address)
                time.sleep(1)
            case 5:
                Echoice = input("Are you sure you want to exit[yes/no]:").lower()
                if Echoice == "yes" or Echoice == "y":
                    break
                else:
                    print("Continuing....")
            case default:
                print("Enter Valid command")
else:
    clear_terminal()
    print("Id or Password didn't match!")
    time.sleep(1)
    register = input("Do you want to register Voter[yes/no]:").lower()
    if register == "yes" or register == "y":
        vs.add_voter()
    else:
        print("Exiting....")
