# Lesson Learned?

- Task 1 Find the Flag
    
    This is a relatively easy machine that tries to teach you a lesson, but perhaps you've already learned the lesson? Let's find out.
    
    Treat this box as if it were a real target and not a CTF.
    
    Get past the login screen and you will find the flag. There are no rabbit holes, no hidden files, just a login page and a flag. Good luck!
    
    # let's perform a Nmap or rust scan
    
    ```jsx
    rustscan -a {ip}
    ```
    
    ![Untitled](Lesson%20Learned%20fa42723fbef24f2a9df61546935ab57a/Untitled.png)
    
    # lets head over to the website(which is login page)
    
    Since there is no other suspicious directories or files, let's perform a SQL injection.
    
    when bypassing we have to be careful not to use the wrong SQL injection commands.
    
    such as OR 1=1. 
    
    ![Untitled](Lesson%20Learned%20fa42723fbef24f2a9df61546935ab57a/Untitled%201.png)
    
    here I have used this command which is known as union select to Select more and more null values until the query is correct:
    
    then we can enter any password. this will bring up the flag.
    
     
    
    ![Untitled](Lesson%20Learned%20fa42723fbef24f2a9df61546935ab57a/Untitled%202.png)