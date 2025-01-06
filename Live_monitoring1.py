import os

# Function to create a spoofed DNS entry
def spoof_dns(domain, fake_ip):
    print("[+] Configuring DNS spoofing...")
    try:
        # Add spoofed DNS entry to the hosts file (requires root access)
        with open("/etc/hosts", "a") as hosts_file:
            hosts_file.write(f"{fake_ip} {domain}\n")
        print(f"[+] Spoofed {domain} to {fake_ip}")
    except Exception as e:
        print(f"Error: {e}")

# Function to view /etc/hosts file
def view_hosts_file():
    print("[+] Viewing current hosts file entries...")
    try:
        with open("/etc/hosts", "r") as hosts_file:
            print(hosts_file.read())
    except Exception as e:
        print(f"Error: {e}")

# Function to reset the hosts file
def reset_hosts_file():
    print("[+] Resetting hosts file...")
    try:
        os.system("cp /etc/hosts.bak /etc/hosts")
        print("[+] Hosts file reset to original state.")
    except Exception as e:
        print(f"Error: {e}")

# Main Menu
if __name__ == "__main__":
    print("""
████████████████████████████████████████████████
[+] DNS Spoofing Tool (Educational Use Only)
[+] Author: Your Name
[+] Modify DNS entries for testing (requires root)
████████████████████████████████████████████████
    """)
    print("\nChoose an option:")
    print("1. Spoof DNS Entry")
    print("2. View Hosts File")
    print("3. Reset Hosts File")
    choice = input("Enter your choice: ")

    if choice == "1":
        domain = input("Enter the domain to spoof (e.g., example.com): ")
        fake_ip = input("Enter the fake IP address (e.g., 192.168.1.100): ")
        spoof_dns(domain, fake_ip)
    elif choice == "2":
        view_hosts_file()
    elif choice == "3":
        reset_hosts_file()
    else:
        print("Invalid choice.")
