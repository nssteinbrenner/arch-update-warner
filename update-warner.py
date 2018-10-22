#!/usr/bin/env python

import feedparser
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

with open('config', 'r') as f:
    for line in f.readlines():
        if 'feed:' in line:
            targetline = line.strip().split(' ')
            feed = targetline[1]
        if 'pkglist:' in line:
            targetline = line.strip().split(' ')
            pkglist = targetline[1]
        if 'archive:' in line:
            targetline = line.strip().split(' ')
            archive = targetline[1]
        if 'botemail:' in line:
            targetline = line.strip().split(' ')
            botemail = targetline[1]
        if 'myemail:' in line:
            targetline = line.strip().split(' ')
            myemail = targetline[1]
        if 'botpassword:' in line:
            targetline = line.strip().split(' ')
            botpassword = targetline[1]


def addArchived(archive, title):
    with open(archive, 'a') as stored:
        stored.write(title)
        stored.write('\n')


def checkArchived(title, archive):
    with open(archive, 'r') as f:
        lines = f.readlines()
        for line in lines:
            if line.strip() == title:
                return False
    return True


def notifyMe(msg, subj, toaddr, fromaddr, password):
    message = MIMEMultipart()
    message['From'] = fromaddr
    message['To'] = toaddr
    message['Subject'] = subj
    message.attach(MIMEText(msg, 'plain'))
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(fromaddr, password)
    text = message.as_string()
    server.sendmail(fromaddr, toaddr, text)


def getpkgs(pkglist):
    with open(pkglist, 'r') as f:
        packages = f.readlines()
        for i, line in enumerate(packages):
            packages[i] = line.strip()
    return packages


def getposts(feed):
    updatefeed = feedparser.parse(feed)
    return updatefeed.entries


def checkpackages(packages, posts, archive):
    for post in posts:
        for package in packages:
            if checkArchived(post.title, archive):
                if package in post.title:
                    addArchived(archive, post.title)
                    fromaddr = botemail
                    toaddr = myemail
                    subj = post.title
                    msg = f'{post.link}\n\n{post.description}'
                    notifyMe(msg, subj, toaddr, fromaddr, botpassword)


packages = getpkgs(pkglist)
posts = getposts(feed)
checkpackages(packages, posts, archive)
