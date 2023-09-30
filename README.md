# Mail Merge Project

## Overview

Welcome to the Mail Merge Project! This project automates the process of creating individual email drafts for a list of names using an email template. With this tool, you can quickly generate personalized email content for each person in your list, making it easy to send customized messages.

## Project Structure

The project consists of the following components:

- **Input Folder**:
  - `Letters` folder: Contains the email template file named `starting_letter.txt`. You can customize this template as per your requirements.
  - `Names` folder: Contains the list of names in a file named `invited_names.txt`. Add or remove names from this list as needed.

- **Output Folder**:
  - `Ready To Send` folder: This folder will contain individual email draft files, each tailored for a specific person. An example email draft is provided in the file named `example.txt`.

- `main.py`: This is the main script of the project. When executed, it processes the names from `invited_names.txt` and generates individual email draft files in the `Ready To Send` folder.

## How to Use

1. Customize the email template:
   - Open `starting_letter.txt` in the `Letters` folder.
   - Modify the email content to suit your needs. You can use placeholders like `{name}` to dynamically insert names from the list.

2. Add or remove names:
   - Open `invited_names.txt` in the `Names` folder.
   - Add the names of the recipients, one per line.

3. Run the script:
   - Execute `main.py`.
   - The script will automatically generate individual email draft files in the `Ready To Send` folder for each name in the list.

4. Ready to send:
   - Open the generated email draft file for a specific person in the `Ready To Send` folder.
   - Copy the content and use it in your preferred email client to send personalized messages.

With the Mail Merge Project, you can save time and effort by automating the process of creating personalized email drafts for multiple recipients. Enjoy sending customized messages with ease! 📧👥
