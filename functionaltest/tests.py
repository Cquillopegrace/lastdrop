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

        inputbox1 = self.browser.find_element_by_id('StudentID')
        self.assertEqual(inputbox1.get_attribute('placeholder'), 'InputID')
        inputbox1.send_keys('TUPC 18 0675')
        time.sleep(1)

        inputbox2 = self.browser.find_element_by_id('CompleteName')
        self.assertEqual(inputbox2.get_attribute('placeholder'), 'First/Middle/LastName')
        inputbox2.send_keys('Carolyn B. Quillope')
        time.sleep(1)

        inputbox3 = self.browser.find_element_by_id('Address')
        self.assertEqual(inputbox3.get_attribute('placeholder'), 'Full Address')
        inputbox3.send_keys('Brgy. San Nicolas 3 Bacoor City')
        time.sleep(1)

        inputbox4 = self.browser.find_element_by_id('Gender')
        self.assertEqual(inputbox4.get_attribute('placeholder'),'F/M/Others')
        inputbox4.send_keys('F')
        time.sleep(1)

        inputbox6 = self.browser.find_element_by_id('MothersName')
        self.assertEqual(inputbox6.get_attribute('placeholder'),'First/Middle/Last Name')
        inputbox6.send_keys('Custodia B. Bumotad')
        time.sleep(1)

        inputbox7 = self.browser.find_element_by_id('MOccupation')
        self.assertEqual(inputbox7.get_attribute('placeholder'),'Occupations')
        inputbox7.send_keys('House Wife')
        time.sleep(1)

        inputbox8 = self.browser.find_element_by_id('FathersName')
        self.assertEqual(inputbox8.get_attribute('placeholder'),'First/Middle/Last Name')
        inputbox8.send_keys('Germinard A. Quillope')
        time.sleep(1)

        inputbox9 = self.browser.find_element_by_id('FAOccupation')
        self.assertEqual(inputbox9.get_attribute('placeholder'),'Occupations')
        inputbox9.send_keys('Deceased')
        time.sleep(1)

        inputbox10 = self.browser.find_element_by_id('Annual Income')
        self.assertEqual(inputbox10.get_attribute('placeholder'),'Input Income')
        inputbox10.send_keys('30000')
        time.sleep(1)

        btnSubmit = self.browser.find_element_by_id('rbtnsubmit')
        btnSubmit.click()
        time.sleep(2)
        
        inputbox11 = self.browser.find_element_by_id('School')
        self.assertEqual(inputbox11.get_attribute('placeholder'),'Your School')
        inputbox11.send_keys('TUPC')
        time.sleep(1)

        inputbox12 = self.browser.find_element_by_id('SAddress')
        self.assertEqual(inputbox12.get_attribute('placeholder'),'Present School')
        inputbox12.send_keys('Salawag Ave. Dasmarinas City')
        time.sleep(1)

        inputbox13 = self.browser.find_element_by_id('YrSection')
        self.assertEqual(inputbox13.get_attribute('placeholder'),'Yr&Sec.')
        inputbox13.send_keys('30000')
        time.sleep(1)

        btnSubmit = self.browser.find_element_by_id('rbtnsubmit')
        btnSubmit.click()
        time.sleep(2)


        #inputbox6 = self.browser.find_element_by_id('MothersName')
        #self.assertEqual(inputbox6.get_attribute('placeholder'),'First/Middle/Last Name')
        #inputbox6.send_keys('Custodia B. Bumotad')
        #time.sleep(1)
