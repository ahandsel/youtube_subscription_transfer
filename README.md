# youtube_subscription_transfer
* Migrate the subscriptions from a YouTube account to another with Python and [Selenium](https://www.selenium.dev/selenium-ide/)


## Credit: following code was used for this project:
* @skhzhang [/youtube_migrate.py](https://gist.github.com/skhzhang/e12195917db5f6bf8c3e6b02cd6a4af2)
* @zenwalker[/youtube_migrate.py](https://gist.github.com/zenwalker/0037fff3be1fbdb889bb)


## Step A - Download subscription_manager.xm for old & new YouTube accounts:
1. Login into the **old** YouTube acount that you want to export the subscriptions from.

2. Go to the Manage Subscriptions page: [www.youtube.com/subscription_manager](www.youtube.com/subscription_manager)

3. Scroll to the buttom to the **Export to RSS readers** section.

4. On the right, click **Export subscriptions** button.
  * The OPML file named "subscription_manager.xml" will download.

5. Rename the file as **subscription_manager-source.xml**

6. Repeate for steps 1 to 4 for your **new** YouTube account that you want to import the subscriptions into.
  * Rename the file as **subscription_manager-destination.xml**

## Step 2 - Install Python + Selenium
* Following assumes MacOS Catalina
1. Install brew | [brew.sh](https://brew.sh/)
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
```
2. Install Pyenv | [Pyenv Installation](https://github.com/pyenv/pyenv#installation)
```bash
$ brew update
$ brew install pyenv
```
* [Selenium Python Installation](https://selenium-python.readthedocs.io/installation.html)



 3  Repeat step 2 for the account you would like to import subscriptions into.
    Save the file as subscription_manager-destination.xml.

 4. Run script, manually login, and go to drink coffee.
    It will take some time.

Note YouTube will temporary block you if you have more that 80 subscriptions.
Just restart the script in a few hours.
