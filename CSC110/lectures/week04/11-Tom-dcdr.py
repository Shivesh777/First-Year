"""Tom Data Class Design Recipe example"""

from dataclasses import dataclass
from python_ta.contracts import check_contracts
import datetime

@check_contracts
@dataclass
class MarriageData:
    """A record of the number of marriage licenses issued in a civic centre
    in a given month.

    Instance Attributes:
      - id: a unique identifier for the record
      - civic_centre: the name of the civic centre
      - num_licenses: the number of licenses issued
      - month: the month these licenses were issued

    Representation Invariants:
      - self.id >= 1000
      - self.civic_centre in {'ET', 'NY', 'TO, 'SC'}
      - self.num_licenses > 0
      - self.month.day == 1

    >>> january_etobicoke = MarriageData(1657, 'ET', 80, datetime.date(2011, 1, 1))
    """
    id: int
    civic_centre: str
    num_licenses: int
    month: datetime.date  # Make sure to "import datetime"
