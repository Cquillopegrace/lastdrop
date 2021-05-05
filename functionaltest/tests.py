from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import WebDriverException

MAX_WAIT = 3
class PageTest(LiveServerTestCase):



    def wait_for_table(self, row_text):        
           start_time = time.time()
           while True:  
               try:                
                   table = self.browser.find_element_by_id('caroltable')                  
                   rows = table.find_elements_by_tag_name('tr')                
                   self.assertIn(row_text, [row.text for row in rows])
                   return
               except (AssertionError, WebDriverException) as e:  
                   if time.time() - start_time > MAX_WAIT:  
                       raise e                  
                   time.sleep(0.5)  
                 
    def setUp(self):
        self.browser = webdriver.Firefox()

    def test_browser_title(self):
        self.browser.get('http://localhost:8000/')
        #self.browser.get(self.live_server_url)
        self.assertIn('CITY of BACOOR',self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('CITY of BACOOR', header_text)
       
        inputbox1 = self.browser.find_element_by_id('Name')
        self.assertEqual(inputbox1.get_attribute('placeholder'), 'InputName')
        inputbox1.send_keys('Carolyn Quillope')
        time.sleep(1)

        inputbox2 = self.browser.find_element_by_id('School')
        self.assertEqual(inputbox2.get_attribute('placeholder'), 'InputSchool')
        inputbox2.send_keys('TUP')
        time.sleep(1)

        inputbox3 = self.browser.find_element_by_id('Precinct')
        self.assertEqual(inputbox3.get_attribute('placeholder'),'PrecinctNo.')
        inputbox3.send_keys('0485')
        time.sleep(1)

        btnSubmit = self.browser.find_element_by_id('rbtnsubmit')
        btnSubmit.click()
        time.sleep(2)

        inputbox4 = self.browser.find_element_by_id('NxtName')
        self.assertEqual(inputbox4.get_attribute('placeholder'), 'InputName')
        inputbox4.send_keys('Carolyn Quillope')
        time.sleep(1)

        inputbox5 = self.browser.find_element_by_id('Year')
        self.assertEqual(inputbox5.get_attribute('placeholder'), 'SY')
        inputbox5.send_keys('2020-2021')
        time.sleep(1)

        inputbox6 = self.browser.find_element_by_id('GPA')
        self.assertEqual(inputbox6.get_attribute('placeholder'),'InputGPA')
        inputbox6.send_keys('90')
        time.sleep(1)

        btnSubmit = self.browser.find_element_by_id('rbtnsubmit')
        btnSubmit.click()
        time.sleep(2)
        
