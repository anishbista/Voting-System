import datetime
from file_handling import read_file, write_file


class Voting:
    VCFile_Name = "votecount.json"
    votecount = read_file(VCFile_Name)
    candidatelist = read_file("candidatelist.json")
    schedule = read_file("schedule.json")
    today_date = datetime.date.today()

    def __init__(self):
        pass

    def show_candidate(self, location):
        if (
            location in self.schedule
            and str(self.today_date) == self.schedule[location]["date"]
        ):
            candidates = [
                candidate
                for candidate in self.candidatelist
                if candidate["candidancy_from"].lower() == location.lower()
            ]
            if candidates:
                for i, candidate in enumerate(candidates, 1):
                    print(
                        f"{i}. {candidate['candidate_name']} - {candidate['political_party']}"
                    )

                try:
                    choice = int(input("Cast the vote on the basis of number: "))
                    if 1 <= choice <= len(candidates):
                        chosen_candidate = candidates[choice - 1]
                        self.record_vote(chosen_candidate, candidate["candidancy_from"])
                    else:
                        print("Invalid choice! Please select a valid candidate number.")
                except ValueError:
                    print("Please enter a valid candidate number.")
            else:
                print(f"No candidate from {location}")
        else:
            print(
                "Voting is not currently open for this location or it does not exist in the schedule."
            )

    def record_vote(self, candidate, location):
        party_name = candidate["political_party"]

        if location in self.votecount:
            if party_name in self.votecount[location]:
                self.votecount[location][party_name] += 1
            else:
                self.votecount[location][party_name] = 1
        else:
            self.votecount[location] = {party_name: 1}
        write_file(self.votecount, self.VCFile_Name)
        print(f"Vote casted for {candidate['candidate_name']}")
