"""
Automationlab: Example script to run one test against the dialer native app using Appium
The test will:
- launch the app
- click the 'dialer' button
"""

import os
import unittest

from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import InvalidSelectorException
from time import sleep

class DialerTests(unittest.TestCase):

	def setUp(self):
		print("dummy setup")


	def tearDown(self):
		'''Tear down the test'''
		self.driver.quit()

	def test_open_dialer(self):
		'''open phone dialer'''
		desired_caps = {}
		desired_caps['platformName'] = 'Android'
		desired_caps['platformVersion'] = '5.1.1'
		desired_caps['deviceName'] = 'Galaxy J5'
		desired_caps['appPackage'] = 'com.instagram.android'
		desired_caps['appActivity'] = 'com.instagram.mainactivity.LauncherActivity'
		self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
		sleep(10)
		#print(self.driver.page_source)
		#sleep(30)

		try:
			email =  self.driver.find_element(By.XPATH,'//[@resource-id="com.instagram.android:id/login_button"]')
			email.send_keys('abdeljalil.bensoudane')
			password = self.driver.find_element(By.XPATH,'//[@resource-id="com.instagram.android:id/password"]')
			password.send_keys('Aurnowac9737')
			login = self.driver.find_element(By.XPATH,'//[@resource-id="com.instagram.android:id/button_text"]')
			login.click()
			sleep(6)
		except InvalidSelectorException:
			login = self.driver.find_element(By.XPATH,'//*[@resource-id="com.instagram.android:id/login_button"]')
			login.click()
			sleep(8)
		
		search = self.driver.find_element(By.XPATH,'//*[@resource-id="com.instagram.android:id/search_tab"]')
		search.click()
		sleep(5)
		search_bar = self.driver.find_element(By.XPATH,'//*[@resource-id="com.instagram.android:id/action_bar_search_edit_text"]')
		search_bar.click()
		sleep(5)
		search_bar = self.driver.find_element(By.XPATH,'//*[@resource-id="com.instagram.android:id/search_tab_bar_layout"]')
		search_bar.send_keys('simo')
		search_click = self.driver.find_element(By.XPATH,'//*[@clickable="true"]')
		search_click.click()
		sleep(6)
		print(self.driver.page_source)
		sleep(8)

#---START OF SCRIPT
if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(DialerTests)
	unittest.TextTestRunner(verbosity=2).run(suite)
