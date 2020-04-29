# youtube_subscription_transfer
* Migrate the subscriptions from a YouTube account to another with Python and [Selenium](https://www.selenium.dev/selenium-ide/)


## Credit: following code was used for this project:
* @skhzhang [/youtube_migrate.py](https://gist.github.com/skhzhang/e12195917db5f6bf8c3e6b02cd6a4af2)
* @zenwalker[/youtube_migrate.py](https://gist.github.com/zenwalker/0037fff3be1fbdb889bb)


## Step 1 - Download subscription_manager.xm
* Login into the old YouTube acount
  * *that you want to export the subscriptions from*
* Go to the Manage Subscriptions page: [www.youtube.com/subscription_manager](www.youtube.com/subscription_manager)
* Scroll to the buttom to the **Export to RSS readers** section.
* On the right, click **Export subscriptions** button.
  * The OPML file named "subscription_manager.xml" will download.

## Step 2 - Install selenium from pypi: