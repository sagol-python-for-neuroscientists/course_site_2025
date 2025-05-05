import pandas as pd

from hw4_q3 import *


class TestPandasMunch:

    fname = '311_service_requests.zip'

    def test_common_complaint(self):
        ans = common_complaint(self.fname)
        assert ans == ('HEATING', 73371)

    def test_parking_borough(self):
        ans = parking_borough(self.fname)
        assert ans == 'BROOKLYN'