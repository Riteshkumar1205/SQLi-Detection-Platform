## 🛡️ SQL Injection Detection Platform
**Secure | Monitor | Respond**

A lightweight, modular, and real-time platform for detecting and responding to SQL Injection (SQLi) attacks in web applications. Designed for ethical use in cybersecurity research, training labs, and internal app monitoring environments.

## ⚠️ Legal Disclaimer
This software is provided strictly for educational, ethical, and authorized security research purposes only.
Any unauthorized deployment, misuse, or testing on systems without prior consent may violate cybersecurity and data protection laws (e.g., IT Act, GDPR, CFAA).

By using this software, you agree to take full legal responsibility and abide by all relevant laws and organizational security policies.

## 🧩 Project Overview
The SQL Injection Detection Platform offers real-time monitoring, logging, and alerting capabilities to detect SQLi payloads. It integrates key security mechanisms such as rate limiting, honeypot traps, and automated notifications, making it suitable for:

Cybersecurity education & red team training

Secure application development environments

Internal threat monitoring in authorized networks

## ✅ Core Features
Category	                           Feature	                                           Description
🧠 Detection	                     Regex-Based SQLi Signatures	                      Identifies common SQL injection payloads through carefully crafted regex rules
📦 Data Logging	                  SQLite-Based Log Storage	                         Records suspicious input with timestamps, IP, and endpoint information
🧪 Deception	                     Honeypot Field	                                     Traps automated bots or crawlers injecting SQLi into decoy fields
📉 Rate Limiting	                  Request Throttling	                               Prevents brute-force or repeated attacks using IP-based rate limiting
📊 Visibility	                     Admin Dashboard	                                  Review, filter, and manage logged threats through a secure web interface
🔔 Alerts	                        Real-Time Notifications	                            Sends alerts to Email and Slack upon detection of suspicious activity
🎨 UI/UX	Dark                       Themed Interface	                                  Clean, responsive frontend built with HTML/CSS using a modern dark UI

## 💻 Technology Stack
Layer	Technology Used
Backend	Python 3.x, Flask
Frontend	HTML5, CSS3 (Dark Theme)
Database	SQLite
Security	Rate Limiting, Honeypots, Regex Patterns
Notifications	smtplib (Email), Slack Webhooks
Environment	Cross-platform (Linux/macOS/Windows)

## 🧰 Installation Guide
~~~
# Clone the repository
git clone https://github.com/susanthratnala/SQLi-Detection-Platform.git
cd SQLi-Detection-Platform

# Set up a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Configure environment variables
cp .env.example .env
~~~

## 📄 .env Configuration
Set the following environment variables in .env:

~~~
EMAIL_USER=your_email@gmail.com
EMAIL_PASS=your_email_app_password
SLACK_WEBHOOK=https://hooks.slack.com/services/xxxx/yyyy/zzzz
~~~
Ensure the use of secure app passwords and never hardcode credentials in source files.

## 🚀 Running the Application
~~~
python3 app.py
~~~
Once started, access the platform via:

📍 http://localhost:5000

## 🔐 Admin Login
   Field       	Value
    Username	   admin
    Password	   adminpass

**⚠️ Important: Update these credentials in production deployments immediately to avoid unauthorized access.**

## 🔎 Sample Detection Flow
User submits form input suspected of SQLi (e.g., ' OR '1'='1)

Regex engine flags the pattern and logs it with metadata

Admin dashboard displays incident with details

Email and/or Slack notifications are dispatched instantly

## 🛡️ Deployment Best Practices
Always run behind HTTPS with proper TLS setup

Change default admin credentials before production use

Regularly rotate Slack and email credentials

Integrate with SIEM tools for broader visibility

Set up IP blacklisting for repeated offenders

## 📄 License
MIT License
This project is open-source and distributed under the MIT license.
You are free to use, modify, and distribute it with proper attribution.

Provided “as is” without warranty.

## ⚖️ Legal & Compliance Notice
You must comply with applicable laws in your jurisdiction, including but not limited to:

Region	Applicable Law(s)
India	Information Technology Act (Sections 43A, 66C, 72)
European Union	General Data Protection Regulation (GDPR)
United States	Computer Fraud and Abuse Act (CFAA), ECPA
Global	Local and institutional cybersecurity frameworks

## 📌 Intended Use Cases
Ethical Hacking Labs & Red Team Exercises

University Cybersecurity Coursework

Internal App Defense Validation

Bug Bounty and Safe Harbor Programs (where permitted)

**❌ Not intended for unauthorized pentesting, phishing campaigns, or third-party web scraping.**

## 🧠 Final Thoughts
The SQL Injection Detection Platform exemplifies how thoughtfully engineered, lightweight components—such as regular expression-based input validation, honeypot deception fields, and intelligent logging—can synergize to create a robust first line of defense against one of the web's most pervasive attack vectors.

Far beyond a proof-of-concept, this platform serves as:

🔍 A hands-on learning tool for cybersecurity students and professionals

🛠️ A framework-ready blueprint for integrating detection into larger security architectures

⚙️ A plug-and-play utility for internal app hardening and rapid-response setups

By coupling simplicity with strategic design, this solution highlights a critical truth in cybersecurity:

Detection doesn’t always require complexity—only clarity, intent, and precision.

Whether deployed in a classroom, lab, or secure internal network, this platform equips defenders with actionable insights, alerting mechanisms, and forensic-ready logs—bringing visibility where blind spots often reside.

🧪 **Crafted for education.**
⚔️ **Empowered for real-world adaptation.**
🧭 **Built to inspire better security practices.**

