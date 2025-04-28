import re
from unittest import TestCase


class Test(TestCase):
    def test_parsing(self):
        company = 'между ООО "Комплекс Поставок" (Экспедитор) и TOO "Exim Artis" (Клиент) по договору №103-10-24/КП  от 21.10.2024'
        company = re.findall(r' и (.*) по договору', company)
        if company:
            company = company[0]
        company = re.sub(r'\s*\(.*\)', '', company)
        print(company)
