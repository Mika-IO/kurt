# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from getpass import getpass
import random


class InstagramBot:
    def __init__(self, username, password, driver_path, post_link, comment, number_of_comments):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome(executable_path=driver_path)

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com")
        time.sleep(1)
        try:
            login_button = driver.find_element_by_xpath(
                "//a[@href='/accounts/login/?source=auth_switcher']"
            )
            login_button.click()
        except:
            print('\nJá estamos na página de login!\n')
            pass
        user_element = driver.find_element_by_xpath(
            "//input[@name='username']")
        user_element.clear()
        time.sleep(2)
        user_element.send_keys(self.username)
        time.sleep(2)
        password_element = driver.find_element_by_xpath(
            "//input[@name='password']")
        password_element.clear()
        password_element.send_keys(self.password)
        time.sleep(3)
        password_element.send_keys(Keys.RETURN)
        self.comentar(post_link, comment, number_of_comments)
        time.sleep(10)

    def comentar(self, post_link, comment, number_of_comments):
        time.sleep(random.randint(4, 8))
        self.driver.get(post_link)
        comment_area = self.driver.find_element_by_class_name('Ypffh')
        time.sleep(random.randint(1, 3))
        c = 0
        for i in range(number_of_comments):
            try:
                c += 1
                comment_area.click()
                time.sleep(random.randint(2, 4))
                comment_area = self.driver.find_element_by_class_name('Ypffh')
                comment_area.send_keys(comment)
                time.sleep(random.randint(2, 5))
                button_publish = self.driver.find_element_by_class_name('sqdOP.yWX7d.y3zKF')
                button_publish.click()
                time.sleep(random.randint(3, 6))
                ncomment = i + 1
                print('\ncomment',ncomment,'\n')
                if c == 5:
                    c = 0
                    time.sleep(15)
            except:
                sleeping = random.randint(25,45)
                sleeping += i
                print(f"\nOcorreu um erro... Esperando {sleeping}seg\n")
                button_publish = self.driver.find_element_by_class_name('sqdOP.yWX7d.y3zKF')
                button_publish.click()
                time.sleep(random.randint(3, 5))
                time.sleep(sleeping)

    def curtir_fotos_com_a_hastag(self, hashtag):
        driver = self.driver
        driver.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
        time.sleep(5)
        for i in range(
            1, 3
        ):  # Altere o segundo valor aqui para que ele desça a quantidade de páginas que você quiser: quer que ele desça 5 páginas então você deve alterar de range(1,3) para range(1,5)
            driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)
        hrefs = driver.find_elements_by_tag_name("a")
        pic_hrefs = [elem.get_attribute("href") for elem in hrefs]
        print(hashtag + " fotos: " + str(len(pic_hrefs)))
        testes = [
            href
            for href in pic_hrefs
            if hashtag in href and href.index("https://www.instagram.com/p") != -1
        ]

        for pic_href in pic_hrefs:
            try:
                pic_href.index("https://www.instagram.com/p")
            except ValueError as err:
                print("pulando link inválido")
                continue
            driver.get(pic_href)
            driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);")
            try:
                driver.find_element_by_xpath(
                    '//button[@class="dCJp8 afkep"]').click()
                time.sleep(20)
            except Exception as e:
                print(e)
                time.sleep(5)

print('\n##### Kurt Boot ####\n')

if not login:
    login.append(input('\nQual é seu email? '))
    login.append(getpass('\nQual é sua senha? '))

post_link = input('Qual o link do post? ')
comment = input('Qual seu comentário? ')
number_of_comments = int(input('Quantas vezes quer comentar? '))

kurt = InstagramBot(login[0], login[1], 'C:\\Users\\mikai\\Desktop\\kurt\\chromedriver.exe', post_link, comment, number_of_comments)
kurt.login()
