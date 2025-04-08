# ao3-chapter-counter
Outputs word counts from AO3 works chapters because its not on the pages.

It should be pretty simple to use, broadly:

```
pip install ao3_api
pip install word-count-package
./ao3-chapter-counter.py 'https://archiveofourown.org/works/xxxxxxxx/chapters/yyyyyyyy'
```

It'll take a while to establish a guest session and get the work, then you should see output like this:

```
Work ID: xxxxxxxx
Established guest session <AO3.session.GuestSession object at 0xXXXXXXXXXXXX>
<Work [Your Work Title Will Appear Here]>
Chapters: 5
chapter 1, 4781
chapter 2, 3200
chapter 3, 4348
chapter 4, 5637
chapter 5, 9739
Total 27705
```

You can grep out the `^chapter` lines, drop them in a spreadsheet and get graphs if you want.

## BUGS

Almost certainly, if you don't give it an argument it probably just blows up, etc.etc.  I wrote it quickly between jobs because I wanted to generate a graph.
