# password_hacker
Password hacker is a simple program that connects to a server and uses predefined vulnerabilities in order to find out the login and password of server's admin. 

**Predefined vulnerabilities of the server:**
- a file with possible admin logins (but every login can have a combination of random upper and lower case)
- if we guess the login correctly we will get the response "Wrong password!" from the server (before "Wrong login!")
- the password contains only ascii_letters and digits
- if we guess the starting part of the password correctly (can be substring of just one character or more) the server has a delay in a response

**Learning outcomes:**  
I've learned about how basic hacking works. I've worked with iterators and generators, and I’ve learned a little something about the itertools module – 
one of the most powerful features of Python. I've practiced developing a client app and connecting to a server using the socket module. 
The project also have got me acquainted with JSON and the time module.
 
   
**Example:**  
Input: *python hack.py localhost 9090*  
Output:  
*{  
      "login" : "su",  
      "password" : "fTUe3O99Rre"  
}*    


This program is based on project from hyperskill.org:  https://hyperskill.org/projects/80  
