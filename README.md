# PennApps Backend Technical Challenge

## Part 1: Authentication

Logging in, logging out, and registering were all implemented using views in `views.py`. 

### Logging in
I implemented logging in with the form found in `login.html`. Actually, first I changed `/` to `login.html` in `urls.py` for when I implemented the protection from non-authenticated users. This means that when you first go to the website, you're sent to the login page, rather than the index where you can see the status of your application. 

When the form in `login.html` is submitted, we send a request to the `signIn` view in `views.py`. This authenticates the user with the inputted username and password. If the login is valid, the user is redirected to `index.html`, which is our home page. A message is displayed using `{{ message }}` to alert the user that the login was successful. Otherwise, the user is returned to the login page again, and another message shows that the login is invalid. The messages were mostly for me (the dev) to see if the login and logout were working. 

### Logging out
When the logout button in `index.html` is clicked, it sends a request to the `signOut` view in `views.py`, which logs out the user and returns them to `/`, which is just the login screen. I used a message to alert them that the logout was successful.  

### Registering 
On the login page, there is another button that when clicked, will take you to `signup.html`. This was the hardest part to implement. Once all the fields are filled correctly, the website sends a request to the `createUser` view. `createUser` uses the Application model (which I modified to include a firstName and lastName field in `models.py`) to create a user based on the input in the form. If the creation is successful, the user is alerted with a message, and they are redirected to the index, where they can check the status of their application, create an application, or log out. 

### Authentication:
Using `@login_required()`, I made it so that all the html pages aside from `login.html and `signup.html` are only accessible by logged-in users. In `settings.py`, I specified that `'login'` as the `LOGIN_URL` so that it would redirect to the right page. 

## Part 2: User Application

For this part, I created a `forms.py` file to store the application form in the `AppForm` class. I also modified the `Application` model in `models.py` to include all the user-implemented fields. 

I had to put `Null=True` in the `applicant` field. I also changed the DateField for birthday into a CharField, instead specifying in `application.html` to use a YYYY-MM-DD format. 

When the submit button is clicked, a request is sent to the `submitApplication` view, which takes all the inputs from the form aside from the applicant. The applicant field is instead obtained with `request.user`, which logs the user that sent the request. "PROC" is also set as the default for every applicant when it appears in `index.html` using `{{user.application.status}}`, and can be changed in the admin panel of django. 

However, one thing that I was struggling with was making it so that each applicant could only submit one application. If a user has already submitted an application, if they go to submit another one, they'll see a unique constraint error. This is because the applicant field is a OneToOneField. If I had more time, I would try to figure this part out. 

## Part 3: The extra things I added
I added messages to alert the user of if they successfully logged in, signed out, or registered, but that's about it. 
