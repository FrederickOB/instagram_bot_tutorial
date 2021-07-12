from selenium import webdriver
from time import sleep


desired_cap = {
"browser" : "Edge",
}


class TwitterBot(object):
    def __init__(self,username,password,tweet):
        self.username = username
        self.password = password
        self.tweet = tweet
        self.driver = webdriver.Edge(executable_path="/Users/fred/Downloads/edgedriver_mac64/msedgedriver",capabilities=desired_cap)
        self.driver.get("https://twitter.com")
        sleep(2)
        self.driver.find_element_by_xpath("//a[contains(@href, '/login')]").click()
        self.driver.find_element_by_xpath("//*[@id=\"react-root\"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input").send_keys(username)
        self.driver.find_element_by_xpath("//*[@id=\"react-root\"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input").send_keys(password)
        self.driver.find_element_by_xpath("//button[@type=\"submit\"]").click()
        sleep(4)


first_test = TwitterBot("friedosei2gmail.com","emmanuel","hi")
