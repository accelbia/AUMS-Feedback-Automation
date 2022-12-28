from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import streamlit as st

def start_rating(driver, links, rating):
    for i in links:
        driver.get(i)
        rating_str = str(5-rating)
        _ = [x.click() for x in driver.find_elements(By.XPATH, '//input[@type="radio"]') if x.get_attribute("value") == rating_str]
        driver.find_element(By.ID, 'form-branch::submitEvaluation').click()
    return 0

def opensite(driver, rating):
    driver.maximize_window()
    driver.get("https://aumscb.amrita.edu/cas/login?service=https%3A%2F%2Faumscb.amrita.edu%2Faums%2FJsp%2FCore_Common%2Findex.jsp")
    
    
    driver.find_element('id', 'username').send_keys(username)
    driver.find_element('id', 'password').send_keys(password)
    driver.find_element('name', 'submit').send_keys(Keys.ENTER)
    
    WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.ID,"maincontentframe")))
    WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.ID,"Iframe1")))
    WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.ID,"sakaiframeId")))
    driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div[2]/nav/div[2]/ul/li[1]/a[2]").click()
    driver.implicitly_wait(5)
    driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div[2]/nav/div[2]/ul/li[1]/ul/li[4]/a").click()
    WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.CLASS_NAME,"portletMainIframe")))
    all_anchors = [x.get_attribute("href") for x in driver.find_elements(By.XPATH, '//a')]
    review_links = [x for x in all_anchors if "take_eval" in x]
    if review_links:
        start_rating(driver, review_links, rating)
    
    return

def formfill():
    if username and password and browser:
        try: 
            if browser == 'Chrome':
                driver = webdriver.Chrome()
            elif browser == 'Firefox':
                driver = webdriver.Firefox()
            elif browser == 'Edge':
                driver = webdriver.Edge()
            opensite(driver, rating)
            st.balloons()
            st.warning('Feedback Filled')
            driver.quit()
        except: 
            st.error('Browser not found')
    else:
        st.warning('Please enter username, password and select browser')
        return

st.title('AUMS Feedback Filler')

username = st.text_input('Username')
password = st.text_input('Password', type='password')
browser = st.radio('Browser', ( 'Edge', 'Chrome', 'Firefox'))
rating = st.slider('Rating', 1, 5, 5)


st.button('Fill Feedback', on_click=formfill)
