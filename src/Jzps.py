#! /usr/bin/env python
#coding=utf-8

'''
FuncName: Jzps.py
Desc: update selenium
Date: 2016-08-23 08:30
Home: http://blog.csdn.net/z_johnny
Author: johnny
'''

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import os,sys,time

reload(sys)
sys.setdefaultencoding('utf-8')

class Jzps(object):
    """
        Jzps framework are committed to a simpler automated testing,
    based on the original selenium.
    """

    def __init__(self, browser='firefox'):
        """
        Run class initialization method, the default is proper
        to drive the Firefox browser,. Of course, you can also
        pass parameter for other browser, such as Chrome browser for the "Chrome",
        the Internet Explorer browser for "internet explorer" or "ie".
        """
        if browser == "firefox" :
            driver = webdriver.Firefox()
        elif browser == "chrome":
            driver = webdriver.Chrome()
        elif browser == "ie" :
            driver = webdriver.Ie()
        elif browser == "phantomjs":
            driver = webdriver.PhantomJS()
        try:
            self.driver = driver
        except Exception:
            raise NameError("Not found this browser,You can enter 'firefox', 'chrome', 'ie' or 'phantomjs'.")

    def get(self, url):
        """
        Open url,same as get.

        Usage:
        driver.get("https://www.baidu.com")
        """
        self.driver.get(url)

    def max_window(self):
        """
        Set browser window maximized.

        Usage:
        driver.max_window()
        """
        self.driver.maximize_window()

    def set_window_size(self, wide, high):
        """
        Set browser window wide and high.

        Usage:
        driver.set_window_size(wide,high)
        """
        self.driver.set_window_size(wide, high)

    def wait(self, secsonds):
        """
        Implicitly wait.All elements on the page.

        Usage:
        driver.wait(10)
        """
        self.driver.implicitly_wait(secsonds)

    def find_element(self,element):
        """
        Judge element positioning way, and returns the element.

        Usage:
        driver.find_element("id=kw")
        """
        if "=" not in element:
            raise NameError("SyntaxError: invalid syntax, lack of '='.")

        by = element.split("=")[0]
        value = element.split("=")[1]

        if by == "id":
            return self.driver.find_element_by_id(value)
        elif by == "name":
            return self.driver.find_element_by_name(value)
        elif by == "class":
            return self.driver.find_element_by_class_name(value)
        elif by == "text":
            return self.driver.find_element_by_link_text(value)
        elif by == "text_part":
            return self.driver.find_element_by_partial_link_text(value)
        elif by == "xpath":
            return self.driver.find_element_by_xpath(value)
        elif by == "css":
            return self.driver.find_element_by_css_selector(value)
        else:
            raise NameError("Please enter the correct targeting elements,'id','name','class','text','xpath','css'.")

    def wait_element(self, element, seconds=5):
        """
        Waiting for an element to display.
        
        Usage:
        driver.wait_element("id=kw",10)
        """
        if "=" not in element:
            raise NameError("SyntaxError: invalid syntax, lack of '='.")

        by = element.split("=")[0]
        value = element.split("=")[1]

        if by == "id":
            WebDriverWait(self.driver,seconds,1).until(EC.presence_of_element_located((By.ID, value)))
        elif by == "name":
            WebDriverWait(self.driver,seconds,1).until(EC.presence_of_element_located((By.NAME, value)))
        elif by == "class":
            WebDriverWait(self.driver,seconds,1).until(EC.presence_of_element_located((By.CLASS_NAME, value)))
        elif by == "text":
            WebDriverWait(self.driver,seconds,1).until(EC.presence_of_element_located((By.LINK_TEXT, value)))
        elif by == "xpath":
            WebDriverWait(self.driver,seconds,1).until(EC.presence_of_element_located((By.XPATH, value)))
        elif by == "css":
            WebDriverWait(self.driver,seconds,1).until(EC.presence_of_element_located((By.CSS_SELECTOR, value)))
        else:
            raise NameError("Please enter the correct targeting elements,'id','name','class','text','xpaht','css'.")

    def send_keys(self, element, text):
        """
        Operation input content after clear.

        Usage:
        driver.send_keys("id=kw","selenium")
        """
        self.wait_element(element)
        self.find_element(element).clear()
        self.find_element(element).send_keys(text)

    def click(self, element):
        """
        It can click any text / image can be clicked
        Connection, check box, radio buttons, and even drop-down box etc..
        
        Usage:
        driver.click("id=kw")
        """
        self.wait_element(element)
        self.find_element(element).click()

    def right_click(self, element):
        """
        Right click element.

        Usage:
        driver.right_click("class=right")
        """
        self.wait_element(element)
        ActionChains(self.driver).context_click(self.find_element(element)).perform()

    def move_to_element(self, element):
        '''
        Mouse over the element.

        Usage:
        driver.move_to_element("css=choose")
        '''
        self.wait_element(element)
        ActionChains(self.driver).move_to_element(self.find_element(element)).perform()

    def double_click(self, element):
        """
        Double click element.

        Usage:
        driver.double_click("name=baidu")
        """
        self.wait_element(element)
        ActionChains(self.driver).double_click(self.find_element(element)).perform()

    def drag_and_drop(self, source_element, target_element):
        """
        Drags an element a certain distance and then drops it.

        Usage:
        driver.drag_and_drop("id=s","id=t")
        """
        self.wait_element(source_element)
        self.wait_element(target_element)
        ActionChains(self.driver).drag_and_drop(self.find_element(source_element), self.find_element(target_element)).perform()

    def back(self):
        """
        Back to old window.

        Usage:
        driver.back()
        """
        self.driver.back()

    def forward(self):
        """
        Forward to old window.

        Usage:
        driver.forward()
        """
        self.driver.forward()

    def get_attribute(self, element, attribute):
        """
        Gets the value of an element attribute.

        Usage:
        driver.get_attribute("id=kw","attribute")
        """
        self.wait_element(element)
        return self.find_element(element).get_attribute(attribute)

    def get_text(self, element):
        """
        Get element text information.

        Usage:
        driver.get_text("name=johnny")
        """
        self.wait_element(element)
        return self.find_element(element).text

    def get_display(self, element):
        """
        Gets the element to display,The return result is true or false.

        Usage:
        driver.get_display("id=ppp")
        """
        self.wait_element(element)
        return self.find_element(element).is_displayed()

    def get_title(self):
        """
        Get window title.

        Usage:
        driver.get_title()
        """
        return self.driver.title

    def get_url(self):
        """
        Get the URL address of the current page.

        Usage:
        driver.get_url()
        """
        return self.driver.current_url

    def get_screenshot(self, file_path):
        """
        Get the current window screenshot.

        Usage:
        driver.get_screenshot("./pic.png")
        """
        self.driver.get_screenshot_as_file(file_path)

    def submit(self, element):
        """
        Submit the specified form.

        Usage:
        driver.submit("id=mainFrame")
        """
        self.wait_element(element)
        self.find_element(element).submit()

    def switch_to_frame(self, element):
        """
        Switch to the specified frame.

        Usage:
        driver.switch_to_frame("id=mainFrame")
        """
        self.wait_element(element)
        self.driver.switch_to_frame(self.find_element(element))

    def switch_to_frame_out(self):
        """
        Returns the current form machine form at the next higher level.
        Corresponding relationship with switch_to_frame () method.

        Usage:
        driver.switch_to_frame_out()
        """
        self.driver.switch_to.default_content()

    def open_new_window(self, element):
        """
        Open the new window and switch the handle to the newly opened window.

        Usage:
        driver.open_new_window(id=johnny)
        """
        current_windows = self.driver.current_window_handle
        self.find_element(element).click()
        all_handles = self.driver.window_handles
        for handle in all_handles:
            if handle != current_windows:
                self.driver.switch_to.window(handle)
    def F5(self):
        '''
        Refresh the current page.

        Usage:
        driver.F5()
        '''
        self.driver.refresh()

    def js(self, script):
        """
        Execute JavaScript scripts.

        Usage:
        driver.js("window.scrollTo(200,1000);")
        """
        self.driver.execute_script(script)

    def accept_alert(self):
        """
        Accept warning box.

        Usage:
        driver.accept_alert()
        """
        self.driver.switch_to.alert.accept()

    def dismiss_alert(self):
        """
        Dismisses the alert available.

        Usage:
        driver.dismiss_alert()
        """
        self.driver.switch_to.alert.dismiss()

    def close(self):
        """
        Close the windows.

        Usage:
        driver.close()
        """
        self.driver.close()

    def quit(self):
        """
        Quit the driver and close all the windows.
        
        Usage:
        driver.quit()
        """
        self.driver.quit()


if __name__ == '__main__':
    driver = Jzps("chrome")
    driver.get("http://www.baidu.com")
    driver.find_element("id=kw")
    driver.set_window_size(1366,768)
    time.sleep(2)
    driver.max_window()
    driver.send_keys("id=kw",u"Johnny'lab")
    time.sleep(2)
    driver.click("id=su")
    time.sleep(2)
    driver.click("id=result_logo")
    time.sleep(2)
    driver.F5()
    driver.get_screenshot("./Jzps.png")
    time.sleep(2)
    driver.right_click("text=登录")
    print driver.get_url()
    print driver.get_text("name=tj_trnuomi")
    driver.move_to_element("id=su")
    print driver.get_title()
    driver.open_new_window("name=tj_trnuomi")
    driver.back()
    time.sleep(2)
    driver.forward()
    driver.quit()


