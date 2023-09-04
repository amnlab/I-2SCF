import ns.core
import ns.network
import ns.point_to_point
import ns.applications
import ns.wifi
import ns.mobility
import ns.csma
import ns.internet
import sys
import subprocess

cmd = ns.core.CommandLine()
cmd.csma_node = 1
cmd.verbose = "True"
cmd.wifi_node = 1
cmd.AddValue("nCsma", "Number of \"extra\" CSMA nodes/devices")
cmd.AddValue("nWifi", "Number of wifi STA devices")
cmd.AddValue("verbose", "Tell echo applications to log if true")

cmd.Parse(sys.argv)

csma_node = int(cmd.csma_node)
verbose = cmd.verbose
wifi_node = int(cmd.wifi_node)

if wifi_node > 18:
	print ("Number of wifi nodes "+ str(wifi_node)+ " specified exceeds the mobility bounding box")
	sys.exit(1)

if verbose == "True":
	ns.core.LogComponentEnable("UdpEchoClientApplication", ns.core.LOG_LEVEL_INFO)
	ns.core.LogComponentEnable("UdpEchoServerApplication", ns.core.LOG_LEVEL_INFO)
#############################################################################################################	
p2pNodes = ns.network.NodeContainer()
p2pNodes.Create(2)

pointToPoint = ns.point_to_point.PointToPointHelper()
pointToPoint.SetDeviceAttribute("DataRate", ns.core.StringValue("100Mbps"))
pointToPoint.SetChannelAttribute("Delay", ns.core.StringValue("2ms"))

p2pDevices = pointToPoint.Install(p2pNodes)
#############################################################################################################	
wifiStaNodes = ns.network.NodeContainer()
wifiStaNodes.Create(wifi_node)
wifiApNode = p2pNodes.Get(0)

wifi = ns.wifi.WifiHelper()
wifi.SetStandard(ns.wifi.WIFI_PHY_STANDARD_80211ac);

channel = ns.wifi.YansWifiChannelHelper.Default()
phy = ns.wifi.YansWifiPhyHelper.Default()
phy.SetChannel(channel.Create())

mac = ns.wifi.WifiMacHelper()
ssid = ns.wifi.Ssid ("ns-3-ssid")

mac.SetType ("ns3::StaWifiMac", "Ssid", ns.wifi.SsidValue(ssid), "ActiveProbing", ns.core.BooleanValue(False))
staDevices = wifi.Install(phy, mac, wifiStaNodes)

mac.SetType("ns3::ApWifiMac","Ssid", ns.wifi.SsidValue (ssid))
apDevices = wifi.Install(phy, mac, wifiApNode)
#############################################################################################################
csmaNodes0 = ns.network.NodeContainer()
csmaNodes0.Create(csma_node)

csmaNodes1 = ns.network.NodeContainer()
csmaNodes1.Create(csma_node)

csmaNodes2 = ns.network.NodeContainer()
csmaNodes2.Create(csma_node)

csmaNodes3 = ns.network.NodeContainer()
csmaNodes3.Create(csma_node)

csma0 = ns.csma.CsmaHelper()
csma1 = ns.csma.CsmaHelper()
csma2 = ns.csma.CsmaHelper()
csma3 = ns.csma.CsmaHelper()
#############################################################################################################
stack = ns.internet.InternetStackHelper()
stack.Install(p2pNodes.Get(1))
stack.Install(csmaNodes0)
stack.Install(csmaNodes1)
stack.Install(csmaNodes2)
stack.Install(csmaNodes3)
stack.Install(wifiApNode)
stack.Install(wifiStaNodes)
#############################################################################################################
csmaNodes0.Add(p2pNodes.Get(1))
csma0.SetChannelAttribute("DataRate", ns.core.StringValue("100Mbps"))
csma0.SetChannelAttribute("Delay", ns.core.TimeValue(ns.core.NanoSeconds(6560)))

csmaNodes0.Add(csmaNodes1.Get(0))
csma0.SetChannelAttribute("DataRate", ns.core.StringValue("200Mbps"))
csma0.SetChannelAttribute("Delay", ns.core.TimeValue(ns.core.NanoSeconds(6560)))

csmaNodes0.Add(csmaNodes3.Get(0))
csma2.SetChannelAttribute("DataRate", ns.core.StringValue("1Mbps"))
csma2.SetChannelAttribute("Delay", ns.core.TimeValue(ns.core.NanoSeconds(6560)))

csmaDevices0 = csma0.Install(csmaNodes0)
#############################################################################################################
csmaNodes1.Add(p2pNodes.Get(1))
csma0.SetChannelAttribute("DataRate", ns.core.StringValue("100Mbps"))
csma0.SetChannelAttribute("Delay", ns.core.TimeValue(ns.core.NanoSeconds(6560)))

csmaNodes1.Add(csmaNodes2.Get(0))
csma1.SetChannelAttribute("DataRate", ns.core.StringValue("450Mbps"))
csma1.SetChannelAttribute("Delay", ns.core.TimeValue(ns.core.NanoSeconds(6560)))

csmaNodes1.Add(csmaNodes3.Get(0))
csma2.SetChannelAttribute("DataRate", ns.core.StringValue("1Mbps"))
csma2.SetChannelAttribute("Delay", ns.core.TimeValue(ns.core.NanoSeconds(6560)))

