import wireless
import


nic = wireless.Wireless(interface='wlp2s0')
nx_name = ''
if nic.current().title() !='':
    nx_name = nic.current().title().upper()
else:
    nic.connect(input('Enter SSID:',input('Enter Password')))
