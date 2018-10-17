# arch-update-warner
Checks Arch Linux news RSS feed and sends me an e-mail if there is an issue with a package I have installed

Reads from a config file, format is line below. Note the space between the ':' character and the rest of it, this is important for it to parse the config file correctly.

feed: {url for rss feed, e.g https://www.archlinux.org/feeds/news/}                                                                                                                                                                                                    
pkglist: {location of a file documenting all installed packages, e.g /home/user/pkglist}                                                                                                                                                                                                          
archive: {location of archive file, for storing previously sent alerts to avoid duplicate emails e.g, /home/user/archive}                                                                                                                                                                                           
botemail: {sender email addr}                                                                                                                                                                                                          
myemail: {recipient email addr}                                                                                                                                                                                                             
botpassword: {sender email pw}

For pkglist, I've found the best way to get it is by the following command: 'pacman -Qqe > /path/to/file'.
