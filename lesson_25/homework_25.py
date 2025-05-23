import requests

"""
Написати 25 XPath та 25 CSS локаторів для сайту https://qauto2.forstudy.space/
"""

username = "guest"
passwd = "welcome2qauto"
url = f"https://{username}:{passwd}@qauto2.forstudy.space"

# LOCATORS

"""xpath locators class"""


class XPATH:
    SIGN_IN_BUTTON_XPATH = "//button[contains(@class, 'header_signin') and text()='Sign In']"
    GUEST_LOG_IN_XPATH = "//button[contains(@class, 'header-link') and contains(@class, '-guest') and text()='Guest log in']"
    EMAIL_INPUT_XPATH = "//input[@name='email']"
    PASSWORD_INPUT_XPATH = "//input[@type='password']"
    LOG_IN_XPATH = "//button[contains(@class, 'btn') and contains(@class, 'btn-primary') and text()='Login']"
    FORGOT_PASSWORD_XPATH = "//button[contains(@class, 'btn') and contains(@class, 'btn-link') and text()='Forgot password']"
    REGISTRATION_XPATH = "//button[contains(@class, 'btn') and contains(@class, 'btn-link') and text()='Registration']"
    SIGN_UP_XPATH = "//button[contains(@class, 'hero-descriptor_btn') and contains(@class, 'btn') and contains(@class, 'btn-primary') and text()='Sign up']"
    SUPPORT_EMAIL_XPATH = "//a[text()='support@ithillel.ua']"
    FACEBOOK_LINK_XPATH = "//a[contains(@href, 'facebook.com/Hillel') and contains(@class, 'socials_link')]"
    TELEGRAM_LINK_XPATH = "//a[contains(@href, 't.me/ithillel') and contains(@class, 'socials_link')]"
    INSTAGRAM_LINK_XPATH = "//a[contains(@href, 'instagram.com') and contains(@class, 'socials_link')]"
    LINKEDIN_LINK_XPATH = "//a[.//span[contains(@class, 'icon-linkedin')]]"
    CONTACTS_HEADING_XPATH = "//h2[text()='Contacts']"
    CONTACTS_SECTION_XPATH = "//div[@id='contactsSection' or contains(@class, 'section contacts')]"
    HOME_LINK_XPATH = "//a[@routerlink='/' and contains(@class, 'header-link')]"
    YOUTUBE_ICON_XPATH = "//a[contains(@href, 'youtube.com') and contains(@class, 'socials_link')]"
    LOGIN_FORM_XPATH = "//div[contains(@class, 'modal')]//form"
    LOGO_SVG_XPATH = "//a[contains(@class, 'header_logo')]//svg"
    ABOUT_BUTTON_BY_ATTR_XPATH = "//button[@appscrollto='aboutSection']"
    CONTACTS_BUTTON_BY_ATTR_XPATH = "//button[@appscrollto='contactsSection']"
    SOCIALS_CONTAINER_XPATH = "//div[contains(@class, 'contacts_socials')]"
    ABOUT_BUTTON_XPATH = "//button[text()='About']"
    CONTACTS_BUTTON_XPATH = "//button[text()='Contacts']"
    LOGO_LINK_XPATH = "//a[@routerlink='/' and contains(@class, 'header_logo')]"


"""CSS locators class"""


class CSS:
    SIGN_IN_BUTTON_CSS = "button.header_signin"
    GUEST_LOG_IN_CSS = "button.header-link.-guest"
    LOG_IN_BUTTON_CSS = "button.btn.btn-primary"
    FORGOT_PASSWORD_CSS = "app-signin-form button.btn.btn-link:nth-of-type(1)"
    REGISTRATION_BUTTON_CSS = "button.btn.btn-link"
    SIGN_UP_BUTTON_CSS = "button.hero-descriptor_btn.btn.btn-primary"
    LOGO_SVG_CSS = "a.header_logo svg"
    FACEBOOK_LINK_CSS = "a.socials_link[href*='facebook.com/Hillel']"
    TELEGRAM_LINK_CSS = "a.socials_link[href*='t.me/ithillel']"
    INSTAGRAM_LINK_CSS = "a.socials_link[href*='instagram.com']"
    LINKEDIN_LINK_CSS = "a.socials_link .icon-linkedin"
    HOME_LINK_CSS = "a.header-link[routerlink='/']"
    LOGO_LINK_CSS = "a.header_logo[routerlink='/']"
    EMAIL_INPUT_CSS = "input[name='email']"
    PASSWORD_INPUT_CSS = "input[type='password']"
    YOUTUBE_ICON_CSS = "a.socials_link[href*='youtube.com']"
    LOGIN_FORM_CSS = "div.modal-content app-signin-form form"
    CONTACTS_SECTION_CSS = "div.section.contacts"
    INSTRUCTIONS_TITLE_CSS = "div.col-lg-6 p.about-block_title.h2"
    SUPPORT_EMAIL_CSS = " a[href^='mailto:developer@ithillel.ua']"
    SOCIALS_CONTAINER_CSS = "div.contacts_socials"
    ABOUT_BUTTON_CSS = "button[appscrollto='aboutSection']"
    CONTACTS_BUTTON_CSS = "button[appscrollto='contactsSection']"
    CONTACTS_HEADING_CSS = "div.contacts h2"
