#Unused_Medicine_Donation
Collaborators :
    (1) Arvind Tomar - 200001008
    (2) Arvind Yadav - 200001009
    (3) Likhit Raj - 200001039
    (4) Rishabh Sharma - 200001067
    (5) Chaitanya Dhanorkar - 200001021

Unused Medicine Donation -

•Functional requirements:-

>Login - 
    Definition: For making use of the App, the users have to enter username and password which they have created during registration and been saved in our database in the Login page. The user might be a customer or an Admin also.
    Inputs: Username and password. 
    Outputs: The system will state whether inputs are correct or not.
    Pre conditions: The user must have signed in the system and have a valid username and password.Incorrect username and Password are notified with a warning on the web page.
    Post conditions: The user will enter their respective profile page after entering right credentials.

>User Login :
    For taking part in medicine donation or any other functionality of the app, the user need must login.

>Admin Login:
    To access admin privileges like add or remove members the admin must login.
    Active member Login: To access database and to revert back to user queries the active member must login.
    Basically, in order to use the app login is necessary.

>Log out :
    Definition: When user wants to end the current session he/she could log out.
    Pre conditions: The user/admin/active member must be logged in.
    Post conditions: The user/admin/active member will be redirected to home page of the website.

>Register Function
    We will add a page where users, active users and admin can register themselves with our website. 
    They need to provide us information such as-
    (1) Name
    (2) Address
    (3) Phone Number
    (4) Email ID
    Then the user/active user/admin will need to create a username and password which they will need to log in to our website.
    We will save the information entered during the registration in our database.
    Administrative functions
				
>Manage Users - 
    Definition:The admin can view user details,create or delete new user,clear a user session and Choose not to receive email notifications about locked user accounts and can also access the user accounts based on terms mentioned in terms and conditions.
    Pre conditions: The admin must be logged in into the respective account.
    Post conditions: The admin can now manage user accounts.

>Manage Policies - 
    Definitions: The admin could edit or create or delete certain policies based on user or management interests.
    Pre conditions: The admin must be logged in and re-authentication is required for editing policies.
    Post conditions: The current policies will be  replaced by the edited ones.

>Security and Authentication -
    The admin decides the level of security and authentication for certain edits in the database.

>Medicine Record :
    We will keep a record of any transaction of medicines between the users and members, including information like name, amount of drugs, donor and receiver's names, etc. This information will only be visible to admins.

>Providing NGO nearby location :
    Interested people will be provided with the location of the nearest NGO  so that they may contribute by donating medicines easily. This shall be implemented by using rest APIs of Google maps. 

>Medicine Received Verification :
    After the donation of medicines, Verification has to be provided by the members and we will change the records accordingly. Verification will assure us that the transaction has occurred successfully, and therefore, it's an important step.

>Transaction Record:
    We will store a record of all the monetary donations made to our portal through monetary donation function.
    Only admin can see the transaction record information.

>Monetary Donation:
    Some people may also contribute by donating money to the NGO . This fund so raised shall be used to arrange medicines for those in need. Our app shall provide facility to donate money to the NGO  via different modes like internet banking , QR code etc.

>Medicine Request Form :
    To distribute medications we will add a request form , user who needs the medications will request the medicine by filling the form. After filling the form the request goes to the admin and base on the information in the form he will decide whether to donate medicine to the user or not.
    Required information in the form.
                1. medicine required (name and amount)
                2. Reason  
                3. medical report
                4. name ,address ,contact

>Medicine Request Message :
    A notification/message will pop up on the members' page once an admin has checked the information filled in the request form and passed it. In this way, the members don't have to worry about verifying info and attend to the needy person and provide them the medicine required.

>Urgent/in-need medicine display:
    We will provide a feature for admin where he can display the name of the medicine required for a needy user and if the medicine is out of stock.

>Customer feedback:
    We will include feedback feature to get suggestion/experience from the users and so that we can implement/improve in the future to provide best service to the users.

•Non Functional Requirements:-

>Reliability :
    This software system fulfills its assigned task in a given environment for all input cases, assuming that the hardware and the input are free of error . It does not fail under normal conditions

>Security:
    The database contains data like medical records of the users and personal details like email,phone number,etc so securing the website becomes highly important.Our security system locks the account after certain number of unsuccessful login attempts.The user needs to get in contact with support cell to unlock the account.We would also ensure a strong password is created during registration

>Maintainability:
    During maintenance we will try impliment all those requirements that relate to the ease with which an end user might be least affected even during the course of a maintenance activity.

>Scalability:
    We will try to make the website scable so that without much of hue and cry additional number of users can we added.

>Usability: 
    Usability refers to how easy it is to learn, understand and operate the system. We will try to make the system user-friendly so that it is easy to use, and this also encourages more participation from the user.

>Efficiency :
    Efficiency refers to how fast the system reacts to the user's actions. It is the ability of the system to handle the load, response time, etc. We will optimize the site and regularly audit the site's performance by checking load times, site speed, correct formatting, and continuity with the text and images.

>Transferability:
    It refers to the ability of a system to be transferred from a particular operating environment to another. The site will work on any type of search engine and thus it is transferable.




>Process,Model,Aproach Suitable for the Project 
        In our opinion , in case of our project (Unused medicine distribution system) waterfall model is more suitable . The reason being that  for our project we are  more or less very clear about the demands of the customers and the functional requirements.
        The customer requirements are predictable in case of unused medicine distribution system and they may not change for sufficiently long time.  Thus the requirements are very well understood and changes will be fairly limited to the design process. The plan driven nature of waterfall model helps coordinate the work . 
        waterfall model can be used for our project due to its reliability ,strong project management capabilities , better documentation and component reusability . 
        However waterfall model has its own drawbacks .Freezing  requirements usually requires choosing hardware which might result in final software using hardware that has become  obsolete. So in such cases agile process becomes more preferred in which the planning is incremental and may even be according to user’s changing requirements. Also a good idea is to freeze a few features according to the highest priority  as in waterfall model and rest in agile process.
        So on basis of above arguments we can conclude that  by and large waterfall model will be most preferred process model for our project . However for few features agile process model will be preferred as per changing scenario



<!-- admin login -->
Username :umd
Password : umd