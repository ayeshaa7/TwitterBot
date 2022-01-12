# Twitter Bot (python)

This Twitter Bot automatically logins in your Twitter account, searches queries, here 'womeninstem', selects each tweet in the search result and favorites the tweet every 10 seconds--to avoid ban.

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

