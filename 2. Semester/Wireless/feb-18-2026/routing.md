# Static routing over a WM 

## NAT 
network address translation protocol
when using NAT the hosts will make a request to the main host who will place mark that this request was made on behalf of someone else
and then via its arp table know there a answer to a request needs to go due to NAT and the arp table keeping track of who and what the hosts are doing

it translates the requests from the vm so they all talk over the hosts ip address and the host handles where things should go



## Host Only
its only the host that can access the internet but the vm's can talk locally between eachother meaning that only the host will ever be able to 
access the internet but it will be able to then later send data to the other hosts on the local network, the main different is that by using NAT
all your hosts will have access by using the hosts ip and then have the host forward the data to them, here only the host can send and recieve data



## Lan segments
you make a small segment of a local network which is only allowed to talk with a certain part of the network chosen by the segment settings

a lan segment doesnt have to access to the internet for the different parts of the network to be able to communicate with eachother 


## Bridged  
connects the network directly with your public ip address via your hosts dhcp making the vm's be their own divice without talking through the host pc 

some of the things that might cause problems when using a bridged could be rules set by the network you are bridging to such as if you were
making a VM and the main network doesnt allow VM's to be bridged automaticly by the DHCP due to a limmited ammount of host addresses available for the network

you would then have to make some static routing on the VM instead for it to then be bridged 

