"""
Defines Title Scraper Class
"""

import time

from newspaper import Article

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from webdriver_manager.chrome import ChromeDriverManager


class ScraperException(Exception):
    """Exception for failing on fiding a Title"""

    def __init__(self, message):
        super().__init__(message)


class TitleScraper:

    def __init__(self, wait):
        self.wait = wait

    def get_title(self, url):
        """
        Using newspaper3k receives
        a url and capetures it's title
        if anything goes wrong it uses
        selenium to capture the title
        """
        try:
            # First tries newspaper3k
            # raise Exception('force selenium')
            article = Article(url, language='pt')
            article.download()
            article.parse()
            return article.title.strip()
        except:
            try:
                # Than scrapes through selenium
                article = Article(url, language='pt')
                article.html = self.__get_html_with_selenium(url)
                article.download_state = 2
                article.parse()
                return article.title.strip()
            except:
                try:
                    title = self.get_title_by_url(url)
                    if title != 'NULL' and title != '':
                        return title
                    else:
                        raise ScraperException('Não foi possível capturar o título da URL')
                except Exception as e:
                    raise ScraperException(str(e))

    def __get_html_with_selenium(self, url):
        """
        Use selenium to load HTML from URL
        """
        # Set Chrome options:
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--window-size=1920x1080")
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--verbose')
        chrome_options.add_experimental_option("prefs", {
            "download.default_directory": "",
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing_for_trusted_sources_enabled": False,
            "safebrowsing.enabled": False
        })
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--disable-software-rasterizer')
        # Create drive:
        driver = webdriver.Chrome(
            ChromeDriverManager(
                log_level=0,
                cache_valid_range=7
            ).install(),
            options=chrome_options
        )
        # Specify wait time:
        wait = WebDriverWait(driver, self.wait) #15
        # Access url:
        try:
            driver.get(url)
            wait.until(
                EC.presence_of_element_located(
                    (By.TAG_NAME, "body"))
                )
            time.sleep(3)
            html = driver.page_source
            driver.close()
        except:
            # Prevents not closed drivers
            driver.close()
            raise

        return html

    def __extract_title(self, s) -> str:
        """
        Mounts the title within the
        specific part of the URL
        """
        filters = ['.html', '.aspx', '.ghtml', 'html', '.']
        parse = s.split('/')
        for el in reversed(parse):
            if '-' in el:
                if any(x in el for x in filters):
                    return el.split('.')[0].replace('-', ' ')
                return el.replace('-', ' ')
        return 'NULL'

    def get_title_by_url(self, url) -> str:
        """
        Verify if it is possible to get title
        directly from the URL, if it is calls
        the private method to perform the extraction
        """
        filters = ['.google','/render','/social_annotation','/start','pagina-','.jpeg','fato-ou-fake','.bmp','.png','.pdf']
        if any(s in url for s in filters):
            return 'NULL'
        title = self.__extract_title(url)
        if len(title.split(' ')) < 9:
            return 'NULL'
        return title
