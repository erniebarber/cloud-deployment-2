"""Assignmnet 2 Part 2
Create 4 nodes and assign the OS and an IP address to each.


"""





# Import the Portal object.
import geni.portal as portal
# Import the ProtoGENI library.
import geni.rspec.pg as pg

# Create a portal context.
pc = portal.Context()

# Create a Request object to start building the RSpec.
request = pc.makeRequestRSpec()

#Set the number of Nodes:
numberofnodes = 4

#create a LAN
link = request.LAN("lan")

#Loop and create nodes.  
for i in range(1, numberofnodes + 1):
    # create and label each node
    node = request.XenVM("node-" + str(i))
    # Install the OS
    node.disk_image = "urn:publicid:IDN+emulab.net+image+emulab-ops:CENTOS7-64-STD"
    # Assign the node to the interface
    intrface = node.addInterface("if" + str(i))
    #assign the 
    intrface.component_id = "eth1" 
    #Assign an IP address to the interface
    intrface.addAddress(pg.IPv4Address("192.168.1." + str(i), "255.255.255.0"))
    #add the interface to the LAN
    link.addInterface(intrface)
    #set Node-1 to a public IP
    if i == 1:
        node.routable_control_ip = "true"

# Install and execute a script that is contained in the repository.
node.addService(pg.Execute(shell="sh", command="/local/repository/silly.sh"))

# Print the RSpec to the enclosing page.
pc.printRequestRSpec(request)
