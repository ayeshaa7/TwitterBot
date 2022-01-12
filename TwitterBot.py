from selenium import webdriver
# using keyboard as input like 'enter' or typing username or password as inputs.
from selenium.webdriver.common.keys import keys
import time  # used to pause iteration after a peroid to avoid bans from twitter


class TwitterBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        # from this we can open up the page, visit the page, visit the link from firefox
        self.bot = webdriver.Firefox()

    def login(self):  # automatically logs in # self to make reference to above; #used for logging in twitter account
        bot = self.bot  # getting bot from TwitterBot
        bot.get('https://twitter.com')  # to get twitter url from firefox
        time.sleep(3)  # pause your app for 3 seconds for webpage to load up
        # webdrivers find element code is find_element_by_class_name so this finds element of class of the login input which has 'text-input email-input' this also has text-input for password input so it'll select password input also, so use email-input
        email = bot.find_element_by_class_name('email-input')
        # session[password] is the 'name' for password input
        password = bot.find_element_by_name('session[password]')
        email.clear()  # just in case there is already some input in the email input field, this clears that
        # just in case there is some input in the password input field, this clears that
        password.clear()
        # to send email input via keys to website rather than writing it manually
        email.send_keys(self.username)
        # to send password input via keys to website rather than writing it manually
        password.send_keys(self.password)
        # to return the username and password automatically
        password.send_keys(Keys.RETURN)
        time.sleep(3)  # wait for 3 seconds

    def likeTweet(self, hashtag):
        bot = self.bot  # getting the bot from TwitterBot
        # uses hashtag you enter to search up the tweets on twitter
        bot.get('https://twitter.com/search?q='+hashtag+'&src=typd')
        time.sleep(3)  # wait for 3 seconds
        # to scroll through the bot.execute_script 3 times as it scrolls only once
        for i in range(1, 3):
            # using javascripts, scrolls down, once so you need to scroll multiple times, hence the scroll loop.
            bot.execute_script(
                'window.scrollTo(0, document.body.scrollHeight)')
            time.sleep(2)
            # 'tweet' is the class name for every tweet so it searches for tweets
            tweets = bot.find_elements_by_class_name('tweet')
            # so we search tweets and we get their user path to their particular tweet so we get each link
            links = [elem.get_attribute('data-permalink-path')
                     for elem in tweets]  # for loop for each element and their data perma path

            for link in links:
                # this interpolates the perma link with twitter.com as perma link doesn't have it for each user
                bot.get('https://twitter.com/' + link)
                # try to like the tweet for each of the link (tweet) in links as its looping over each one
                try:
                    # favorite buttons class is heartanimation and clicks it
                    bot.find_element_by_class_name('HeartAnimation').click()
                    time.sleep(10)  # every 10 seconds wait
                except Exception as e:
                    # catches error and waits for 60 seconds before iterating
                    time.sleep(60)


# with username and password
ayesha = TwitterBot('ayeshafakeid@yahoo.com', 'fakepasswordfordemo')
ayesha.login()
ayesha.likeTweet('womeninstem')
