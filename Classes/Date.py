from re import match

class Date:
    def __init__(self, date:str):
        self.set_date(date)

    def set_date(self, date:str):
        if self.validate(date):
            date = date.split('/')

            self.day = int(date[0])
            self.month = int(date[1])
            self.year = int(date[2])
        else:
            raise ValueError("Invalid Date")

    @staticmethod
    def validate(date:str)->bool:
        #Validate if passed date is valid

        pattern = r"^(\d{2})/(\d{2})/(\d{4})$"
        if not match(pattern, date):
            return False
        
        date = date.split('/')
        day = int(date[0])
        month = int(date[1])
        year = int(date[2])

        if not (1 <= month <= 12):
            return False
        if not (1 <= day <= 31):
            return False
        if month == 2 and day > 29:
            return False
        if year < 1900 or year > 2100:
            return False

        return True

    def __str__(self)->str:
        return f"{self.day:02}/{self.month:02}/{self.year:04}"
