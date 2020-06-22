from abc import abstractmethod
from datetime import datetime,timedelta
from app.api.koko import koko_utils

def test_calculating_days(monkeypatch):

    def mock_calculating_days():
        return [lambda x: datetime.now() - datetime.timedelta(days=7)]
    monkeypatch.setattr(koko_utils,"calculating_days",mock_calculating_days)


def test_calculate_total_rent(monkeypatch):

    def mock_calculate_total_rent():
        return [lambda c: 10 * (2 * 4.5)]
    monkeypatch.setattr(koko_utils,"calculate_total_rent",mock_calculate_total_rent)
