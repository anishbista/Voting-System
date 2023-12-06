from file_handling import read_file,write_file
class VotingSystem:
    @staticmethod
    def login():
        username=input("Enter Username:")
        password=input("Enter Password:")
        Users=read_file("user.json")
        for user in Users:
            if username=="admin" and password=="superuser":
                print(f"{'Admin Login Sucessful':*^100}")
                return 1
            elif user["name"]==username and user["password"]==password:
                print(f"{'User Login Sucessful':*^100}")
                return 0
vs=VotingSystem()
usr_type=VotingSystem.login()
if usr_type==1:
    print("Admin module")
elif usr_type==0:
    print("User module")
