MailScanner – Email Extraction Tool (Python)

MailScanner is a lightweight Python script that helps you extract email addresses from web pages you choose.  

Note: This project is intended for **personal or learning purposes only**.  
Using scraped emails for unsolicited contact or illegal actions is strictly prohibited.

---

How It Works

1. Open the file called `url.txt`  
   - Each line should contain one webpage URL you want to scan

2. Run the script  
   - Open your terminal or command prompt  
   - Type:
     ```bash
     python3 main.py
     ```

3. Get the results  
   - A `.csv` file will be automatically created  
   - Each column corresponds to one URL  
   - Email addresses found on each page are listed below

---

Generated CSV:

| mail_1                      | mail_2                          |
|-----------------------------|----------------------------------|
| info@example.com            | jane.doe@anotherexample.org     |
| support@example.com         | contact@anotherexample.org      |

---

Legal Disclaimer
  
You are entirely responsible for complying with local laws and the terms of service of the websites you access.

Misusing email addresses obtained with this tool may violate privacy laws or platform guidelines.  
Please use responsibly and ethically.

---

Feel free to fork, give feedback!
