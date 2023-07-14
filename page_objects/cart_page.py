from seleniumbase import BaseCase
import time
class CartPage(BaseCase):
    cart = 'https://practice.automationbro.com/cart/'
    file_path = './foto.jpg'
    remove_hiden_class = 'document.getElementByID("upfile_1").classList.remove("file_input_hidden")'
    up_file = '#upfile_1'
    upload_file = '#upload_1'
    submit_message = '#wfu_messageblock_header_1_label_1'

    def cart_page(self):
        self.open(self.cart)

    def add_file(self):
        self.add_js_code(self.remove_hiden_class)
        self.choose_file(self.up_file, self.file_path)
        self.click(self.upload_file)
    
    def verify_upload(self):
        self.wait_for_element_visible(self.submit_message, timeout=15)
        self.assert_text('uploaded successfully', self.submit_message)
