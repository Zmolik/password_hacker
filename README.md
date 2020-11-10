# password_hacker
A program based on project at hyperskill.org: https://hyperskill.org/projects/80
   
Password hacker is a simple program that connects to a server and use predefined vulnerabilities in order to find out the login and password of admin. 

Predefined vulnerabilities:
- a file with possible admin logins (but every login can have a combination of random upper and lower case)
- if we guess the login correctly we will get the response "Wrong password!" from the server (before "Wrong login!")
- the password contains only ascii_letters and digits
- if we guess the starting part of the password correctly (can be substring of just one character or more) the server has a delay in a response

Learning outcomes:  
You will learn how hacking works. You will work with iterators and generators, and you’ll learn a little something about the itertools module – 
one of the most powerful features of Python. You will practice developing a client app and connecting to a server using the socket module. 
The project will also get you acquainted with JSON and the time module.
 
   
Example 1:  
Input: python hack.py localhost 9090  
Output:  
{  
      "login" : "su",  
      "password" : "fTUe3O99Rre"  
}  
