#!bin/bash

eog image/BigPanda.jpg &
pid=$(ps -C eog -o pid=)
echo $pid
exit 0
