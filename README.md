# The "official" OS-tan Discord bot.

![ME-tan](https://raw.githubusercontent.com/SpaceboyRoss01/metan-discord/master/icon.jpg)

This bot is "derived" from an older version that was developed in JavaScript and was largely inactive since 2019 and made for an older Discord server. The current version uses Python and actually has a purpose, though the code is janky and I wouldn't trust it. The prefix for using the bot is & but can be changed in config.json.

While it is called the "OS-tan" bot it also shows information on some other characters that are not strictly called OS-tans, but fit it anyway.

Code is seriously hacked together and not intended for everyday use as it was made to test a theory :p

## Features

### bot.py and config.json

This is used for running the bot. Your bot token should be put into config.json.

### ping.py, info.py, help.py and wiki.py

Most of these don't need to be explained...

- &ping is used for pinging the bot like most other bots.
- &info gives information about the bot itself
- &help is for getting help on what each command does but doesn't work lol.
- &wiki is the main command for the bot and presents information on OS-tans and similar characters in a embed.

### os_tan_data_scraper.py and json maker.py

I actually forgot which one does which but these scripts can be used without the bot running and can be used to make character json files by extracting the character page links, extracting data from the infobox on each page and clean the unwanted bracketed text from character. You should modify the code to have a different output folder for the json files and to use a different wiki.

os_tan_data_scraper.py is really janky so maybe don't use it...

### wiki copy.py

This is an older version of wiki.py which is the script used for searching characters via the bot but instead of using a local database of json files, it attempts to rip right from the wiki itself. In theory it does work but should not be used as depending on the format for the infobox or if a page has no infobox, it will break on the embed output.

## Contributions and Removals

Contributions are welcome! If you have suggestions for improvements or new features, please feel free to submit a pull request. In regards to adding other characters you should read [this](https://github.com/Sinclair-Speccy/metan-discord/blob/master/characters/readme.md), make a pull request and meet these requirements:
 
- It must have a source such as a wiki. This is for the footer text.
- It should be an OS-tan or similar. Not all technology related characters are OS-tans but they may be exceptions for this... i.e: Nanami Madobe is more of a mascot but everyone sees her as a OS-tan because she follows the same convention as them.
- Get permission. I mean this may be a hit or miss thing but you should at least *try* to contact the creator if you can... depending on the circumstances stuff may be added without contacting first.

If you have stuff here that you would like to be removed, please please *please* make a pull request or contact me via the email on my profile so this way I have proof content was requested to be removed. If I'm going to be honest complaining and not adhering to this make you look like an ass.

## License

This project is licensed under Apache License 2.0. See the LICENSE file for details.
