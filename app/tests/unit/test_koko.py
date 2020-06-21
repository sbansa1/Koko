from abc import abstractmethod
from datetime import datetime,timedelta
from app.api.koko import koko_utils

def test_calculating_days(monkeypatch):

    def mock_calculating_days():
        return [lambda x: datetime.now() - datetime.timedelta(days=7)]
    monkeypatch.setattr(koko_utils,"calculating_days",mock_calculating_days)

    @abstractmethod
    def calc_rent(duration,number_of_books):
        """Calc Rent takes two arguments duration and number of books"""