csmaDevices1 = csma1.Install(csmaNodes1)
#############################################################################################################
csmaNodes2.Add(p2pNodes.Get(1))
csma2.SetChannelAttribute("DataRate", ns.core.StringValue("100Mbps"))
csma2.SetChannelAttribute("Delay", ns.core.TimeValue(ns.core.NanoSeconds(6560)))

csmaNodes2.Add(csmaNodes3.Get(0))
csma2.SetChannelAttribute("DataRate", ns.core.StringValue("1Mbps"))
csma2.SetChannelAttribute("Delay", ns.core.TimeValue(ns.core.NanoSeconds(6560)))

csmaDevices2 = csma2.Install(csmaNodes2)
#############################################################################################################
csmaDevices3 = csma3.Install(csmaNodes3)
#############################################################################################################
information = [["csmaTier0", 200, "x", 50, 100, 10], 
               ["csmaTier1", 200, 450, 50, 100, 15], 
               ["csmaTier2", "x", 450, 50, 100, 60]]
csmaTier0_info = [["csmaNode0" ,350, 9],["csmaNode1", 350, 10]]
csmaTier1_info = [["csmaNode0" ,350, 14],["csmaNode1", 350, 15]]
csmaTier2_info = [["csmaNode0" ,350, 59],["csmaNode1", 350, 60]]
                
#############################################################################################################
mobility = ns.mobility.MobilityHelper()
mobility.SetPositionAllocator ("ns3::GridPositionAllocator", 
                               "MinX", ns.core.DoubleValue(0.0), 
                               "MinY", ns.core.DoubleValue (0.0), 
                               "DeltaX", ns.core.DoubleValue(5.0), 
                               "DeltaY", ns.core.DoubleValue(10.0), 
                               "GridWidth", ns.core.UintegerValue(1), 
                               "LayoutType", ns.core.StringValue("RowFirst"))
                                 
mobility.SetMobilityModel ("ns3::RandomWalk2dMobilityModel", 
                           "Bounds", ns.mobility.RectangleValue(ns.mobility.Rectangle (0, 0, 0, 0)))
mobility.Install(wifiStaNodes)

mobility.SetMobilityModel("ns3::ConstantPositionMobilityModel")
mobility.Install(wifiApNode)
#############################################################################################################
address = ns.internet.Ipv4AddressHelper()
address.SetBase(ns.network.Ipv4Address("10.1.1.0"), ns.network.Ipv4Mask("255.255.255.0"))
p2pInterfaces = address.Assign(p2pDevices)

address.SetBase(ns.network.Ipv4Address("10.1.2.0"), ns.network.Ipv4Mask("255.255.255.0"))
csmaInterfaces0 = address.Assign(csmaDevices0)

address.SetBase(ns.network.Ipv4Address("10.1.3.0"), ns.network.Ipv4Mask("255.255.255.0"))
csmaInterfaces1 = address.Assign(csmaDevices1)

address.SetBase(ns.network.Ipv4Address("10.1.4.0"), ns.network.Ipv4Mask("255.255.255.0"))
csmaInterfaces2 = address.Assign(csmaDevices2)

address.SetBase(ns.network.Ipv4Address("10.1.5.0"), ns.network.Ipv4Mask("255.255.255.0"))
csmaInterfaces3 = address.Assign(csmaDevices3)

address.SetBase(ns.network.Ipv4Address("10.1.6.0"), ns.network.Ipv4Mask("255.255.255.0"))
address.Assign(staDevices)
address.Assign(apDevices)
#############################################################################################################
echoServer = ns.applications.UdpEchoServerHelper(9)

serverApp0 = echoServer.Install(csmaNodes0.Get(0))
serverApp0.Start(ns.core.Seconds(1.0))
serverApp0.Stop(ns.core.Seconds(10.0))

serverApp1 = echoServer.Install(csmaNodes1.Get(0))
serverApp1.Start(ns.core.Seconds(1.0))
serverApp1.Stop(ns.core.Seconds(10.0))

serverApp2 = echoServer.Install(csmaNodes2.Get(0))
serverApp2.Start(ns.core.Seconds(1.0))
serverApp2.Stop(ns.core.Seconds(10.0))

serverApp3 = echoServer.Install(csmaNodes3.Get(0))
serverApp3.Start(ns.core.Seconds(1.0))
serverApp3.Stop(ns.core.Seconds(10.0))



echoClient0 = ns.applications.UdpEchoClientHelper(csmaInterfaces3.GetAddress(0), 9)
echoClient0.SetAttribute("MaxPackets", ns.core.UintegerValue(1))
echoClient0.SetAttribute("Interval", ns.core.TimeValue(ns.core.Seconds (1.0)))
echoClient0.SetAttribute("PacketSize", ns.core.UintegerValue(1024))

clientApps0 = echoClient0.Install(wifiStaNodes.Get (wifi_node - 1))
clientApps0.Start(ns.core.Seconds(2.0))
clientApps0.Stop(ns.core.Seconds(10.0))

ns.internet.Ipv4GlobalRoutingHelper.PopulateRoutingTables()

ns.core.Simulator.Stop(ns.core.Seconds(10.0))
#############################################################################################################

