from bs4 import BeautifulSoup as be
from selenium import webdriver
import time
import re

from selenium.webdriver.firefox.webdriver import WebDriver

class scraper:
    def __init__(self , driver  , file1 ,  file2):

        self.driver = driver 
        self.file1 = file1 
        self.file2 = file2 

    def main(self):
        driver.get("https://www.time4education.com/")
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="popupfoot"]/a').click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="header"]/div[1]/div[1]/div[3]/div[2]/div[2]/a').click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="username"]').send_keys('userid')#Change the userid according to you
        driver.find_element_by_xpath('//*[@id="password"]').send_keys('password')#Change the password according to you
        driver.find_element_by_xpath('//*[@id="loginbtn"]').click()

        time.sleep(1)
        driver.get('https://www.time4education.com/e-books/mahcet21/MAHCET2021classhandouts.asp?idcardno=5b56482b5b5648235b56482c5b56482e5b56485f5b56482e5b56482d5b5648365b5648595b5648&fg=5b56485e5b5648')
        time.sleep(2)
        html = driver.page_source
        soup = be(html, 'html.parser')
        link_fetch_file = open('path to your links.txt' , 'w') #Change the path according to you
        hrefs = soup.find_all('a', href=True)
        time.sleep(2)
        for a in hrefs:
            link_fetch_file.writelines("{}\n".format(a['href']))

        link_fetch_file.close()
        time.sleep(1)
        Docs_file = file1.readlines()        
        link_file = file2.readlines()
        linkss = []
        counter = 0
        for line in Docs_file:
            for link in link_file:   
                if line.split(" ")[0] == link.split("/")[-1].replace(".pdf\n" , ""):
                    linkss.append("".join(re.split("\\n" , link)))
                    counter += 1

        time.sleep(1)
        file_count = 0
        pages_count = []
        for web in linkss:
            driver.get(web)
            time.sleep(3)
            driver.switch_to.frame(0)
            time.sleep(1)
            driver.switch_to.frame(0)
            time.sleep(1)
            driver.fullscreen_window()
            counter = 1
            time.sleep(0.5)
            pages =  int(str(driver.find_element_by_xpath('//*[@id="numPages"]').get_attribute('innerHTML')).split()[-1])
            pages_count.append(pages)
            if driver.find_element_by_xpath('//*[@id="pageNumber"]').get_attribute('value') != 1:
                test = [driver.find_element_by_xpath('//*[@id="pageNumber"]').get_attribute('value')]
                for test in range(0 ,int(test[0])):
                    driver.find_element_by_xpath('//*[@id="previous"]').click()

            time.sleep(1.5)
            
            for i in range(0 , pages):    
                time.sleep(0.75)
                name = (str(web).split("/")[-1].replace(".pdf" , "")) +" "+ str(counter) + str(".png")
                driver.get_screenshot_as_file("Path to where your screenshorts will pe saved{}".format(str(name)))#Change the path according to you
                time.sleep(1)
                driver.find_element_by_xpath('//*[@id="next"]').click()
                counter += 1
            
            file_count += 1

            time.sleep(2)
        
        test_count = 0
        for i in pages_count:
            test_count += int(i)
        print("TOTAL PAGES:- " ,test_count)
        print("TOTAL FILES:- ",file_count)
        


if __name__ == "__main__":
    START_TIME = time.time()
    driver = webdriver.Edge("path to your web browser driver .exe")
    driver.maximize_window()
    open("path to your links.txt" , 'w').close()#Change the path according to you
    file1 = (open("Path to where a temperary file named 'MHCET_Docs_names.txt' be saved" , 'r'))#Change the path according to you
    file2 = (open("path to your links.txt" , 'r'))#Change the path according to you
    try:
        obj = scraper(driver=driver, file1= file1 , file2= file2)
        obj.main()
    finally:
        driver.quit()
        file1.close()
        file2.close()
    
    print("TIME TAKEN :- " , str(time.time() - START_TIME))