# youtube_subscription_transfer
* Migrate the subscriptions from a YouTube account to another with Python and [Selenium](https://www.selenium.dev/selenium-ide/)


## Credit: following code was used for this project:
* @skhzhang [/youtube_migrate.py](https://gist.github.com/skhzhang/e12195917db5f6bf8c3e6b02cd6a4af2)
* @zenwalker[/youtube_migrate.py](https://gist.github.com/zenwalker/0037fff3be1fbdb889bb)


## Step A - Download subscription_manager.xm for old & new YouTube accounts:
1. Login into the **old** YouTube acount that you want to export the subscriptions from.

2. Go to the Manage Subscriptions page: [www.youtube.com/subscription_manager](https://www.youtube.com/subscription_manager)

3. Scroll to the buttom to the **Export to RSS readers** section.

4. On the right, click **Export subscriptions** button.
  * The OPML file named "subscription_manager.xml" will download.

5. Rename the file as **subscription_manager-source.xml**

6. Repeate for steps 1 to 4 for your **new** YouTube account that you want to import the subscriptions into.
  * Rename the file as **subscription_manager-destination.xml**

## Step B - Install pyenv & Python
* Following assumes MacOS Catalina
1. Install brew | [brew.sh](https://brew.sh/)
    ```bash
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
    ```

2. Install pyenv | [pyenv Installation](https://github.com/pyenv/pyenv#installation)
    ```bash
    brew update
    brew install pyenv
    brew install openssl readline sqlite3 xz zlib
    ```
    * Add `pyenv init` to your shell to enable shims and autocompletion.
      * Please make sure eval "$(pyenv init -)" is placed toward the end of the shell configuration file since it manipulates PATH during the initialization.
    * For bash:
    ```bash
    echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bash_profile
    ```
    * For zsh:
    ```zsh
    echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.zshrc
    ```
    * Restart your shell so the path changes take effect. You can now begin using pyenv.
    ```bash
    exec "$SHELL"
    ```

3. Install Python using pyenv
    * Quick list of pyenv commands:

    | pyenv commands | action |
    |--|--|
    | `pyenv install --list` | lists out the python versions |
    | `pyenv install <version>` | Installs the selected version |
    | `pyenv versions` | lists out all installed versions|
    |  `pyenv global <version>` | Set the global or default python version |
    | `pyenv local <version>` | Set the local version by cd'ing into the repo then.. |
    | `python --version` | Check current python version |

    * Install [python](https://www.python.org/downloads/) version 3.8.2 and set as the default version
    ```bash
    pyenv install 3.8.2
    pyenv global 3.8.2
    ```

## Step C - Install Selenium
  * [Selenium Python Installation](https://selenium-python.readthedocs.io/installation.html)
  1. Update pip (you already installed pip when you installed Python version >= 3.4)
      ```bash
      pip install --upgrade pip
      ```
  2. Downloading Python bindings for Selenium
      ```bash
      pip install selenium
      ```

## Step D - Install FireFox's geckodriver
  * [geckodriver/releases](https://github.com/mozilla/geckodriver/releases)
  * Selenium requires a driver to interface with a browser in your PATH (/usr/bin or /usr/local/bin)
    * Firefox broswer --> requires GeckoDriver driver
  1. Under [**Assets**](https://github.com/mozilla/geckodriver/releases), install the geckodriver-v0.26.0-macos.tar.gz
  2. Then running the following command to address the [MacOS Notarization](https://firefox-source-docs.mozilla.org/testing/geckodriver/Notarization.html) known problem:
     * `  xattr -r -d com.apple.quarantine geckodriver-v0.26.0-macos.tar.gz`
  3. Run the following in your terminal
       * `sudo nano /etc/paths`
  4. Insert the path to the geckodriver download at the bottom of the file
    * My PATH is: /Users/beta/Downloads/geckodriver
    * `control`+`x` to quit
    * `y` to save
    * return to confirm
    * Confirming New PATH: relaunch Terminal and run
      * `echo $PATH`
    * Your path to geckodriver should be included in the output
  5. Geckodriver executable needs to be in PATH
     * `sudo cp geckodriver /usr/local/bin`
  6. Install [Firefox](https://www.mozilla.org/en-US/firefox/new/)
    * Firefox 76.0 is used

## Step E - Place the three files in one folder
  * youtube_migrate.py
  * subscription_manager-**source**.xml
  * subscription_manager-***destination***.xml

## Step F - Run script, manually login, and go to drink coffee.
  * It will take some time.
  * Note YouTube will temporary block you if you have more that 80 subscriptions.
  * Just restart the script in a few hours.

## ERROR: selenium.common.exceptions.WebDriverException: Message: 'geckodriver' executable needs to be in PATH.
* cd to the folder with the geckodriver and run the following command: `sudo cp geckodriver /usr/local/bin`


## References used:
* [Running selenium on MacOS using chromedriver](https://medium.com/@KelvinMwinuka/running-selenium-on-macos-using-chromedriver-96ef851282b5)
* [Code documentation on selenium-python](https://selenium-python.readthedocs.io/)
* [Set up Selenium & GeckoDriver \(Mac\)](https://medium.com/dropout-analytics/selenium-and-geckodriver-on-mac-b411dbfe61bc)
* [The Python virtual environment with Pyenv & Pipenv](https://dev.to/writingcode/the-python-virtual-environment-with-pyenv-pipenv-3mlo)
* [How to install and Set up Python on Mac](https://dev.to/brohittv/how-to-install-and-set-up-python-on-mac-29fd?signin=true)
* [Python Development on macOS with pyenv](https://medium.com/python-every-day/python-development-on-macos-with-pyenv-2509c694a808)

https://addons.mozilla.org/en-GB/firefox/addon/selenium-ide/


export PATH=$PATH:/path/to/directory/of/executable/downloaded/in/previous/step

