# Firewalls 

## what is a Firewall?

it needs at least 2 interfaces as to create a inside and outside

it needs to be autherized trafic that passes throught it 

it needs to have rules in order to determine what to filter out 

the firewall needs to be immune itself 

## what does it do?
It sorts good and bad data to only allow the good data/requests to go throught 

### Service Control
service, addresses, protocols, prots

### Direction Control 
is trafic going in or out? Who started the connection?

### User Control 
Controls access based on users, such as a admin or normal user 

### Behavior Control
What kind of content is avaliable? where are trafic going and what is happening?


## How does it react 

### Drop
it doesn't allow the packet to go throught and doesn't let the person who sent it know it was dropped 

### Deny
lets the sender know that the packet was dropped 

### Permit
allows the packet to pass throught


## How does it analize trafic?
It reads and analizes packets, it then reads all the content and where its going, what its doing, who send it, what they want and so on 


## DMZ 
De militrized zone

a zone with less strict rules allowing special kinds of trafic to pass throught to somethere depending on the requests

## Different kinds/types

### Packet filtering 
The most simple firewall type that goes throught packets and looks throught the rules, meaning that more spread out attacks will cause it problems

### Stateful inspection
can do the same as the packet filtering type but also sessions and data, its one of the most common types of firewalls and the one that is used in home networks

### Application proxy 
a specilized firewall made to only look at 1 type of trafic tailered to the application its made for

### Guard
looks at the full context of the communication 

### Personal filtering 
Personal protection used for device protection, such as windows defender


## Terms 
NACK = Negative acknowledgement


# Defence in Depth
an old militery strategy 

more time to detect attackers and more time to react and watch what they are doing


