#!/bin/bash

set -eu
# set -x

echo "Generating vim startup profile..."
logfile="vim.log"

if [ -f $logfile ]; then
    # clear the log file first
    rm $logfile
    echo foo
fi

if [[ $# -eq 0 ]]; then
    nvim --startuptime $logfile -c q
else
    nvim --startuptime $logfile $1
fi


plugDir="$HOME/.local/share/nvim/site/pack/packer/start/"

if [[ -d "$plugDir" ]]; then
    echo "packer plugin dir has been detected."
else
    echo "packer dir not found."
    exit 1
fi


grep_str="packer/start"
echo "Parsing vim startup profile..."
grep $grep_str $logfile > tmp.log
awk -F\: '{print $1}' tmp.log > tmp1.log
echo "packer/start" | awk -F'/' '{print $NF}' tmp.log > tmp2.log
paste -d ',' tmp1.log tmp2.log | tr -s ' ' ',' > ./data/profile.csv
rm tmp.log tmp1.log tmp2.log $logfile


python3 neovim_startup-time.py

cat <<EOF
charts have been saved
*-----------------------------------------------*
| Top 10 Plugins That Slows Down neovim Startup |
*-----------------------------------------------*

$(cat -n ./data/results.csv | head -n 10 | tr "," "\t" | column -t) 

*-----------------------------------------------* 
Done!
EOF

