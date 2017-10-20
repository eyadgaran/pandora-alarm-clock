'''Functions to control echo player (pandora)'''
from selenium import webdriver
from packaged_scripts.selenium.webelements import XPathElements,\
    XPathSlider, XPathElement
from secrets import USERNAME, PASSWORD
import time
from os.path import join, split, abspath

PROJECT_PATH = split(split(abspath(__file__))[0])[0]
CHROMEDRIVER_PATH = join(PROJECT_PATH, "env/chromedriver")
OPTIONS = webdriver.ChromeOptions()
OPTIONS.add_argument("--headless")
# OPTIONS.binary_location = '/opt/google/chrome/google-chrome'
SERVICE_LOG_PATH = join(PROJECT_PATH, "logs/chromedriver.log")
SERVICE_ARGS = ['--verbose']


class EchoPlayer(object):
    '''Class to control echo player using selenium'''
    def __init__(self, station):
        self.station = station
        self.initialize()

        # Volume Configs
        self.max_volume = 3
        self.volume_increment = 0.1

    def initialize(self):
        # Initialize driver
        self.driver = webdriver.Chrome(
            executable_path=CHROMEDRIVER_PATH,
            chrome_options=OPTIONS,
            service_args=SERVICE_ARGS,
            service_log_path=SERVICE_LOG_PATH)

        # Navigate to webplayer
        login_url = 'https://alexa.amazon.com'
        self.driver.get(login_url)

        # Sign In
        self.driver.find_element_by_css_selector('#ap_email').send_keys(USERNAME)
        self.driver.find_element_by_css_selector('#ap_password').send_keys(PASSWORD)
        self.driver.find_element_by_css_selector('#signInSubmit').click()

        # Open Pandora
        self.pandora_url = 'https://alexa.amazon.com/spa/index.html#music/PANDORA'
        self.driver.get(self.pandora_url)

        # Map Stations
        station_xpath = "Radio"
        self.station_elements = XPathElements(self.driver, station_xpath)

        # # Start the initial station
        # self.change_station(self.station)
        #
        # # Start by zeroing out volume
        # self.zero_volume()

    def zero_volume(self):
        # Navigate to the player page to control playback
        self.player_url = 'https://alexa.amazon.com/spa/index.html#player'
        self.driver.get(self.player_url)
        time.sleep(2)
        volume_locator = ''
        self.volume_element = XPathSlider(self.driver, volume_locator)
        self.current_volume = 0

    def change_station(self, station):
        self.station = station

        # Navigate to the station page
        self.driver.get(self.pandora_url)

        # Wait until the station list loads
        max_wait = 15
        wait = 0
        while wait < max_wait:
            # Play station
            stations = self.station_elements.element_map
            wait += 1
            time.sleep(1)
            if self.station in stations:
                break

        # default to clickable object to avoid failure
        stations.get(self.station, stations['default']).click()

    def increase_volume(self):
        if self.current_volume < self.max_volume:
            self.current_volume += self.volume_increment

    def play(self):
        pass

    def close(self):
        self.driver.close()


if __name__ == '__main__':
    station_map = [
        ('Mythos Radio', 30),
        ('Lindsey Stirling Radio', 15),
        ("Today's Hip Hop and Pop Hits Radio", .5)
    ]

    player = EchoPlayer(station_map[0][0])

    for station, wait_time in station_map:
        player.change_station(station)
        if wait_time:
            time.sleep(60 * wait_time)

    player.close()
