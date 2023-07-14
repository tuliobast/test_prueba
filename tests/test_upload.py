from seleniumbase import BaseCase
import time

class UploadTest(BaseCase):
    def test_visible_upload(self):
        self.open('https://the-internet.herokuapp.com/upload')
        # find archive path
        file_path = '../foto.jpg'
        # upload file
        #time.sleep(5)
        self.choose_file("#file-upload", file_path)
        # click upload botton
        #time.sleep(5)
        self.click("#file-submit")
        # assert file upload text
        self.assert_text("File Uploaded!", "h3")

    def test_hidden_upload(self):
        self.open('https://practice.automationbro.com/cart/')
        # find archive path
        file_path = '../foto.jpg'
        #add js code
        remove_hiden_class = 'document.getElementByID("upfile_1").classList.remove("file_input_hidden")'
        self.add_js_code(remove_hiden_class)
        # upload file
        #time.sleep(5)
        self.choose_file('#upfile_1', file_path)
        # click upload botton
        self.click('#upload_1')
        #time.sleep(5)
        self.wait_for_element_visible('#wfu_messageblock_header_1_label_1', timeout=20)
        # assert file upload text
        self.assert_text('uploaded successfully', '#wfu_messageblock_header_1_label_1')
