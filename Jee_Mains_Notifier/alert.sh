#!/bin/bash

cd /root/Programs/Jee_Mains_Notifier/

SCRAPE()
{
	python3 scraper.py > "$1"
}
COMPARE()
{
	shafirstScrape=$(shasum firstScrape | awk '{ print $1 }')
	shasecondScrape=$(shasum secondScrape | awk '{ print $1 }')
	if [ "$shafirstScrape" != "$shasecondScrape" ]
	then
		echo "change detected."
		diff secondScrape firstScrape > DIFF.txt
		mv secondScrape firstScrape
		echo "Running notify script!"
		python3 notify.py
		rm DIFF.txt
	else
		echo "No change detected"
		# as there are no changes lets just nuke secondScrape.
		rm secondScrape
	fi
}



main()
{
	if [ -f firstScrape ]
	then
		SCRAPE secondScrape
	else
		SCRAPE firstScrape
		SCRAPE secondScrape
	fi
	COMPARE
}
main
