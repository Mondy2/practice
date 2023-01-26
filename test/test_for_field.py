import time
from msilib.schema import RadioButton
from random import random

import pytest

from element.practice_form import PracticeForm


@pytest.mark.usefixtures('setup')
class TestElements:




    def test_practice_form(self):
        practice_form=PracticeForm(self.driver)
        first_name=practice_form.add_new_person()

        practice_form.random_button()

        practice_form.submit_button()
        result=practice_form.find_element()
        print(first_name)
        print(result)
        assert first_name in result

