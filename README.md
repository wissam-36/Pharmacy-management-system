## Pharmacy Management System


This Python script with a simple graphical user interface (GUI) for managing a pharmacy's inventory and user authentication system. It allows users to adding new medicines, viewing existing medicines, modifying medicine details, and checking the validity of medicines based on expiry dates.The system supports user authentication with login and sign-up functionalities.

### Features
- `**Add Medicine**` : Allows users to add new medicines to the inventory with details such as name, quantity, expiry date, purchase price, and selling price.
- `**View Medicine**` : Displays a list of existing medicines in a tabular format showing details like name, expiry date, purchase price, selling price, and quantity.
- `**Modify Medicine**`: Enables users to modify the details of existing medicines including name, expiry date, purchase price, selling price, and quantity.
- `**Validity Check**` : Feature to check the validity of medicines based on their expiry dates, highlighting medicines that have expired or are about to expire.
- `**User Authentication**` : Implements a simple user authentication system with login and sign-up functionalities to control access to the system.

### Technologies Used
- Python
- Tkinter
- customtkinter
- PIL (Python Imaging Library)
- MySQL Connector (Python library for connecting to MySQL databases)

### Installation
1. Ensure you have Python installed on your system. If not, download and install it from [Python's official website](https://www.python.org/).
2. Install required Python packages:

```
pip install customtkinter
```
```
pip install PIL
```
```
pip install mysql-connector-python
```
3. Set up a MySQL database with appropriate tables for storing medicine details and user credentials.
4. Update the MySQL database configuration in the script (`mysql_user`, `mysql_password`, `mysql_loginDB_name`, `mysql_pharnacyDB_name`) .
5. Run .