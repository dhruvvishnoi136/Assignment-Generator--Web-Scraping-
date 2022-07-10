from bs4 import BeautifulSoup as be
from selenium import webdriver
import time
import re
class scraper:
    def __init__(self , driver  , file1 ,  file2):
        self.driver = driver 
        self.file1 = file1 
        self.file2 = file2 
    def main(self):
        self.driver.get("https://www.time4education.com/")
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="popupfoot"]/a').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="header"]/div[1]/div[1]/div[3]/div[2]/div[2]/a').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="username"]').send_keys('Your userid') #Change the userid according to you
        self.driver.find_element_by_xpath('//*[@id="password"]').send_keys('Your Password') #Change the password according to you
        self.driver.find_element_by_xpath('//*[@id="loginbtn"]').click()
        time.sleep(1)
        self.driver.get('https://www.time4education.com/e-books/cmatvdhandouts/cmat21classhandouts.asp?idcardno=5c5b482b5c5b48235c5b482c5c5b482e5c5b485f5c5b482e5c5b482d5c5b48365c5b48595c5b48&fg=5c5b485e5c5b48')
        time.sleep(2)
        html = self.driver.page_source
        soup = be(html, 'html.parser')
        link_fetch_file = open('path to your links.txt' , 'w') #Change the path according to you
        hrefs = soup.find_all('a', href=True)
        time.sleep(2)
        for a in hrefs:
            link_fetch_file.writelines("{}\n".format(a['href']))
        link_fetch_file.close()
        time.sleep(1)
        Docs_file = self.file1.readlines()        
        link_file = self.file2.readlines()
        linkss = []
        lis = []
        counter = 0
        for line in Docs_file:
            for link in link_file:   
                if line.split(" ")[0] == link.split("/")[-1].replace(".pdf\n" , "").replace(".doc" , "").replace(" pdf" , ""):
                    linkss.append("".join(re.split("\\n" , link)))
                    counter += 1
        time.sleep(1)
        file_count = 0
        pages_count = []
        for web in linkss:
            self.driver.get(web)
            time.sleep(3)
            self.driver.switch_to.frame(0)
            time.sleep(1)
            self.driver.switch_to.frame(0)
            time.sleep(1)
            self.driver.fullscreen_window()
            counter = 1
            pages =  int(str(self.driver.find_element_by_xpath('//*[@id="numPages"]').get_attribute('innerHTML')).split()[-1])
            pages_count.append(pages)
            for i in range(0 , pages):
                time.sleep(1.75)
                name = (str(web).split("/")[-1].replace(".pdf" , "").replace(".doc" , "").replace(" pdf" , "")) +" "+ str(counter) + str(".png")
                self.driver.get_screenshot_as_file("Path to where your screenshorts will pe saved{}".format(str(name))) #Change the path according to you
                time.sleep(1.75)
                self.driver.find_element_by_xpath('//*[@id="next"]').click()
                counter += 1
            file_count += 1
            time.sleep(2)
        test_count = 0
        for i in pages:
            test_count += int(i)
        print("TOTAL PAGES:- " ,test_count)
        print("TOTAL FILES:- ",file_count)

        
if __name__ == "__main__":
    START_TIME = time.time()
    driver = webdriver.Edge("path to your web browser driver .exe")
    driver.maximize_window()
    open("Path to your links.txt" , 'w').close()
    file1 = (open("path to your web browser driver .exe" , 'r')) #Change the path according to you
    file2 = (open("Path to your links.txt" , 'r')) #Change the path according to you
    try:
        obj = scraper(driver=driver, file1= file1 , file2= file2)
        obj.main()
    finally:
        driver.quit()
        file1.close()
        file2.close()
    print("TIME TAKEN :- " , str(time.time() - START_TIME))