from page_objects.home_page import HomePage
from page_objects.login_page import LoginPage
from page_objects.contact_page import ContactPage
from page_objects.cart_page import CartPage
from page_objects.shop_page import ShopPage

class LoginTest(HomePage, LoginPage, ContactPage, CartPage, ShopPage):

    def setUp(self):
        super().setUp()
        print('running before each test')
        # open home page
        self.open_page()

    def test_login(self):
        self.login()
        #self.logout()

    def test_home_page(self):
        #verify page title
        self.verify_page_title()

        #verify logo
        self.verify_logo()

        #verify click en el botton get started
        self.verify_click_get_started_btn()

        #verify texto del h1
        self.verify_heading_text()

        #scrolldown y assert copyright text
        self.verify_copyright()

        #assert de los links de menu
        self.verify_links_menu()

    def test_contact_page(self):
        # open contact page
        self.contact_page()

        # fill all the fields
        self.fill_fields()

        # click in submit botton
        self.click_submit_btn()

        # assert submit message
        self.verify_submit_msg()

    def test_upload_file(self):
        #open cart page
        self.cart_page()

        #add file
        self.add_file()

        self.verify_upload()

    def test_add_to_cart(self):
        self.open_shop()
        self.add_cart()
        self.verify_link_cart()
        self.view_cart()
        self.verify_add_to_cart()
        self.get_current_subtotal()
        self.chance_cart_quantity()
        self.update_subtotal()

    '''def test_logout(self):
        self.login()
        self.logout()'''

    def tearDown(self):
        print('running after each test')
        super().tearDown()



