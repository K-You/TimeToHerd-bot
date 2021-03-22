from time import sleep

import chromedriver_binary
import yaml
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class TimeToHerdBot():
  def __init__(self):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    self.driver = webdriver.Chrome(options=chrome_options)

    self.remainingDays = None

    with open(r'./properties.yml') as file:
      properties = yaml.full_load(file)
      self.TIME_TO_HERD_URL = properties['timetoherd']['url']
      self.COUNTRY = properties['timetoherd']['country']

  def __del__(self):
    self.driver.quit()
  
  def gotToMain(self):
    self.driver.get(self.TIME_TO_HERD_URL)
  
  def clickDropdown(self):
    _dropdown = self.driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[1]/p[1]/span/span")
    action = ActionChains(self.driver);
    _dropdown.click()
    sleep(1)
    _countryItem = self.driver.find_element_by_xpath("/html/body/div[3]/div/div/ul/li[span='"+self.COUNTRY+"']")
    action.move_to_element(_countryItem).click().perform();
    sleep(2)

  def collectValue(self):
    _result = self.driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[1]/div[1]/span[1]/span")
    self.remainingDays = _result.text
    return self.remainingDays
