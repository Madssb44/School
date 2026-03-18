# Overview
today we are gonna make a relay agent, its a dhcp term that will allaw a single dhcp server to be a dhcp for 2 seperate networks

we are also gonna talk about how to set up a dhcp on a windows server, as well as how to set a scope for a dhcp

## DHCP on windows 

### Installation 
you need to have a running windows server with a static ip address and a scope and range you want to allocate

the install itself is done from a powershell terminal using the command 'Install-WindowsFeature DHCP -IncludeManagementTools'

### Authorize 
you then need to authorize the service with the following commands 

this adds the ip of the dhcp itself and a dns 'Add-DhcpServerInDC -DnsName #### -IPAddress 10.0.0.3'  

then verify it with the command 'Get-DhcpServerInDC' which should show you the information you just added

### Range & Scope 

you then need to add a scope, this done with the following commands 
'Add-DhcpServerv4Scope -Name "Name for the scope" -StartRange 10.10.10.100 -EndRange 10.10.10.200 -SubnetMask 255.255.255.0'

### Manage scopes 
you can then manage the scope with the command
'Set-DhcpServerv4OptionValue -ScopeId 192.168.15.0 -OptionId 6 -Value "192.168.15.10", "192.168.15.11"'

this command makes as scope for the 2 ips indicated in the values section and assoisiates them with the id 6

### Reserved IPs 
you can also reserve ip addresses and have them reserved for certain MAC addresses this is done with the command
'Add-DhcpServerv4Reservation -ScopeId 192.168.15.0 -IPAddress 192.168.15.100 -ClientId "00-11-22-33-44-55" 

### Exclude ranges 
you can also exclude ranges with the command
'Add-DhcpServerv4ExclutionRange -ScopeId 192.168.15.0 -StartRange 192.168.15.1 -EndRange 192.168.15.10 



## relay agent
A relay agent is a dhcp server that can forward dhcp requests from a host to a dhcp on another subnet 

### Installation & Configuring 
On linux a commonly used one is 'isc-dhcp-relay' this needs to be installed on the subnet that needs to request from somethere else
it also needs to be configured in '/etc/default/isc-dhcp-relay' it needs to know which dhcp to make requests from and which interfaces to use 

You then need the dhcp to be setup with 2 scopes, this is done by changing the config file for the dhcp in '/etc/dhcp/dhcpd.conf'
there you need to add 2 subnets, the 'main' one the dhcp is attatched to and a second one that you will give to via the relay agent 

Both require their services to be installed beforehand, 

## Scopes 

### Single/static scope 
Single or static scopes refer to a dhcp that only allocates IPs for a single subnet 

### Multicast scope 
A multicast scope allows a dhcp a allocate ip addresses over a pre configured range instead of a single subnet 


### Super scope 
A superscope is tho complete scope a dhcp can allocate to and is used as a administrative function to for very large networks


