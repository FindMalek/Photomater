import datetime

class DateService:
    def __init__(self):
        self.date = datetime.date.today()
        self.weekdays = {
            "Lundi": 0, "Mardi": 1, "Mercredi": 2,
            "Jeudi": 3, "Vendredi": 4, "Samedi": 5, "Dimanche": 6
        }

    def get_week_date(self):
        if self.date.weekday() >= 4:  
            days_until_next_monday = 7 - self.date.weekday()
            start_of_next_week = self.date + datetime.timedelta(days=days_until_next_monday)
        else:
            start_of_next_week = self.date - datetime.timedelta(days=self.date.weekday())

        end_of_next_week = start_of_next_week + datetime.timedelta(days=6)

        return {
            "start": start_of_next_week.strftime("%d/%m"),
            "end": end_of_next_week.strftime("%d/%m"),
            "string": f"{start_of_next_week.strftime('%d/%m')} -> {end_of_next_week.strftime('%d/%m')}"
        }
    
    def getWeekPointer(week_date, layer_name):
        if 'start' in layer_name.lower():
            return week_date['start']
        elif 'end' in layer_name.lower():
            return week_date['end']
        

    def getWeekDict(self, artboard_name, week_date):
        """
        Returns a dictionary with the artboard name as keys and the week date as value.
        Example: artboard_name = "Lundi", week_date = {"start": "01/01", "end": "07/01"}
        Returns: {"Lundi": "01/01"}
        Example: artboard_name = ["Mardi"], week_date = {"start": "01/01", "end": "07/01"}
        Returns: {"Mardi": "02/01"}
        """
        start_date = datetime.datetime.strptime(week_date["start"], "%d/%m")

        if artboard_name in self.weekdays:
            day_offset = self.weekdays[artboard_name]
            target_date = start_date + datetime.timedelta(days=day_offset)
            return {artboard_name: target_date.strftime("%d/%m")}
        
        return {}
    
