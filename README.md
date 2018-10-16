# arch-update-warner
Checks Arch Linux news RSS feed and sends me an e-mail if there is an issue with a package I have installed

Reads from a config file, format is line below. Note the space between the ':' character and the rest of it, this is important for it to read correctly.

feed: {url for rss feed, e.g https://www.archlinux.org/feeds/news/}                                                                                                                                                                                                    
pkglist: {loc of a list of installed packages, e.g /home/user/pkglist}                                                                                                                                                                                                          
archive: {loc of archive file, for storing previously sent alerts to avoid duplicate emails e.g, /home/user/archive}                                                                                                                                                                                           
botemail: {mail from addr}                                                                                                                                                                                                          
myemail: {rcpt to addr}                                                                                                                                                                                                             
botpassword: {mail from pw}
