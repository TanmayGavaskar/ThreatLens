# ThreatLens
A Real Time Vulnerability Monitoring Tool

Note: This repository only includes the main script, sel.py.

ThreatLens is a Python-based web scraping tool designed to help organizations monitor OEM websites for critical vulnerabilities in IT/OT equipment. This project focuses on real-time data extraction and reporting to enhance cybersecurity measures.

Project Overview:

ThreatLens leverages powerful Python libraries such as Selenium to scan specified OEM websites for vulnerabilities, extract relevant information like CVE-IDs, risk severity, product details, and publication dates, and then sends this data to predefined recipients via automated email. The tool is designed to be adaptable, allowing users to set up vulnerability monitoring for various websites and adjust the level of alerts based on risk severity.

Key Features:

1. Real-Time Web Scraping: Monitors OEM websites continuously to detect vulnerabilities as they are published.  
2. Data Extraction: Captures and parses critical information including CVE-IDs, product names, risk levels, and dates.  
3. Automated Email Notifications: Sends collected data and mitigation strategies directly to designated email addresses.  
4. Compliance & Security: Ensures responsible data scraping by adhering to best practices for privacy and security.  


Technologies Used:

1. Programming Language: Python  
2. Web Scraping: Selenium 
3. Email Automation: SMTP (Simple Mail Transfer Protocol)  
4. Database: MySQL for storing website links and user information  

Installation & Setup:  

1. Clone the repo:   

  ```git clone https://github.com/nachiket2048/Web-Scraping-Tool.git```  

2. Navigate to the project directory:

  ```cd Web-Scraping-Tool``` 

3. Set up your configuration:  
Modify the script to include the necessary website links, email credentials, and other configurations.

Usage: 

Run the main Python script to initiate vulnerability monitoring:

```python sel.py```

The script will begin scanning the specified OEM websites, collecting vulnerability data, and sending email notifications as per the configured settings.

Limitations and Considerations:

1. Website Changes: Frequent updates to OEM websites’ structures may require adjustments to the script.  
2. Anti-Scraping Measures: Implementing proxy rotation and CAPTCHA bypass techniques can be necessary to maintain seamless operation.  
3. Data Privacy: Ensure you comply with the terms and conditions of the target websites and check their robots.txt files for scraping permissions.  


Contributions:

Feel free to fork this project and submit pull requests. Contributions are welcome to enhance the functionality or address additional use cases.


