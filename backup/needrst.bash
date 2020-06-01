#!/bin/bash
# Developer : Hamdy Abou El Anein
# hamdy.aea@protonmail.com

currentDate=$(date +"%D %T")
echo $currentDate > /root/aide_result
needs-restarting -r >> /root/aide_result
printf "\n\n">> /root/aide_result
