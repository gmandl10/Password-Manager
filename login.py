class Account():
    
    def __init__(self):
        
        self.website, self.url = self.enter_website()
        self.user = self.enter_user()
        self.password = self.enter_password()
        # self.encrypted = self.encrypt_password()
        self.security = self.enter_security()
        self.password_history = []
        
    def enter_website(self):
        """
        This method acquires the website name for which the user is making a new account.

        Parameters:
        - None

        Returns:
        - website_name (str): The name of the website for which the user is making a new account
        - website_name (str): The url of the website for which the user is making a new account
            This variable is optional. It takes on a either string value (in the case that the user entered
            a website url) or None if the user has chosen to skip entering the url

        """
        
        website_name = str(input('Enter the name of website on which you have created an account: '))
        website_url = str(input('Enter the url of the website (optional: press ENTER to continue): '))
        
        # check if user skipped the url
        if website_url == "":
            website_url = None
        else:
            while not self.__is_valid_url(website_url) or website_url != "":
                print("Invalid URL for website. Enter a valid url or press Enter to continue without a URL: ")
        
        return website_name, website_url
    
    def enter_user(self):
        """
        This method acquires the user name that the user used to make the new account.

        Parameters:
        - None

        Returns:
        - user_name(str): The user name that the user created the account with
        
        """
        
        user_name = str(input('Enter the username for the login: '))
        
        return user_name
    
    def enter_password(self):
        """
        This method determines the password for the new account.

        The user can either enter their own password or elect for the computer to auto generate
        a password for them. In the case of the latter, the create password function would be called.

        Parameters:
        - None

        Returns:
        - password (int): The pre-encryption numerical representation of the account password

        """
        
        password = str(input('Enter the password for the login (or press ENTER for a computer generated password): '))
        if password == '':
            password = self.__create_password()
        
        password = self.__string_to_number(password) # compute the numerical representation of the password
        
        return password
        
    def enter_security(self):
        """
        This method retrieves the security questions selected by the user for the new account.

        Parameters:
        - None

        Returns:
        - security (dict): The security dictionairy's keys are the security questions and the 
        value is the answer corresponding to the question of the key. In the case where there are
        no security questions, security is given a value of None.

        """
        
        security = {} # initialize dictionairy for storing security questions and answers
        question = ' '
        while question != '':
            question = str(input('Enter the security question (or press ENTER to finish): '))
            if question == '':
                break
            answer = str(input(f"Enter the answer to the security question: "))
            security[question] = answer

        # check if security is empty
        if len(security) == 0:
            security = None
            
        return security
    
    def __create_password(self):
        """
        This method generates a random password for the user.

        The user can control the length of the password by entering the minimum and maximum
        length for the user. Then, a choice is made for a random length between the maximum
        and the minimum.

        Parameters:
        - None

        Returns:
        - password (str): The string representation of the randomnly generated password

        """
        import string
        import random
        
        min_length = int(input('Enter minimum length for password: '))
        max_length = int(input('Enter maximum length for password (or 0 if there is no maximum): '))
        if max_length == 0:
            max_length = 45
        chars = string.ascii_letters + string.punctuation + string.digits # list of 
         # characters to randomnly select from
        
        password = ''
        
        password_length = random.randint(min_length, max_length) # select random length
        
        while len(password) < password_length: # randomnly select characters
            index = random.randint(0, len(chars)-1)
            password += chars[index] 
            
        print('The computer generated password is: ' + password)
        
        return password
            
    def set_new_password(self):
        """
        This method sets a new password for an existing account.

        The user can either enter their own password or elect for the computer to auto generate
        a password for them. In the case of the latter, the create password function would be called.

        Parameters:
        - None

        Returns:
        - None

        """
        
        new_password = str(input('Enter new password for login (or press ENTER for a new computer generated password): '))
        
        while new_password == self.password:
            new_password = str(input('Error - Same as old password. Enter new password for login (or press ENTER for a new computer generated password): '))
            
        if new_password == '':
            new_password = self.create_password()

        new_password = self.__string_to_number(new_password)
            
        self.password = new_password # set password to the new password
        print('Password Changed Succesfully')
        return 
    
    def set_new_username(self):
        """
        This method sets a new user name for an existing account.

        Parameters:
        - None

        Returns:
        - None

        """
        
        new_user = str(input('Enter new username for login: '))
        old_user = self.user
        self.user = new_user
        
        print('Username changed successfully from ' + old_user + ' to ' + new_user)
        
        return

    def __string_to_number(string):
        """
        This method converts a string into its pre-encrypted numeric string.

        The string is read character by character and the ordinal value of each character is
        appended to a string. At the end, the numeric string is converted into an integer.

        Parameters:
        - string (str): the string representation of the password

        Returns:
        - password (int): The pre-encryption numerical representation of the account password

        """
        m = ''

        for i in string:
            m += str(ord(i))
        return int(m)
    
    def __is_valid_url(url):
        """
        Check if a string is a valid URL for a website.

        Parameters:
        - url (str): The URL to be checked.

        Returns:
        - bool: True if the URL is valid for a website, False otherwise.
        """
        from urllib.parse import urlparse

        try:
            # Parse the URL and check if it has a valid scheme (e.g., http, https)
            parsed_url = urlparse(url)
            return all([parsed_url.scheme, parsed_url.netloc])
        except ValueError:
            return False