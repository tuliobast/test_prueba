from seleniumbase import BaseCase
from selenium.webdriver.common.keys import Keys
class ShopPage(BaseCase):
    shop = 'https://practice.automationbro.com/shop/'
    add_to_cart = 'a[aria-label="Add “Canon Antique Camera” to your cart"]'
    cart_count_text = '//*[@id="header-action"]/ul/li[2]/a/span'
    view_cart_text= '//*[@id="primary"]/ul/li[2]/a[3]'
    subtotal_text = '//*[@id="post-7"]/div/div[2]/div[2]/div/table/tbody/tr[1]/td/span'
    product_quantity = 'input[id^="quantity"]'
    update_cart_btn = '//*[@id="post-7"]/div/div[2]/form/table/tbody/tr[2]/td/button'
    subtotal = ''

    #open shop page
    def open_shop(self):
        self.open(self.shop)

    #add item to cart
    def add_cart(self):
        self.click(self.add_to_cart)

    #verify to add item to cart
    def verify_add_to_cart(self):
        self.assert_text('1', self.cart_count_text)

    #verify link to cart
    def verify_link_cart(self):
        self.wait_for_element_visible(self.view_cart_text)

    #view cart
    def view_cart(self):
        self.click(self.view_cart_text)

    #get current Subtotal
    def get_current_subtotal(self):
        self.wait_for_element_visible(self.subtotal_text)
        self.subtotal = self.get_text(self.subtotal_text)
        print(self.subtotal)

    #change quantity of item
    def chance_cart_quantity(self):
        self.set_value(self.product_quantity, '8')
        self.send_keys(self.product_quantity, Keys.RETURN)
        self.click(self.update_cart_btn)

    #wait for teh current subtotal
    def wait_for_current_subtotal(self):
        self.wait_for_element_visible(self.subtotal_text)
        self.wait_for_element_not_visible(self.subtotal_text)
        self.wait(12)

    #Verify change subtotal
    def update_subtotal(self):
        update_subtotal = self.get_text(self.subtotal_text)
        print(update_subtotal)
        self.assertNotEquals(self.subtotal, update_subtotal)