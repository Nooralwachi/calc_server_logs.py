# calc_server_logs.py


You are given a large number of logs with contents like this:

...

s1.yaboo.com 12:23:00 10/15/2020 0.55 0.75 0.65

s1.yaboo.com 12:24:00 10/15/2020 0.45 0.80 0.66 

s1.yaboo.com 12:25:00 10/15/2020 0.80 0.80 0.66 

s1.yaboo.com 12:26:00 10/15/2020 0.85 0.86 0.87 

s1.yaboo.com 12:27:00 10/15/2020 0.86 0.79 0.67 

s1.yaboo.com 12:28:00 10/15/2020 0.76 0.79 0.87

s1.yaboo.com 12:29:00 10/15/2020 0.86 0.89 0.87

s1.yaboo.com 12:30:00 10/15/2020 0.86 0.89 0.87

s1.yaboo.com 12:31:00 10/15/2020 0.86 0.89 0.67

s1.yaboo.com 12:32:00 10/15/2020 0.86 0.79 0.67

...
 
Note:

1) each log only content the info a single server

2) the last three columns are CPU load %, RAM load %, Disk used % respectively

 
Please write a function to detect if any load is >= 80% for two consecutive minutes and print out a warning message.

The message should look like "Warning: server s1.yaboo.com CPU load is over 80% from 12:25:00 10/15/2020 to 12:27:00 10/15/2020"
