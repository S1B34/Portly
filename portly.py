# Portly - Advanced Port Scanner

import socket
import re
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime


def resolve_hostname(hostname):
    """
    Resolve a hostname to an IP address.
    """
    try:
        return socket.gethostbyname(hostname)
    except socket.gaierror:
        print(f"[ERROR] Could not resolve hostname: {hostname}")
        exit()


def scan_tcp_port(target, port):
    """
    Scan a single TCP port to check if it's open.
    """
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            s.connect((target, port))
            try:
                service = socket.getservbyport(port, "tcp")
            except OSError:
                service = "Unknown Service"
            print(f"[OPEN] TCP Port {port} (Service: {service}) is open.")
            log_result(target, port, "TCP", service)
    except (socket.timeout, ConnectionRefusedError):
        pass
    except Exception as e:
        print(f"[ERROR] Could not scan port {port}: {e}")


def grab_banner(target, port):
    """
    Grab a banner from an open port (if available).
    """
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(2)
            s.connect((target, port))
            s.send(b"GET / HTTP/1.1\r\n\r\n")
            banner = s.recv(1024).decode().strip()
            return banner
    except Exception:
        return "No banner available"


def log_result(target, port, protocol, service="Unknown"):
    """
    Log scan results to a file.
    """
    with open("scan_results.txt", "a") as file:
        file.write(f"{datetime.now()} - {target}:{port} ({protocol}) - {service}\n")


def scan_ports(target, start_port, end_port, protocol, max_threads):
    """
    Scan a range of ports on the target using multithreading.
    """
    with ThreadPoolExecutor(max_threads) as executor:
        for port in range(start_port, end_port + 1):
            if protocol == "TCP":
                executor.submit(scan_tcp_port, target, port)


def get_scan_range():
    """
    Get the range of ports to scan.
    """
    print("Select a scan type:")
    print("1. Quick Scan (ports 1-1024)")
    print("2. Full Scan (ports 1-65535)")
    print("3. Custom Scan")

    choice = input("Enter your choice (1-3): ").strip()
    if choice == "1":
        return 1, 1024
    elif choice == "2":
        return 1, 65535
    elif choice == "3":
        start_port = int(input("Enter the start port: "))
        end_port = int(input("Enter the end port: "))
        if start_port < 1 or end_port > 65535 or start_port > end_port:
            print("[ERROR] Invalid port range.")
            exit()
        return start_port, end_port
    else:
        print("[ERROR] Invalid choice.")
        exit()


def main():
    print("Welcome to Portly - Advanced Port Scanner!")
    print("1. Scan a single IP/domain")
    print("2. Scan multiple targets from a file")

    scan_choice = input("Choose an option (1 or 2): ").strip()
    if scan_choice == "1":
        target = input("Enter the target IP address or hostname: ").strip()
        target = resolve_hostname(target)
        start_port, end_port = get_scan_range()
        max_threads = int(input("Enter the number of threads to use: "))
        protocol = "TCP"  # You can extend for UDP
        print(f"\nScanning {target} from port {start_port} to {end_port}...\n")
        scan_ports(target, start_port, end_port, protocol, max_threads)
    elif scan_choice == "2":
        file_path = input("Enter the file path containing targets: ").strip()
        try:
            with open(file_path, "r") as file:
                targets = [line.strip() for line in file if line.strip()]
            start_port, end_port = get_scan_range()
            max_threads = int(input("Enter the number of threads to use: "))
            protocol = "TCP"  # You can extend for UDP
            for target in targets:
                print(f"\nScanning {target} from port {start_port} to {end_port}...\n")
                resolved_target = resolve_hostname(target)
                scan_ports(resolved_target, start_port, end_port, protocol, max_threads)
        except FileNotFoundError:
            print(f"[ERROR] File not found: {file_path}")
            exit()
    else:
        print("[ERROR] Invalid choice.")
        exit()

    print("\nPort scan completed. Results saved to 'scan_results.txt'.")


if __name__ == "__main__":
    main()
