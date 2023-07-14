from seleniumbase import BaseCase

class LoginPage(BaseCase):
    my_account = 'https://practice.automationbro.com/my-account'
    username = '#username'
    password = '#password'
    btn_login = 'button[name=login]'
    btn_logout = '.woocommerce-MyAccount-content a[href*=logout]'
    logout_text = '.woocommerce-MyAccount-content'

    def login(self):
        self.open(self.my_account)
        self.add_text(self.username, 'tuliobast')
        self.add_text(self.password, 'Jag$5247pa')
        self.click(self.btn_login)
        self.assert_text('Log out', self.logout_text)

    def logout(self):
        self.open(self.my_account)
        self.click(self.btn_logout)
        self.assert_element_visible(self.btn_login)