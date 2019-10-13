ps aux | grep wush60309 | grep mainsec | grep -v grep | awk '{print $2}' | xargs kill
