# Relay agent
today we are gonna make a relay agent, its a dhcp term that will allaw a single dhcp server to be a dhcp for 2 seperate networks

## Cooperative learning task
 
what and why. 

a dhcp is a service that allocates ip addresses, dns and gateways from a avaliable pool




dhcp on windows

you need to have a running windows server with a static ip address and a scope and range you want to allocate

the install itself is done from a powershell terminal using the command 'Install-WindowsFeature DHCP -IncludeManagementTools'

you then need to authorize the service with the following commands 

this adds the ip of the dhcp itself and a dns 'Add-DhcpServerInDC -DnsName #### -IPAddress 10.0.0.3'  

then verify it with the command 'Get-DhcpServerInDC' which should show you the information you just added


you then need to add a scope, this done with the following commands 
'Add-DhcpServerv4Scope -Name "Name for the scope" -StartRange 10.10.10.100 -EndRange 10.10.10.200 -SubnetMask 255.255.255.0'


you can then manage the scope with the command
'Set-DhcpServerv4OptionValue -ScopeId 192.168.15.0 -OptionId 6 -Value "192.168.15.10", "192.168.15.11"'

this command makes as scope for the 2 ips indicated in the values section and assoisiates them with the id 6

you can also reserve ip addresses and have them reserved for certain MAC addresses this is done with the command
'Add-DhcpServerv4Reservation -ScopeId 192.168.15.0 -IPAddress 192.168.15.100 -ClientId "00-11-22-33-44-55" 


you can also exclude ranges with the command
'Add-DhcpServerv4ExclutionRange -ScopeId 192.168.15.0 -StartRange 192.168.15.1 -EndRange 192.168.15.10 



what is a relay agent

a relay agent is a intermediary dhcp server that allows a dhcp that isnt part of your subnet to allocate ip addresses to you and others
without having to be on the same subnet as the dhcp itself,

It does require a seperate dhcp server to be installed on the subnet you want to allocate to as well an one on the subnet you want to allocate form
sa well as the dhcp you want to allocate form being configured to set scopes for remote subnets


what is multicast scope 
multicast scope works by assigning a single unique ip address from a range you set out the individual dhcp servers
they can then allocate them out to their hosts


what is superscope

A superscope is an administrative feature that allows a single dhcp to allocate ip addresse for multiple supnets within the same network


