from selenium import webdriver
from time import sleep


desired_cap = {
"browser" : "Edge",
}

class InstaBot(object):
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.driver = webdriver.Edge(executable_path="/Users/fred/Downloads/edgedriver_mac64/msedgedriver",capabilities=desired_cap)
        self.driver.get("https://instagram.com")
        sleep(2)
        self.driver.find_element_by_xpath("//input[@name=\"username\"]").send_keys(username)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(password)
        self.driver.find_element_by_xpath("//button[@type=\"submit\"]").click()
        sleep(4)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
        sleep(2)

    def get_unfollowers(self):
        self.driver.find_element_by_xpath("//a[contains(@href, '/{}/')]".format(self.username)).click()
        sleep(2)
        self.driver.find_element_by_xpath("//*[@id=\"react-root\"]/section/main/div/header/section/ul/li[3]/a").click()
        following = self._get_names()
        sleep(2)
        self.driver.find_element_by_xpath("//*[@id=\"react-root\"]/section/main/div/header/section/ul/li[2]/a").click()
        followers = self._get_names()
        sleep(2)
        not_following_me=[user for user in following if user not in followers]
        print(not_following_me)

    def _get_names(self):
        sleep(1)
        scroll_box = self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div[2]")
        sleep(1)
        last_ht, ht = 0,1
        while last_ht != ht:
            last_ht = ht
            sleep(1) 
            ht = self.driver.execute_script("""
            arguments[0].scrollTo(0,arguments[0].scrollHeight);
            return arguments[0].scrollHeight;
            """,scroll_box)
        links = scroll_box.find_elements_by_tag_name("a")
        names = [name.text for name in links if name.text != '']
        self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div[1]/div/div[2]/button").click()
        return names


first_test = InstaBot("foobah","naashome")
first_test.get_unfollowers()