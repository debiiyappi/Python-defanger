# Python-defanger





Just a quick lightweight Python tool I threw together to help with daily triage. It automatically converts dangerous live URLs into safe, non-clickable text formats (defanging) so I dont accidentally click a malicious link while analyzing threat campaigns.

Right now, it converts standard links like http:// or https://" into hxxp:// and hxxps://, and wraps all domain dots in [] brackets.

## Why I made this
I was tracking a malicious actor hosting fake RMM/Teams updates and got tired of manually editing strings and swapping out characters in Notepad just to safely log indicators of compromise (IoCs). 

## How it works
It's super straightforward. Run the script, drop your raw target link into the input prompt, and it will immediately spit out the clean, defanged version in your terminal.


python defang.py or python3 defang.py dont forget to install python so it works ;)


## To-do list
* [ ] Add an unfanger function to reverse the process back into live links when needed
* [ ] Drop in a continuous `while` loop so I can process multiple links in one go without restarting the script
* [ ] Add support for mass defanging IP addresses
