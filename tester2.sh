#!/bin/sh

a=0

until [ $a -gt 10 ]
do
   python3 repetition_removal_scipt.py | python3 testScriptForRepetitionFile.py
   echo 
   a=`expr $a + 1`
done
