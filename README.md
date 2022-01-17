# Twitter Bot 

Twitter Bot 

Tools and Frameworks:
- Python
- Selenium
- Twitter API
- CLI

Automatically logs in, searches for tweets from selected keywords, searches for each user’s tweet path,
and generates automated favorites, every 10 seconds. It catches the error and re-iterates after 60 seconds. - Link to GitHub

- Automatically logs in your account using selenium 
- uses TwitterBot function to log in with your credentials: username and password
- clears username and password in case there is already input in the fields before it logs in
- scrolls down the twitter feed thrice to search for tweets every 2 seconds
- searches for tweets
- searches for particulat data-perma-link for each users tweet to get particular tweet path
- interpolates twitter.com before each data-perma-link
- clicks on favorite button using class name 'HeartAnimation' 
- catches error if exception, and waits for 60 seconds before re-iteration
- 

In case of error, waits to iterate every 60 seconds.

