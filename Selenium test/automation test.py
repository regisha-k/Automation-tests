from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://qasvus.wixsite.com/ca-marketing")
driver.maximize_window()

print(driver.find_element(By.TAG_NAME, "a").get_attribute("href"))

# Verify "California Marketing" in  website title
assert "California Marketing" in driver.title

#  Print website title
print(driver.title)
driver.implicitly_wait(10)
driver.find_element(By.XPATH, "//button[@id='comp-k00e6z1wlogin']").click()
# print(driver.find_element(By.XPATH, "//button[@id='comp-k00e6z1wlogin']").text)

driver.implicitly_wait(10)
driver.find_element(By.ID, "signUpDialogswitchToEmailLink").click()
driver.find_element(By.ID, "signUpDialogemailInputinput").send_keys("regish_86@mail.ru")
driver.find_element(By.ID, "signUpDialogpasswordInputinput").send_keys("qa2020")

driver.implicitly_wait(10)
driver.find_element(By.ID, "signUpDialogokButton").click()
driver.implicitly_wait(10)

assert "California Marketing" in driver.title
driver.implicitly_wait(10)

driver.close()
