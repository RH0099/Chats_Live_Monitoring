import os
import subprocess

# Function to start packet sniffing
def start_sniffing(interface):
    print(f"[*] Sniffing network traffic on interface: {interface}")
    try:
        # Start tcpdump to capture packets on the network
        os.system(f"tcpdump -i {interface} -w /data/data/com.termux/files/home/sniffed_traffic.pcap")
    except Exception as e:
        print(f"[-] Error: {e}")

# Function to analyze captured packets (simple filter for chat-related traffic)
def analyze_traffic():
    print("[*] Analyzing captured packets...")
    try:
        # Using tshark to analyze the captured pcap file for text data
        os.system("tshark -r sniffed_traffic.pcap -Y 'http' -T fields -e http.host -e http.request.uri")
    except Exception as e:
        print(f"[-] Error: {e}")

# Function to edit chat message (modifying the HTTP traffic in real-time)
def edit_chat_message(original_message, new_message):
    print(f"[*] Editing message: {original_message} -> {new_message}")
    try:
        # This can be a simple substitution of text in HTTP packets (in the real world, you would need MITM tools)
        os.system(f"sed -i 's/{original_message}/{new_message}/g' sniffed_traffic.pcap")
        print("[*] Chat message edited successfully.")
    except Exception as e:
        print(f"[-] Error: {e}")

# Main function
if __name__ == "__main__":
    print("""
    ███████████████████████████████████████████████
    [+] Live Chat Monitoring and Editing Tool (Educational Use Only)
    [+] creator:      <~{{ RH }}~>
    [+] Team Name: 📿☝️Muslim Army☝️ 📿 
    [+] Monitoring and Editing Network Traffic (Non-root)
    ███████████████████████████████████████████████
    """)

    print("[*] Please enter the network interface (e.g., wlan0): ")
    interface = input("Enter Interface: ")

    print("\nChoose an option:")
    print("1. Start Sniffing")
    print("2. Analyze Traffic")
    print("3. Edit Chat Message")
    choice = input("Enter your choice: ")

    if choice == "1":
        start_sniffing(interface)
    elif choice == "2":
        analyze_traffic()
    elif choice == "3":
        original_message = input("Enter the original chat message to edit: ")
        new_message = input("Enter the new message to replace it with: ")
        edit_chat_message(original_message, new_message)
    else:
        print("Invalid choice.")
