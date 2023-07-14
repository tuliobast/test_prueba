from seleniumbase import BaseCase

class ContactPage(BaseCase):
    contact = 'https://practice.automationbro.com/contact/'
    contact_name = '.contact-name input'
    contact_email = '.contact-email input'
    contact_phone = '.contact-phone input'
    contact_message = '.contact-message textarea'
    submit_btn = '#evf-submit-277'
    submit_massage = 'div[role=alert'

    def contact_page(self):
        self.open(self.contact)

    # fill all the fields
    def fill_fields(self):
        self.send_keys(self.contact_name, 'Test Name')
        self.send_keys(self.contact_email, 'test@mail.com')
        self.send_keys(self.contact_phone, '0384732123')
        self.send_keys(self.contact_message, 'This is a test message')

    #click in submit botton
    def click_submit_btn(self):
        self.click(self.submit_btn)

    #assert submit message
    def verify_submit_msg(self):
        self.wait_for_element_visible(self.submit_massage)
        self.assert_text('Thanks for contacting us! We will be in touch with you shortly', self.submit_massage)
        #Thanks for contacting us! We will be in touch with you shortly