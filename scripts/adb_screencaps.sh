file=$1

adb shell screencap -p | perl -pe 's/\x0D\x0A/\x0A/g' > $1