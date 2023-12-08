from file_handling import read_file, write_file


class Candidate:
    def __init__(self):
        self._candidate_list = list()

    def addCandidate(self):
        cname = input("Enter name of candidate who participate in election:").lower()
        political_party = input("Enter name of party name:").upper()
        c_from = input("Enter Location:").lower()
        self._candidate_list = read_file("candidatelist.json")
        candidate_registered = False
        for candidates in self._candidate_list:
            if (
                candidates["candidate_name"] == cname
                and candidates["political_party"] == political_party
                and candidates["candidancy_from"] == c_from
            ):
                candidate_registered = True
                break
        if candidate_registered:
            print(f"{'Candidate Already Registered':*^100}")
        else:
            self._candidate_list.append(
                {
                    "candidate_name": cname,
                    "political_party": political_party,
                    "candidancy_from": c_from,
                }
            )
            write_file(self._candidate_list, "candidatelist.json")
            print(
                f"Candidate:{cname} Political Party:{political_party} Candidancy from:{c_from} is registered"
            )

    def showCandidate(self):
        self._candidate_list = read_file("candidatelist.json")
        if len(self._candidate_list) > 0:
            print("#" * 100)
            header = "{:^30}{:^30}{:^30}".format(
                "Name of candidate".center(30),
                "Political Party".center(30),
                "candidacy from".center(30),
            )
            print(header)
            for candidates in self._candidate_list:
                candidate_value = "{:^30}{:^30}{:^30}".format(
                    candidates["candidate_name"].center(30),
                    candidates["political_party"].center(30),
                    candidates["candidancy_from"].center(30),
                )
                print(candidate_value)
            print("#" * 100)
        else:
            print(f"{'Empty Candidate List':*^100}")

    def updateCandidate(self):
        self._candidate_list = read_file("candidatelist.json")
        if len(self._candidate_list) > 0:
            cname = input(
                "Enter name of candidate who participate in election:"
            ).lower()
            political_party = input("Enter name of party name:").upper()
            c_from = input("Enter Location:").lower()
            candidate_registered = False
            for candidates in self._candidate_list:
                if (
                    candidates["candidate_name"] == cname
                    and candidates["political_party"] == political_party
                    and candidates["candidancy_from"] == c_from
                ):
                    candidate_registered = True
                    break
            if candidate_registered:
                cname = input(
                    "Enter updated of candidate who participate in election:"
                ).lower()
                political_party = input("Enter updated name of party name:").upper()
                c_from = input("Enter updated Location:").lower()
                self._candidate_list.remove(candidates)
                self._candidate_list.append(
                    {
                        "candidate_name": cname,
                        "political_party": political_party,
                        "candidancy_from": c_from,
                    }
                )
                write_file(self._candidate_list, "candidatelist.json")
                print(
                    f"Candidate:{cname} Political Party:{political_party} Candidancy from:{c_from} is updated"
                )
            else:
                print(f"{'Candidate Not Registered':*^100}")
        else:
            print(f"{'Empty Candidate List':*^100}")

    def deleteCandidate(self):
        self._candidate_list = read_file("candidatelist.json")
        if len(self._candidate_list) > 0:
            cname = input("Enter name of candidate to be deleted:").lower()
            political_party = input("Enter name of party name:").upper()
            c_from = input("Enter Location:").lower()
            candidate_registered = False
            for candidates in self._candidate_list:
                if (
                    candidates["candidate_name"] == cname
                    and candidates["political_party"] == political_party
                    and candidates["candidancy_from"] == c_from
                ):
                    candidate_registered = True
                    break
            if candidate_registered:
                self._candidate_list.remove(candidates)
                write_file(self._candidate_list, "candidatelist.json")
                print(
                    f"Candidate:{cname} Political Party:{political_party} Candidancy from:{c_from} is deleted"
                )
            else:
                print(f"{'Candidate Not Registered':*^100}")
        else:
            print(f"{'Empty Candidate List':*^100}")
