import datetime
from file_handling import read_file, write_file


class Schedule:
    SFile_Name = "schedule.json"
    schedule = read_file(SFile_Name)

    def validate_date(self, date):
        today = datetime.date.today()
        input_date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
        if input_date <= today:
            raise ValueError("Date should be greater than today")
        return date

    def add_schedule(self):
        constituency = input("Enter the constituency: ")
        date = input("Enter a date for the election (YYYY-MM-DD format): ")
        try:
            validated_date = self.validate_date(date)
            if constituency in self.schedule:
                raise Exception("Constituency already added!")
            self.schedule[constituency] = {"date": validated_date}
            write_file(self.schedule, self.SFile_Name)
            print(f"{constituency}: {validated_date} added successfully")
        except ValueError as e:
            print(f"Error: {e}")

    def show_schedule(self):
        for constituency, data in self.schedule.items():
            print(f"Constituency: {constituency} Date: {data['date']}")
