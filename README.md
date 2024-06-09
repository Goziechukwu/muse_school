# Muse School

Muse School is a django-based eCommerce site which runs in the Code Institute mock terminal on Heroku. It seeks to greatly aid people in learning music theory and musical instruments, specifically the violin, the saxophone, the piano and the guitar in a progressive step-by-step basis from beginner to mastery. The site is a B2C (Business to Customer) website and will be targeted towards all kinds of people who have interest in learning music, but especially towards passionate learners who have the patience to go through the simplified lesson categories. The lessons in this eCommerce site can be bought by the user in the form of products in an eCommerce website. 


## Using Muse School

Upon visiting Muse School's website, the user will be greeted with the homepage which contains the navigation links and a clickable button to begin the purchase of courses. The user can freely click on any of the navigation links to find what it contains. The website content has been divided into categories that show when the main navigation links are clicked. This website is responsive to all device sizes and works effectively on all types of browsers.

<img src="./static/images/responsivity-test1.PNG" alt="Responsivity on Laptops">

<img src="./static/images/responsivity-test2.PNG" alt="Responsivity on Tablets">

<img src="./static/images/responsivity-test3.PNG" alt="Responsivity on Handsets">


## Features

### Home Section

The Home Section is the first page the site user is greeted with upon visiting the site for the first time. It is open to all site visitors and registered users. At the bottom of the home page contains links to the website's social media page.

<img src="./static/images/home-page.PNG" alt="Home Page">


### My Account Section

The "My Account" section contains the links for Registering and Logging in.

### Register Section

The Register Section can be found in the drop down menu at "My Acount". It contains the Sign-Up form for site visitors who would love to register on the platform. Registered users can buy courses, but site visitors can only read the description of the courses.

<img src="./static/images/register-section.PNG" alt="SignUp Section for Registration">

### Login Section

The Login Section contains the login page for registered users. Site visitors who visit the login page have a signup external link placed there so they can directly signup from there as they can from the Sign Up page.

<img src="./static/images/login-section.PNG" alt="Login or Sign-In Section">

### Courses Section

The Courses Section contains the list of all courses and their titles, prices, ratings and images. When a course is bought, a confirmation email is sent to the buyer and the buyer will be linked to the teacher of that purchased course. Because the courses when bought are educational one-on-one tutorials both in video and when possible in presence, the courses are therefore only bought on a single basis, one after the other, so as to distinguish it from a retail store which usually has a shopping bag that could contain many different items.


## Wireframes

The skeletal structure of the User Interface that focus on the arrangement of the elements and the overall user flow can be seen in the image below:

<img src="./static/images/wireframe.png" alt="Wireframes">


## Search Engine Optimization

A robots.txt file have been added to tell search engine crawlers which pages or files on the website should be crawled and indexed, thereby controlling the access to the website for search engines.

Similarly, a sitemap.xml file which lists all the pages on the website has been created for the purpose of helping search engines discover and crawl them more efficiently.

Appropriate Keywords have been selected relating to what people care about that are linked to Muse School's commercial functions. Some keywords like:
- Music School
- High school musical
- Muse School curriculum
- Muse School music education
- Music school programs
- Music learning for kids
- Children's music education

These keywords are intended to aid the visibility of the website in a Google Search.

## Marketing Techniques

A Facebook business page has been created at [Facebook page](https://www.facebook.com/profile.php?id=61560667980178) to showcase Muse School's brands, engage with it's audience, and run targeted advertising campaigns.

<img src="./static/images/facebook-page1.PNG" alt="Facebook Content 1">
<img src="./static/images/facebook-page2.PNG" alt="Facebook Content 2">
<img src="./static/images/facebook-page3.PNG" alt="Facebook Content 3">

## Technologies Used

The website was designed using the following hosting services and programming languages:

- Django

- Bootstrap

- Cloudinary (for external image management)

- ElephantSQL for the PostgreSQL

- Python

- JavaScript

- HTML5

- CSS3

- [Google Fonts](https://fonts.google.com/) was used to obtain the two fonts, Lato and Sans-Serif used in the website.

The Codeanywhere workspace was used to write the code. 

• All the codes, README and the commits were pushed to GitHub repository

• The fonts used were obtained from the Google Fonts library in google


## Testing Forms and Views

The forms and views have been tested on the gitpod workspace terminal and the tests, totalling to 10 tests returned successful.

<img src="./static/images/test-run-success.PNG" alt="Testing Results for Forms and Views">


## Accessibility Requirements

Muse School has been tested using Lighthouse on Google and found to completely meet Accessibility Requirements, in addition to having Best Practices, and more, as indicated in the screenshot below:

<img src="./static/images/lighthouse-report.PNG" alt="Accessibility Requirements Score">


## Deployment to Heroku

The full-stack project was deployed using the Code Institute's Heroku mock terminal by the following major steps:

- Clone or fork the repository
- Click the "Create New App" button in the Heroku platform
- Add the keys: CLOUDINARY_URL, DATABASE_URL, and their values from their corresponding files.
- I also added a SECRET_KEY and created a private value for it
- From the Settings, I linked the app to the repository
- Click on the "Deploy" button

The project was deployed to heroku with the following link: [Muse School Heroku App](https://muse-school-65d38376d319.herokuapp.com//)


## User Stories

### Site Users

A site user can:

- view a list of all courses or of courses by category and select a course to view more details about it.
- click on a course to read the full description of the course.
- view the courses by level, as shown on the navigation link of the homepage ("Harmonic Beginnings, "Melodic Journeys", or "Symphonic Mastery")
- view courses by ratings, prices or categories.
- register an account so as to be able to comment on a post.
- like or unlike a post, so as to appreciate the writer.


### Registered Users

A registered user can:

- perform all the functions a site user can, but in addition can
- purchase a course.


### Site Administrators

A site admin can:

- add more courses as products
- remove courses
- approve or disapprove card payments for any course.


## Bugs, and How I Fixed Them

I discovered my "Edit" button for posted comments was not responding to the click event, in order to fix this, I checked the button id on the post html and the button id on the comment section JavaScript and found that I had used the wrong button id on the post html. I then changed the button id for the "Edit" button on the post html to correspond with the button id for the edit-event listening function in the comment section javascript. This solved the issue.

Secondly I discovered that when comments have not been approved yet by the admin, they were visible in blur form to not only the maker of the comment, but to other registered users. To fix this, I placed the comment-form variable definition above the post-request condition in the blog views python file. This action solved the issue.


## Contact information

The website developer's contact details are as below:

Email: inekwegoziechukwu@gmail.com

## Acknowledgements and References

- _Blog Post Content_: The contents of the blog posts are real life stories of individuals, extracted from the blog owner's personal testimony and from the book titled "The 5 Resets" written by the Harvard stress expert, Dr. Nerurkar Aditi.

- _User Interface, Experience and Logic Design_: A large part of the UI/UX and website interactivity design ideas were obtained from the mock project- _Boutique Ado_ by the Code Institute.

- _Deployment Terminal_: The deployment terminal used in the project was created by Code Institute.

- _Images_: All images were downloaded from [Pixabay](pixabay.com) and [Unsplash](unsplash.com) free online source, except the image in the About Section of the blog site, which was downloaded from the mock project- _Codestar blog_ by the Code Institute.