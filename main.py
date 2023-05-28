import json
import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service

PATH = 'msedgedriver.exe'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.62'
edge_options = Options()
edge_options.add_experimental_option('detach', True)
edge_options.add_argument(f'user_agent={user_agent}')
edge_options.add_experimental_option("excludeSwitches", ["enable-logging"])
edge_options.add_argument("--disable-popup-blocking")
edge_options.add_argument('--disable-default-apps')
edge_options.add_argument('--allow-silent-push')
edge_options.add_argument('--disable-notifications')
edge_options.add_argument('--suppress-message-center-popups')
edge_options.add_argument('--inprivate')
edge_options.add_argument('--lang=en')

edge_service = Service(PATH)
driver = webdriver.Chrome(service=edge_service, options=edge_options)


class MainClass:
    """Initialize variables for script"""

    def __init__(self, links, min_likes, login, password):
        self.links = links
        self.min_likes = min_likes
        self.login = login
        self.password = password

    def main(self):
        self.login_fb()

        time.sleep(2)

        self.check_posts()

        driver.quit()

    def login_fb(self):
        driver.get('https://facebook.com/')

        time.sleep(5)

        try:
            cookie_but = driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div/div/div/div/div[4]/button[2]')
            cookie_but.click()
        except Exception:
            pass

        login_field = driver.find_element(By.XPATH, '//*[@id="email"]')
        pass_field = driver.find_element(By.XPATH,
                                         '/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[2]/div/input')

        login_field.send_keys(self.login)
        pass_field.send_keys(self.password)

        login_button = driver.find_element(By.XPATH,
                                           '/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]')
        login_button.click()

    def check_posts(self):
        delete_post_links = []

        for i in self.links:
            driver.get(self.normalize_link(i))

            scroll_to_bottom()

            feed = driver.find_element(By.XPATH, '//section[@class="_7k7 storyStream _2v9s"]')
            all_posts = feed.find_elements(By.XPATH, '//article[@class="_55wo _5rgr _5gh8 async_like"]')

            for j in all_posts:
                likes = 0
                try:
                    likes_block = j.find_element(By.CLASS_NAME, "_1g06").text
                    if likes_block == '':
                        likes = 0
                    elif not likes_block.isdigit():
                        liked_person = likes_block.split()
                        for k in liked_person:
                            if k.isdigit():
                                likes = int(k) + 1
                                break
                            else:
                                likes = 1
                    else:
                        likes = int(likes_block)

                except Exception:
                    likes = 0

                print(likes)

                if likes < self.min_likes:
                    delete_post_links.append(j.find_element(By.XPATH, './/a[@class="_5msj"]').get_attribute('href'))
        if delete_post_links:
            self.delete_post(delete_post_links)

    def delete_post(self, posts_link):
        for i in posts_link:
            driver.get(i)

            driver.implicitly_wait(2)

            try:
                option_button = driver.find_element(By.XPATH,
                                                    '//div[@class="xqcrz7y x78zum5 x1qx5ct2 x1y1aw1k x1sxyh0 xwib8y2 xurb0ha xw4jnvo"]')
                option_button.click()

                driver.implicitly_wait(3)
                time.sleep(1)

                try:
                    delete_button = driver.find_element(By.XPATH, '//span[text()="Delete post"]')
                    delete_button.click()

                    driver.implicitly_wait(5)
                    time.sleep(1)

                    confirm_delete = driver.find_element(By.XPATH, '//span[text()="Delete"]')
                    confirm_delete.click()
                except Exception:
                    try:
                        delete_button = driver.find_element(By.XPATH, '//span[text()="Remove post"]')
                        delete_button.click()

                        driver.implicitly_wait(5)
                        time.sleep(1)

                        confirm_delete = driver.find_element(By.XPATH, '//span[text()="Confirm"]')
                        confirm_delete.click()
                    except Exception as e:
                        print(e)
            except Exception as e:
                print(e)

            time.sleep(3)

    def normalize_link(self, link):
        link = link.split('https://www.')

        return 'https://m.' + link[1]


def scroll_to_bottom():
    current_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
        time.sleep(2)

        new_height = driver.execute_script("return document.body.scrollHeight")

        if new_height == current_height:
            break

        current_height = new_height


if __name__ == "__main__":
    with open('parameters.json') as file:
        data = json.load(file)

    script = MainClass(links=data['groups_link'], min_likes=data['minimal_likes'], login=data['email'],
                       password=data['password'])

    script.main()
