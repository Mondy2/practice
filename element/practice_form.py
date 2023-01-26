from random import random
import random

from generator.generator import generator_person
from selenium_base_new.base import SeleniumBase





class PracticeForm(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.first_name='input[id="firstName"]'
        self.last_name='input[id="lastName"]'
        self.number_field='input[id="userNumber"]'
        self.radio1 = 'label[for="gender-radio-1"]'
        self.radio2 = 'label[for="gender-radio-2"]'
        self.radio3 = 'label[for="gender-radio-3"]'
        self.submit_field = 'button[class="btn btn-primary"]'
        self.table_field='div[class="modal-body"]'

    def find_first_name(self):
        return self.is_visiable('css',self.first_name)
    def find_last_name(self):
        return self.is_visiable('css',self.last_name)
    def check_box1(self):
        return self.is_visiable('css',self.radio1)
    def check_box2(self):
        return self.is_visiable('css',self.radio2)
    def check_box3(self):
        return self.is_visiable('css',self.radio3)
    def find_number(self):
        return self.is_visiable('css',self.number_field)
    def field_submit(self):
        return self.is_visiable('css',self.submit_field)
    def submit_button(self):
        button =self.is_visiable('css',self.submit_field)
        self.click_on_element(button)



    def add_new_person(self):
        count = random.randint(1, 3)
        while count != 0:
            person_info = next(generator_person())
            first_name = person_info.first_name
            last_name = person_info.last_name
            number_field=person_info.age

            self.find_first_name().send_keys(first_name)
            self.find_last_name().send_keys(last_name)
            self.find_number().send_keys(number_field)
            count -= 1
            return [first_name, last_name, str(number_field)]
    def random_button(self):
        count=random.randint(1,3)
        if(count==1):
            return self.is_visiable('css', self.radio1).click()
        elif(count==2):
            return self.is_visiable('css', self.radio2).click()
        else:
            return self.is_visiable('css', self.radio3).click()


    def find_element(self):

        table_element = self.are_visiable('css', self.table_field)
        data = []
        for item in table_element:
            data.append(item.text.splitlines())
        return data
