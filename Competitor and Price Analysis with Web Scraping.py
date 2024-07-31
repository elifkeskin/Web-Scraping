import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

# Configuring and launching the browser
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)

# Examining and scraping the homepage
Sleep_time=2
driver.get("https://books.toscrape.com/")
time.sleep(Sleep_time)

category_elements_xpath = '//a[contains(text(), "Travel") or contains(text(), "Nonfiction")]'
category_elements = driver.find_elements(By.XPATH, category_elements_xpath)

# Finding category detail links
category_urls = [element.get_attribute("href") for element in category_elements]
print(category_urls)

# Inspecting and Scraping the Category Page
driver.get(category_urls[0])
time.sleep(Sleep_time)

book_elements_xpath = "//div[@class='image_container']//a"
book_elements = driver.find_elements(By.XPATH, book_elements_xpath)

# This way we capture the link each book has.
book_urls = [element.get_attribute("href") for element in book_elements]
print(book_urls)
print(len(book_urls))

# Pagination
MAX_PAGINATION = 10
url = category_urls[1]  # 0:travel, 1:nonfiction
book_urls = []
for i in range(1, MAX_PAGINATION):
    update_url = url if i==1 else url.replace("index", f"page-{i}")
    driver.get(update_url)
    book_elements = driver.find_elements(By.XPATH, book_elements_xpath)
    
    if not book_elements:
        break
    temp_urls = [element.get_attribute("href") for element in book_elements]
    book_urls.extend(temp_urls)

print(book_urls)
print(len(book_urls))

# Scraping the Product Detail Page
driver.get(book_urls[0])
time.sleep(Sleep_time)
content_div = driver.find_elements(By.XPATH, "//div[@class='content']")

inner_html = content_div[0].get_attribute("innerHTML")

soup = BeautifulSoup(inner_html, "html.parser")

# finding book name:
name_elem = soup.find("h1")
book_name = name_elem.text

# finding book price:
price_elem = soup.find("p", attrs={"class":"price-color"})
book_price = price_elem.text

# Finding p element whose class starts with start-rating
import re
regex = re.compile("^star-rating")
star_elem = soup.find("p", attrs={"class":regex})

# The number of stars we want is at the bottom of the list.
book_star_count = star_elem["class"][-1]

# finding book description:
# find_next_sibling() : It finds the next sibling of the element we found.
desc_elem = soup.find("div", attrs={"id":"product description"}).find_next_sibling()
book_desc= desc_elem.text

# Finding the information in the table under the Product Information heading.
# th: key ; td:value
product_info = {}
table_rows = soup.find("table").find_all("tr")

for row in table_rows:
    key = row.find("th").text
    value = row.find("td").text
    product_info[key] = value


