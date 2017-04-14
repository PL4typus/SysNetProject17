#!bin/bash

eog image/RedPanda.jpg &
pid=$(ps -C eog -o pid=)
echo $pid
exit 0
