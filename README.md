#Beluga Cat - an OpenAI-powered chatbot for Discord
Beluga Cat is a chatbot that can communicate with humans and provide responses to their messages. It's powered by the OpenAI API, which uses artificial intelligence to generate natural language responses.

##Getting started
To use Beluga Cat, you'll need to have a Discord account and a Discord bot token. You can get a token by following [these instructions]
(https://discordpy.readthedocs.io/en/latest/discord.html).

You'll also need to have an OpenAI account and provide your email and password in the config.py file. If you don't have an OpenAI account yet, you can sign up [here](https://beta.openai.com/signup/).

Once you have both your Discord bot token and your OpenAI credentials, you can start using Beluga Cat by running the beluga_cat.py script.

##Features
Beluga Cat responds to commands that start with the prefix /. Here are some of the available commands:

/ping: Test the bot's responsiveness.
/login <email> <password>: Log in to the OpenAI chat website.
/send <message>: Send a message to the OpenAI chat website.
/help: List available commands.
/about: Display information about the bot.
Beluga Cat can also respond to regular messages that don't start with the prefix /. In this case, it will try to generate a natural language response using the OpenAI API.

##Contributing
If you'd like to contribute to Beluga Cat, you can fork this repository and make your changes in a new branch. Once you're done, you can create a pull request and we'll review your changes.

Please make sure to follow the [Python style guide](https://www.python.org/dev/peps/pep-0008/) when writing code, and to test your changes thoroughly before submitting them.
