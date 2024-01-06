import datetime

class DateService:
    @staticmethod
    def get_week_date(date=None):
        if date is None:
            date = datetime.date.today()

        start = date - datetime.timedelta(days=date.weekday())
        end = start + datetime.timedelta(days=6)

        return {
            "start": start.strftime("%d/%m"),
            "end": end.strftime("%d/%m"),
            "string": f"{start.strftime('%d/%m')} -> {end.strftime('%d/%m')}"
        }
