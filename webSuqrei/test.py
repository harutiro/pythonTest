from selenium import  webdriver
from time import sleep


browser = webdriver.Chrome('C:\\Users\\harut\\VSCode\\pythonTest\\webSuqrei\\chromedriver.exe')

url = "https://scraping-for-beginner.herokuapp.com/login_page"
browser.get(url)



# sleep(3)

# browser.quit()