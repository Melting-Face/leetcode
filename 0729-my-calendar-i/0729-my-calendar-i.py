class MyCalendar:
    def __init__(self):
        self.book_dates = []

    def book(self, start: int, end: int) -> bool:
        book_dates = self.book_dates
        if not book_dates:
            book_dates.append([start, end])
            return True

        for book_date in book_dates:
            start_date, end_date = book_date
            if end <= start_date or end_date <= start:
                continue
            return False
        book_dates.append([start, end])
        return True
