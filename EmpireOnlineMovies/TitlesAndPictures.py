
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

url = 'https://www.empireonline.com/movies/features/best-movies-2'
chrome_driver_path = 'chromedriver'

chrome_options = Options()
chrome_options.add_argument('--headless')

webdriver = webdriver.Chrome(ChromeDriverManager().install())


with webdriver as driver:
    # Set timeout time
    wait = WebDriverWait(driver, 10)

    # Retrieve url in headless browser
    driver.get(url)

    html = driver.page_source

    driver.close()


soup = BeautifulSoup(html, 'html.parser')

titles = soup.find_all(name='h3', class_='jsx-2692754980')
titles = [i.text for i in titles if i.text is not None]
print(titles)

imgs = soup.find('div', class_='jsx-3821216435').find_all('img')
print(imgs)

