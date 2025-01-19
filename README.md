# Portly - Advanced Port Scanner

**Portly** is a powerful and efficient Python-based port scanner that helps you detect open ports, resolve services, grab banners, and log results. With multithreading support, Portly makes network scanning fast and simple.

---

## Features
- **Quick Scan**: Scans well-known ports (1-1024).
- **Full Scan**: Scans all ports (1-65535).
- **Custom Scan**: Allows you to specify a custom range of ports.
- **Multithreaded Scanning**: Scan multiple ports simultaneously for faster results.
- **Service Detection**: Identifies services running on open ports.
- **Banner Grabbing**: Fetch additional information from open ports.
- **Hostname Resolution**: Converts domain names to IP addresses.
- **Batch Scanning**: Scan multiple targets from a file.
- **Logging**: Save scan results to `scan_results.txt`.

---

## How to Use
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/portly.git
   ```
2. Navigate to the project directory:
   ```bash
   cd portly
   ```
3. Run the script:
   ```bash
   python portly.py
   ```

4. Follow the on-screen prompts to:
   - Enter a single target (IP or hostname) or provide a file with multiple targets.
   - Choose the type of scan (Quick, Full, or Custom).
   - Specify the number of threads for faster scanning.

---

## Example
### Single Target
```bash
Enter the target IP address or hostname: scanme.nmap.org
Enter the start port: 20
Enter the end port: 80
Enter the number of threads to use: 10
```

---

## Output
- Open ports and their services are displayed in the terminal.
- Results are saved to `scan_results.txt` for future reference.

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.

---

## Credits
Developed by **[Your Name]** as an efficient and lightweight network scanner.
