# EasyXCStats


EasyXCStats is an application that adds a public users most recent Strava run to XCStats

## Installation

Click main.exe and then download. You can also download credentials.txt as a template for inputting your credentials, but credentials.pickle is **necessary**. The python files are not necessary but are there for open source purposes.


## Usage

Put main.exe, credentials.txt, and credentials.pickle in the same folder.

Inside credentials.txt you should format the information like this.
```
XCStats account email
XCStats account password
Strava user id
```
Example:
```
XCStatsEmail@email.com
Password123
12345678
```
If you don't know what your Strava user id is you can follow these steps

1. Go to your own profile on a computer web browser
2. Look at the url and copy the number that is after https://www.strava.com/athletes/

So if the url is https://www.strava.com/athletes/12345678, then your user id is 12345678.

**Note that if your Strava account if private, this program will not work.** If anyone wants me to make EasyXCStats compatible with private accounts then dm me (read Contributing below).

Once you have a folder with **main.exe**, **credentials.txt**, and **credentials.pickle**, and your information in credentials.txt, run main.exe. The program will begin checking for new runs and adding them to XCStats. You can keep main.exe running in the background on your computer, or you can run it once after you finish a run.

## Contributing

You can add me on discord tatertot#2643 and dm for suggestions.

I may make this program work with private accounts, and run in the background to eliminate the manual aspect of it, but I need at least one person to dm me for me to work on it as if nobody needs it then I won't do it.
