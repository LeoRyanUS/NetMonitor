from scapy.all import sniff
import sys
import time
import os
import subprocess

# Colors for terminal output
class Colors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    RESET = '\033[0m'

packet_count = 0

def packet_callback(packet):
    global packet_count
    packet_count += 1
    if packet.haslayer("IP"):
        ip_src = packet["IP"].src
        ip_dst = packet["IP"].dst
        print(f"{Colors.GREEN}Packet count: {packet_count}{Colors.RESET}")
        print(f"{Colors.YELLOW}Source IP: {ip_src}  --->  Destination IP: {ip_dst}{Colors.RESET}")
        print(f"Arrival Time: {time.strftime('%Y-%m-%d %H:%M:%S')}")

def net_monitor_info():
    print(f"{Colors.GREEN}")
    print("""
  _   _      _   __  __             _ _             
 | \ | |    | | |  \/  |           (_) |            
 |  \| | ___| |_| \  / | ___  _ __  _| |_ ___  _ __ 
 | . ` |/ _ \ __| |\/| |/ _ \| '_ \| | __/ _ \| '__|
 | |\  |  __/ |_| |  | | (_) | | | | | || (_) | |   
 |_| \_|\___|\__|_|  |_|\___/|_| |_|_|\__\___/|_|   
                By Leo Ryan
     All Social Network User name (LeoRyanUS)  
           Email:LeoRyanUS@gmail.com                                          
                                                    
""")
    print(f"{Colors.RESET}")
    print("\nWelcome to NetMonitor!")
    print("Please enter the IP address you want to monitor:")
    ip_address = input("IP address: ")
    return ip_address

def show_options():
    print("\nChoose an option:")
    print("1. Monitor all network traffic")
    print("2. Monitor traffic to/from a specific IP address")
    print("3. Email notifications")
    print("4. Record network traffic to file")
    print("5. Filter by port")
    print("6. Configure network security")
    print("7. Network device information")
    print("8. Analyze network traffic")
    print("9. View network traffic statistics")
    print("10. Add a new feature")
    print("11. Exit")

def start_monitoring(ip_address=None):
    while True:
        show_options()
        option = get_user_option()
        if option == 1:
            print("Monitoring all network traffic...")
            sniff(prn=packet_callback, store=False)
        elif option == 2:
            if not ip_address:
                ip_address = get_user_ip()
            print(f"Monitoring traffic to/from {ip_address}...")
            sniff(filter=f"host {ip_address}", prn=packet_callback, store=False)
        elif option == 3:
            print("Email notifications enabled.")
            # Add code for email notifications
        elif option == 4:
            filename = input("Enter the filename to save network traffic: ")
            print(f"Recording network traffic to {filename}...")
            # Add code to record network traffic to file
        elif option == 5:
            port = input("Enter the port number to filter: ")
            print(f"Filtering network traffic by port {port}...")
            # Add code to filter network traffic by port
        elif option == 6:
            print("Network security configured.")
            # Add code for network security configuration
        elif option == 7:
            print("Network device information:")
            os.system("ifconfig")  # Run ifconfig command to display network device information
        elif option == 8:
            print("Starting network analysis...")
            packet_analysis()
        elif option == 9:
            print("Starting traffic statistics...")
            packet_statistics()
        elif option == 10:
            print("Adding a new feature...")
            # Add code for new feature
        elif option == 11:
            print("Exiting...")
            sys.exit()
        else:
            print(f"{Colors.RED}Invalid option. Please try again.{Colors.RESET}")

def packet_analysis():
    print("Starting network analysis...")
    sniff(prn=packet_callback, store=False)

def packet_statistics():
    print("Starting traffic statistics...")
    sniff(prn=packet_callback, store=False)

def get_user_option():
    try:
        option = int(input("Enter your choice: "))
        return option
    except ValueError:
        print(f"{Colors.RED}Invalid input. Please enter a number.{Colors.RESET}")
        return get_user_option()

def get_user_ip():
    ip_address = input("Please enter the IP address you want to monitor: ")
    return ip_address

if __name__ == '__main__':
    ip_address = net_monitor_info()
    start_monitoring(ip_address)
