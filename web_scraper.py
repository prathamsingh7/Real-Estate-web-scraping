from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from googletrans import Translator
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import pandas as pd
import psycopg2
import time

options = webdriver.ChromeOptions()
s = Service("chromedriver.exe")
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=s)

url = "https://pay2igr.igrmaharashtra.gov.in/eDisplay/propertydetails/"
driver.get(url)
driver.maximize_window()
time.sleep(5)

# # Selecting using XPATH and click()
# district_path = "/html/body/div[1]/div[1]/main/div[1]/div/form/div[2]/div[2]/div[1]/select/option[26]"
# taluka_path = "/html/body/div[1]/div[1]/main/div[1]/div/form/div[2]/div[2]/div[2]/select/option[2]"
# village_path = "/html/body/div[1]/div[1]/main/div[1]/div/form/div[2]/div[2]/div[3]/select/option[59]"
# reg_reg_year_path = "/html/body/div[1]/div[1]/main/div[1]/div/form/div[2]/div[1]/div[2]/select/option[31]"
# entry_path = "/html/body/div[1]/div[1]/main/div[2]/div/div/div[2]/div/div[1]/div[1]/div/label/select/option[3]"

# def select_district():
#     dropdown = Select(driver.find_element(By.ID, "district_id"))
#     # driver.find_element(By.XPATH, district_path).click()
#     dropdown.select_by_value(str(37))
#     time.sleep(2)

# def select_taluka():
#     driver.find_element(By.ID, "taluka_id")
#     driver.find_element(By.XPATH, taluka_path)
#     time.sleep(2)
    
# def select_village():
#     driver.find_element(By.ID, "village_id").click()
#     driver.find_element(By.XPATH, village_path).click()
#     time.sleep(2)
    
# def select_reg_reg_year():
#     driver.find_element(By.ID, "dbselect").click()
#     # drop.select_by_index(30)
#     driver.find_element(By.XPATH, reg_reg_year_path).click()
#     time.sleep(2)

# def entry_number():
#     driver.find_element(By.CLASS_NAME, "custom-select custom-select-sm form-control form-control-sm").click()
#     driver.find_element(By.XPATH, entry_path).click()
#     time.sleep(2)
    
# def reg_reg_reg_year():
#     type_reg_reg_year = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/main/div[1]/div/form/div[3]/div[2]/input")
#     type_reg_reg_year.send_keys("2023")
#     time.sleep(2)
    
# Defining all the required functions using Select() and select_by_value()
def select_reg_reg_year():
    table1 = driver.find_element(By.ID, "dbselect")
    drop_table = Select(table1)
    drop_table.select_by_index(30)
    time.sleep(2)

def select_district():
    table2 = driver.find_element(By.ID, "district_id")
    drop_table = Select(table2)
    drop_table.select_by_value(str(37))
    time.sleep(2)
    
def select_taluka():
    table3 = driver.find_element(By.ID, "taluka_id")
    drop_table = Select(table3)
    drop_table.select_by_value(str(1))
    time.sleep(2)

def select_village():
    table4 = driver.find_element(By.ID, "village_id")
    drop_table = Select(table4)
    drop_table.select_by_value(str(57))
    time.sleep(2)
    
def reg_reg_reg_year():
    # table5 = driver.find_element({"class" : "form-control", "id" : "free_text"})
    table5 = driver.find_element(By.CSS_SELECTOR, ".form-control#free_text")
    table5.send_keys("2023")
    time.sleep(2)

def entry_number():
    # table6 = driver.find_element(By.CLASS_NAME, "custom-select custom-select-sm form-control form-control-sm")
    table6 = driver.find_element(By.NAME, "tableparty_length")
    drop_table = Select(table6)
    drop_table.select_by_value(str(50))
    time.sleep(2)

# Select the reg_reg_year, district, taluka, village and reg reg_reg_year
select_reg_reg_year()  
select_district() 
select_taluka()
select_village()
reg_reg_reg_year()

# Manually entering captcha

time.sleep(30)

# click on submit
# submit = driver.find_element(By.ID, "submit")
# submit.click()

# Give require number of entry, here - 50
entry_number()

# Scraping data with translation
rows = driver.find_elements(By.XPATH,'//*[@id="tbdata"]')

serial_number = []
document_number = []
document_type = []
revenue_office = []
reg_year = []
Buyer_name = []
Seller_name = []
Other_information = []
List_no_2 = []

for row in rows:
    serial_number.append(row.find_element(By.XPATH, './td[1]').text)
    document_number.append(row.find_element(By.XPATH, './td[2]').text)
    document_type.append(row.find_element(By.XPATH, './td[3]').text)
    revenue_office.append(row.find_element(By.XPATH, './td[4]').text)
    reg_year.append(row.find_element(By.XPATH, './td[5]').text)
    Buyer_name.append(row.find_element(By.XPATH, './td[6]').text)
    Seller_name.append(row.find_element(By.XPATH, './td[7]').text)
    Other_information.append(row.find_element(By.XPATH, './td[8]').text)
    new_link = row.find_element(By.XPATH, './td[9]/a')
    List_no_2.append(new_link.get_attribute('href') if new_link else "")


df  =  pd.DataFrame({'Serial number': serial_number, 'Document number': document_number, 'Document type' : document_type, 'Revenue Office': revenue_office, 'Registration Year': reg_year, 'Buyer name': Buyer_name, 'Seller name': Seller_name, 'Other information' : Other_information, 'List no.2': List_no_2})
df.to_csv('data.csv', index = False)

# translator = Translator()

# translated_document_type = []
# translated_revenue_office = []
# translated_Buyer_name = []
# translated_Seller_name = []
# translated_Other_information = []

# for text in document_type:
#     if text.strip():
#         try:
#             translation = translator.translate(text, src='hi', dest='en')
#             translated_document_type.append(translation.text)
#         except:
#             translated_document_type.append("")
#     else:
#         translated_document_type.append("")

# for text in revenue_office:
#     if text.strip():
#         try:
#             translation = translator.translate(text, src='hi', dest='en')
#             translated_revenue_office.append(translation.text)
#         except:
#             translated_revenue_office.append("")
#     else:
#         translated_revenue_office.append("")

# for text in Buyer_name:
#     if text.strip():
#         try:
#             translation = translator.translate(text, src='hi', dest='en')
#             translated_Buyer_name.append(translation.text)
#         except:
#             translated_Buyer_name.append("")
#     else:
#         translated_Buyer_name.append("")

# for text in Seller_name:
#     if text.strip():
#         try:
#             translation = translator.translate(text, src='hi', dest='en')
#             translated_Seller_name.append(translation.text)
#         except:
#             translated_Seller_name.append("")
#     else:
#         translated_Seller_name.append("")

# for text in Other_information:
#     if text.strip():
#         try:
#             translation = translator.translate(text, src='hi', dest='en')
#             translated_Other_information.append(translation.text)
#         except:
#             translated_Other_information.append("")
#     else:
#         translated_Other_information.append("")

# df  =  pd.DataFrame({'Serial number': serial_number, 'Document number': document_number, 'Document type' : document_type, 'Revenue Office': revenue_office, 'Registration Year': reg_year, 'Buyer name': Buyer_name, 'Seller name': Seller_name, 'Other information' : Other_information, 'List no.2': List_no_2})
# df.to_csv('data.csv', index = False)
# df  = pd.read_csv('data.csv')