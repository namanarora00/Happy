# Happy

A chatbot is a software that is used to interact between a computer and a human in 
natural language like humans chat. Chatbots chat with the user in a conversation in place 
of a human and reply to the user. This goal of this chat bot is to help cope up with 
depression or sadness by talking to the user about the things that are bothering 
him / her and if possible provide him with some sort of solution as well like telling some jokes or talking more about things that the user is positive about. The bot is made using the 
Telegram bot API for python3. For processing messages and semantic analysis nltk 
library is used. Pre-existing data sets and trained models are for classifications.

### Installation

Install Python3 and pip. Install pipenv using pip. Then run the following command in the root directory.

```bash
pipenv install
```

### Running the server

Before continuing make sure to get the Bot API key from telegram. Make sure that you have a working internet connection.

* Add the api key environment variables by running the following command.
  ```bash
  export API_TELEGRAM={API_KEY}
  ```
  Make sure that it is set successfully by running this command
  ```bash
  env | grep API_TELEGRAM
  ```

* After you've added the API key, run the following commmand
    ```bash
    pipenv run python3 server.py
    ```

    Then go to the telegram app on phone or desktop and start talking to the Bot.


### Team
* Naman Arora
* Lovedeep Singh Sidhu