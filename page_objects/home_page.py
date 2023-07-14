from seleniumbase import BaseCase

class HomePage(BaseCase):
    home = 'https://practice.automationbro.com'
    title_page = 'Practice E-Commerce Site – Automation Bro'
    get_started_btn = '#get-started'
    logo_icon = '.custom-logo-link'
    heading_text = 'h1'
    copyright_text = '.tg-site-footer-section-1'
    menu_links = '#primary-menu li[id*= menu-item]'
    expected_links = ['Home', 'About', 'Shop', 'Blog', 'Contact', 'My account']

    def open_page(self):
        self.open(self.home)

    def verify_page_title(self):
        self.assert_title(self.title_page)

    def verify_logo(self):
        self.assert_element(self.logo_icon)

    def verify_click_get_started_btn(self):
        self.click(self.get_started_btn)
        get_started_url = self.get_current_url()
        self.assert_true('get-started' in get_started_url)

    def verify_heading_text(self):
        self.assert_text('Think different. Make different.', self.heading_text)

    def verify_copyright(self):
        self.scroll_to_bottom()
        self.assert_text('Copyright © 2020 Automation Bro', self.copyright_text)

    def verify_links_menu(self):
        menu_links_el = self.find_elements(self.menu_links)
        for idx, link_ele in enumerate(menu_links_el):
            print(link_ele.text)
            self.assertEquals(self.expected_links[idx], link_ele.text)


