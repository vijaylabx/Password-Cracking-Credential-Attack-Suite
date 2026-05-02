# Password Cracking & Credential Attack Suite

**Password Cracking & Credential Attack Suite** is an advanced cybersecurity toolkit designed for professionals and security enthusiasts. This tool is utilized for penetration testing, security auditing, and comprehensive password strength analysis.

---

## 🔥 What's New (v1.1)
*   **HIBP API Integration:** Added a new module to check passwords against billions of leaked credentials in the **Have I Been Pwned** database.
*   **Visual Analytics:** Automated generation of **Pie Charts** for password strength distribution using Matplotlib.
*   **Network Attack Simulation:** Added brute-force modules for **SSH** and **FTP** services.
*   **Web Login Security Auditor:** A module for testing and auditing local web-based authentication forms (for educational/lab use).
*   **Improved Security:** Implementation of the **K-Anonymity** model for password checking, ensuring your local passwords are never sent over the internet in plain text or full hash.

---

## 📌 Use Cases

1.  **Security Auditing:** To evaluate the strength of passwords within your system or organization.
2.  **Penetration Testing:** To identify vulnerable systems during authorized security assessments.
3.  **Password Recovery:** To recover original passwords from hashes using custom wordlists.
4.  **Educational Learning:** To understand how hashing algorithms and various credential attacks function.
5.  **Compliance Testing:** To verify if passwords adhere to NIST security standards and organizational policies.

---

## 🎯 Purpose

The primary objective of this suite is to provide a robust platform for evaluating credential security. It offers a centralized set of tools capable of handling everything from simple dictionary attacks to advanced multi-threaded cracking and detailed security audit reporting. It serves as an ideal project for cybersecurity internships and security research.

---

## 🚀 Key Features

*   **Dictionary Generator:** Creates thousands of password permutations and combinations using custom base words and mutation rules.
*   **Hash Identification:** Automatically detects unknown hash algorithms (MD5, SHA1, SHA256, SHA512, etc.).
*   **Multi-Threaded Cracking:** Utilizes multiple CPU cores to maximize performance and speed up the cracking process.
*   **Batch Mode:** Capable of processing hundreds of hashes simultaneously from a single file.
*   **Advanced Password Analyzer:** Calculates password entropy and provides actionable recommendations to improve security.
*   **Network Attack Simulation:** Capability to test and audit network services like **SSH** and **FTP**.
*   **Web Form Auditing:** Automated testing of web-based login forms in controlled environments.
*   **Visual Analytics:** Automatically generates visual summaries (`.png` charts) of security audits.
*   **Real-World Leak Checker:** Checks if a password has been compromised in known data breaches using the **Have I Been Pwned (HIBP)** API.
    *   *Technical Note:* Uses the **Range API** with a 5-character SHA-1 prefix for maximum privacy.
*   **Automated Reporting:** Generates professional security audit reports detailing all activities and findings.

---

## 🛠️ Installation & Usage Guide

### 1. Prerequisites
Ensure you have **Python 3.x** installed on your system.

### 2. Installation
1. Clone or download this repository 
```bash
   https://github.com/vijaylabx/Password-Cracking-Credential-Attack-Suite.git 
   ```

2. Navigate to the project directory in your terminal or command prompt.
    ```bash
    cd Password-Cracking-Credential-Attack-Suite 
    ```


3. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```
   Alternatively, install manually:
   ```bash
   pip install requests paramiko matplotlib
   ```

### 3. Running the Tool
Execute the following command to launch the suite:
```bash
python suite.py
```

### 4. Menu Options
*   **Option 1 (Dictionary Generator):** Enter base words (e.g., admin, password) to generate an expanded wordlist.
*   **Option 2 (Hash Identification):** Paste a hash to identify its algorithm (e.g., MD5 vs SHA256).
*   **Option 3 (Single Cracker):** Provide a hash and a wordlist path (e.g., `reports/wordlist.txt`) to attempt a crack.
*   **Option 4 (Batch Mode):** Upload a file containing `username:hash` pairs for automated bulk cracking.
*   **Option 5 (Analyzer):** Enter any password to view its security metrics and NIST compliance status.
*   **Option 6 (Audit Report):** Generate a comprehensive summary of all cracking attempts and analysis performed during the session.
*   **Option 7 (Leak Checker):** Use the HIBP database to check if a password has ever appeared in a public data breach.
*   **Option 8 (Network Attack):** Perform brute-force simulations on SSH and FTP services.
*   **Option 9 (Web Auditor):** Audit local web application login forms for credential vulnerabilities.

### 5. Quick Start Example
1. Install dependencies: `pip install -r requirements.txt`
2. Run: `python suite.py`
3. Choose option 1 to generate a wordlist with base words "admin,password".
4. Choose option 5 to analyze a password like "P@ssw0rd123".
5. Choose option 7 to check if "password123" is leaked.

**Note:** Network and web features are for educational use in controlled environments only. Unauthorized use is illegal.

---

## 📂 Project Structure

*   `suite.py`: The main entry point featuring the interactive CLI menu.
*   `modules/`: Contains the core logic for the cracker, analyzer, generator, and reporter.
*   `reports/`: Default directory for saved wordlists and generated audit reports.
*   `hashFiles/`: Recommended directory for storing input hash files.

---

## ⚠️ Disclaimer

**For Educational Purposes Only!**
This tool is intended strictly for educational use and authorized security testing. Attacking any system without explicit permission is illegal. The developer assumes no liability for any misuse of this software.

---
**Developed By:** Vijay Gi
**Version:** 1.1