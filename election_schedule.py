from file_handling import read_file, write_file

File_Name = "schedule.json"


class Schedule:
    schedule = read_file(File_Name)

    def add_schedule(self):
        constituency = input("Enter the constituency: ")
        date = input("Enter a date for election(YYYY-MM-DD format): ")
        if constituency in self.schedule:
            raise Exception("Constituency already added !")
        self.schedule[constituency] = {"date": date}
        write_file(self.schedule, File_Name)
        print(f"{constituency}:{date} added successfully")

    def show_schedule(self):
        for constituency, data in self.schedule.items():
            print(f"Constituency: {constituency} Date: {data['date']}")
