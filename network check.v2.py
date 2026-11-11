
def network_check():
    import psutil
    import socket
    import logging
    logging.basicConfig(
        filename="network_check.log",
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )


    stats = psutil.net_if_stats()

    interfaces = psutil.net_if_addrs()
    io = psutil.net_io_counters(pernic=True)

    for interface_name, stat in stats.items():
        print(interface_name, stat.isup)

    interface_to_check = input("enter interface name: ")



    while interface_to_check not in stats:
        print(f"Interface selected does not exist: {interface_to_check}")
        logging.info("Interface selected: %s", interface_to_check)
        interface_to_check = input("enter interface name: ")



    for interface_name, data in io.items():
        if interface_name == interface_to_check:
            print("Bytes sent:", data.bytes_sent)
            print("Bytes received:", data.bytes_recv)

    for interface_name, addresses in interfaces.items():

            if interface_name == interface_to_check:
                for address in addresses:
                    if address.family == socket.AF_INET:
                        print("IPV4:", address.address)
                        logging.info("IPV4: %s", address.address)


                    if address.family == psutil.AF_LINK:
                        print("MAC:", address.address)

    for interface_name, stat in stats.items():
        if interface_name == interface_to_check:
            print("SPEED:", stat.speed)
            print("MTU:", stat.mtu)
            print("Duplex:", stat.duplex)



network_check()
input("Press Enter to exit")




