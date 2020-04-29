"""
Automatic migration of subscriptions to another
YouTube account with Python and Selenium.

Tested with:
 - selenium 3.0
 - firefox 49.0
 - python 3.5

 1. Install selenium from pypi:
    $ pip install selenium

 2. Go to the down of page https://www.youtube.com/subscription_manager
    and download your current subscriptions feed.
    Save file as subscription_manager-source.xml.

 3  Repeat step 2 for the account you would like to import subscriptions into.
    Save the file as subscription_manager-destination.xml.

 4. Run script, manually login, and go to drink coffee.
    It will take some time.

Note YouTube will temporary block you if you have more that 80 subscriptions.
Just restart the script in a few hours.
"""

from collections import namedtuple
from selenium import webdriver
from selenium.common.exceptions import ElementNotInteractableException
from xml.dom import minidom
import time
import re


def main():

    notYetSubscribed = list(set(load_subcriptions('subscription_manager-source.xml')) - set(load_subcriptions('subscription_manager.xml')))

    driver = webdriver.Firefox()
    sign_in(driver)
    for channel in notYetSubscribed:
        subscribe(driver, channel)
    driver.close()


def sign_in(driver):
    driver.get('https://www.youtube.com')

    input('Please login. Press enter after: ')
    time.sleep(1)


def load_subcriptions(filename):
    xmldoc = minidom.parse(filename)
    itemlist = xmldoc.getElementsByTagName('outline')
    channel_id_regexp = re.compile('channel_id=(.*)$')
    Channel = namedtuple('Channel', ['id', 'title'])
    subscriptions = []

    for item in itemlist:
        try:
            feed_url = item.attributes['xmlUrl'].value
            channel = Channel(id=channel_id_regexp.findall(feed_url)[0],
                              title=item.attributes['title'].value)
            subscriptions.append(channel)
        except KeyError:
            pass

    return subscriptions


def subscribe(driver, channel):
    channel_url = 'https://www.youtube.com/channel/' + channel.id
    driver.get(channel_url)
    time.sleep(1)

    try:
        button = driver.find_element_by_id('subscribe-button')

        button.click()
        print('{:.<50}{}'.format(channel.title, 'done'))
        time.sleep(1)

    except ElementNotInteractableException as error:
        # cannot scroll button into view
        print('{:.<50}{}'.format(channel.title, 'error'))
        print(error)
        input('Press enter to proceed: ')
        time.sleep(1)

if __name__ == '__main__':
    main()