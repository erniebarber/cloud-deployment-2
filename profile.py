# Import the Portal object.
import geni.portal as portal
# Import the ProtoGENI library.
import geni.rspec.pg as pg

# Create a portal context.
pc = portal.Context()

# Create a Request object to start building the RSpec.
request = pc.makeRequestRSpec()

#Set the number of Nodes:
int numberofnodes = 4

#create a LAN
link = request.LAN("lan")

#Loop and create nodes
for i in range(numberofnodes):
    node = request.XenVM("node" + str(i))
    node.disk_image = "urn:publicid:IDN+emulab.net+image+emulab-ops:CENTOS7-64-STD"
    intrface = node.addInterface("if" + str(i))
    intrface.component_id = "eth1"
    intrface.addAddress(rspec.IPv4Address("192.168.1." + str(i)))
    link.addInterface(intrface)
    #set Node 0 to a public IP
    if node == 0 
     node.routable_control_ip = True

# Install and execute a script that is contained in the repository.
node.addService(pg.Execute(shell="sh", command="/local/repository/silly.sh"))

# Print the RSpec to the enclosing page.
pc.printRequestRSpec(request)
