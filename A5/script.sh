#!/bin/bash

# Server details
SERVER="172.27.26.188"
USERNAME="student"
PASSWORD="cs641"

# Group details
GROUP_NAME="enigma404"
GROUP_PASSWORD="enigma@321"
filename=$1
outfile=$2

# SSH command
/usr/bin/expect <<EOD
spawn ssh $USERNAME@$SERVER
expect "password:"
send "$PASSWORD\r"
expect "Enter your group name:"
send "$GROUP_NAME\r"
expect "Enter password:"
send "$GROUP_PASSWORD\r"
expect "at:"
send "5\r"
expect ">"
send "go\r"
expect ">"
send "wave\r"
expect ">"
send "dive\r"
expect ">"
send "go\r"
expect ">"
send "read\r"
expect ">"
set input [open "$filename" r]
set output [open "$outfile" w]
while {[gets \$input line] != -1} {
    send "\$line\r"
    expect "reads ..."
    expect -re {(\S+)}
    set output_text \$expect_out(1,string)
    puts \$output "\$output_text"
    expect ">"
    send "c\r"
    expect ">"
}
close \$input
close \$output
send "exit\r"
expect eof
EOD