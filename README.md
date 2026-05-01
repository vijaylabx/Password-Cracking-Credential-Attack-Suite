# Password Cracking & Credential Attack Suite

**Password Cracking & Credential Attack Suite** is an advanced cybersecurity toolkit designed for professionals and security enthusiasts. This tool is utilized for penetration testing, security auditing, and comprehensive password strength analysis.

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
*   **Automated Reporting:** Generates professional security audit reports detailing all activities and findings.

---

## 🛠️ Usage Guide

### 1. Prerequisites
Ensure you have **Python 3.x** installed on your system. This tool relies on standard Python libraries, so no additional external dependencies are required.

### 2. Setup
Download the project folder and open your terminal or command prompt (CMD) in that directory.

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
**Version:** 1.0