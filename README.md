# Python-stuff
<h1 center="align">The first file (SSH-BruteForce.py)</h1> <br/>

- Python script Explanation:<br/>
<br/>
The first script is is a python code that aims to conduct an SSH based Brute Force attack on a given system in a very brief period of time , it automate the process of attempting multiple username and password combinations in order to gain unauthorized access to an SSH server. It is typically used as a hacking tool and is not ethical or legal to use without proper authorization. <br/>
<br/>
Here's a high-level overview of how an SSH brute force Python code typically works:<br/>
User Input: The script prompts the user to enter the target SSH server's IP address or hostname and a file containing a list of username and password combinations to try.<br/>
<br/>
SSH Connection: The script uses a Python SSH library (such as Paramiko) to establish a connection to the target SSH server.<br/>
<br/>
Username and Password Combination: The script reads each line from the provided file, which contains username and password pairs, and attempts to authenticate with the SSH server using the current combination.<br/>
<br/>
Authentication Attempt: For each username and password combination, the script sends an authentication request to the SSH server and waits for the response.<br/>
<br/>
Response Handling: The script checks the response from the SSH server to determine if the authentication was successful. If successful, it means the correct username and password combination has been found, and the script may proceed to perform unauthorized actions on the target system. If unsuccessful, it continues to try the next combination.<br/>
<br/>
Brute Force Loop: The script repeats the process of attempting different username and password combinations until it exhausts the list or finds a successful combination.<br/>
<br/>
<br/>
<h1 center="align">The second file (InfoGathering.py)</h1> <br/>

- Python script Explanation:<br/>
<br/>
The get_ip_address() function retrieves the local IP address of the machine running the script using the socket library.<br/>
The get_public_ip() function makes a request to the ipify API to fetch the public IP address of the machine using the requests library.<br/>
The get_user_agent() function sends a request to the httpbin.org API to get the user agent string of the machine's web browser.<br/>
The main() function calls the above functions and prints the gathered information.<br/>
When executed, the script will display the local IP address, public IP address, and user agent string.<br/>
The get_location() function takes the public IP address as a parameter and uses the ipapi API to retrieve location information such as country, city, region, postal code, and timezone.<br/>
The main() function calls all the relevant functions and prints the gathered information, including the local IP address, public IP address, user agent string, and location details.<br/>
In this version, the script includes an additional get_location() function that fetches location information based on the public IP address. The ipapi API is used to obtain the country, city, region, postal code, and timezone associated with the IP address.<br/>


