#!/usr/bin/python3


# pip install ao3_api word-count-package
import AO3
import sys
import re
import wordcount

url = sys.argv[1];
if (re.match('^https://archiveofourown.org/', url) is None):
    print(f"URL '{url}' doesn't seem to be an Ao3 URL")
    exit(1)

workid = AO3.utils.workid_from_url(url)
print(f"Work ID: {workid}")

sess = AO3.GuestSession()
print(f"Established guest session {sess}")
# sess = AO3.Session("uname", "pword")
# sess.refresh_auth_token()

try:
    work = AO3.Work(workid, sess)
    print(work)
    
    if (work is None):
        print(f"work '{work}' is broken")
        exit(1)

except AttributeError as e:
    str_err = str(e)
    if (str_err == "'NoneType' object has no attribute 'text'"):
        print(f"Ao3 said no, usually come back in like 10 minutes")
        exit(1)
    else:
        print(f"Ao3 said no in a weird way: '{str_err}'")
        exit(1)
    
    
chapters = work.nchapters
print(f"Number of Chapters: {chapters}")
total_wc = 0
chapter_wc = dict()
for i in range(0, chapters):
    # print(f"Attempting to retrieve chapter {i}/{chapters} from work {workid}")
    text = work.chapters[i].text
    c_wc_obj = wordcount.count_words_and_chars(text)
    c_wc = c_wc_obj['words']
    
    total_wc += c_wc
    chapter_wc[i] = c_wc
    print(f"chapter {i + 1}, {c_wc}")

print(f"Total {total_wc}")



