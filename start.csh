#! /bin/tcsh
while(1)
	set a = `ps aux | grep wush | grep python | grep mainsec`
	if ( $#a > 1 ) then
		kill $a[2]
	endif
	python3 mainsec.py &
	echo "rebooted at `date`"
	sleep 3600
#	sleep 604800
end
