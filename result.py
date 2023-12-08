from file_handling import read_file,write_file
class vote_result:
    RFILE_NAME="votecount.json"
    def generate_result(self):
        vote_count = read_file(self.RFILE_NAME)
        total_dict=dict()
        if len(vote_count)>0:
            for location,party_vote in vote_count.items():
                if location=="winner":
                    continue
                max_vote=max(party_vote.values())
                max_party_name=[pname for pname,vote in party_vote.items() if vote==max_vote]
                total_dict[location]=max_party_name[0]
            vote_count["winner"]=total_dict
            write_file(vote_count,self.RFILE_NAME)
            print("Winner Result Generated")
        else:
            print("Votecount is empty")
    def show_result(self):
        winner_select = read_file(self.RFILE_NAME)
        if len(winner_select)>0:
            winner_party=winner_select.get("winner")
            print(f"{'Winner Party':#^100}")
            for location,party in winner_party.items():
                print(f"Party {party} won in {location}")
            print("#"*100)
        else:
            print("Votecount is empty")