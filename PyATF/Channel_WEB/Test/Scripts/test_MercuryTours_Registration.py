__author__ = 'Vikram C'

import unittest
from time import sleep
from Channel_WEB.Test.TestUtility.ScreenShot import SS
from Channel_WEB.Src.PageObject.Pages.ConfirmationPage import Confirmation
from Channel_WEB.Src.PageObject.Pages.HomePage import Home
from Channel_WEB.Src.TestBase.EnvironmentSetUp import EnvironmentSetup

from Channel_WEB.Src.PageObject.Pages.RegistrationPage import Register


class MercuryTours_Registration(EnvironmentSetup):

    def test_RegistrationFlow(self):

# Screenshots relative paths
        ss_path = "/Test_MercuryTours_Registration/"

        driver = self.driver
        self.driver.get("http://newtours.demoaut.com")
        self.driver.set_page_load_timeout(20)

# Creating object of SS screenshots utility
        ss = SS(driver)
#calling home page object to click on Register Link
        home = Home(driver)
        if home.getRegister().is_displayed():
            print("Register Link displaying")
            home.getRegister().click()
            sleep(4)

#calling registration page object to proceed with registration flow
        reg = Register(driver)
        if reg.getRegis_txt().is_displayed():
            print(reg.regis_txt.text)
            ss.ScreenShot(ss_path+"Registration.png")
        else:
            print("Registration page not loaded")
        try:
            reg.setFirstName("Sarun")
            reg.setLastName("Vikram")
            reg.setPhone("7501498896")
            reg.setEmail("sarun.vikram@gmail.com")
            reg.setCountry("INDIA")
            reg.setUserName("sarun.vikram@gmail.com")
            reg.setPassword(123456)
            reg.setConfirmPassword(123456)
            sleep(2)
            ss.ScreenShot(ss_path+"RegistrationData.png")
            reg.submitRegistration()
            sleep(4)
            ss.ScreenShot(ss_path+"PostRegistration.png")
        except Exception as e:
            print("Exception occurred "+e)

#calling Post Registration check
        post = Confirmation(driver)
        print(post.thankYou.text)
        if (post.UserID.text).find("sarun.vikram@gmail.com"):
            print("Registration Process Successful")
        else:
            print("User Failed to register properly")



if __name__ == '__main__':
    unittest.main()
