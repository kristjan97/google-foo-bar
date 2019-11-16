# google-foo-bar

**Google Foo Bar** is a bot that will automate the process of getting an invitation for the Google foo bar challenge.
It opens a Chrome driver that will scrape 100 questions submitted to Stackoverflow and querry them into Google.
Each querry will be checked for the Google foo bar challenge invitation.

This bot requires permission to take screenshots of your screen and control mouse movements.

Created by: **Kristjan von Bulow**

## User Stories

The following features are implemented:
* [x] Bot querrys multiple computer science related questions/topics until the google foo bar challenge invitation appears.

The following **optional** features are implemented:
* [x] Automate normal user interaction by scrolling page up and down.
* [ ] Allow user to log into Google account before the bot will automate searching.
* [x] Allow driver to scrape more questions from stackoverflow API


## Notes

Need more information on how the Google foo bar challenge invitation appears. If you have more information on how it works/appears,
please contact me at kristjanvonbulow@gmail.com

- I also think that perhaps Google is using their ad personalization module to target people and give them an invitation. What this means is that you cannot run this program without logging into a Google account, also I believe you cannot run this program if you set strict privacy settings on your Google account. 

## License

    Copyright [2019] [Kristjan von Bulow]

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0
