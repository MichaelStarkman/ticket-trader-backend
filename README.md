# lets-dish-express-api
repository for Let's Dish Express APi


Ticket Trader app


Hosted App Link
-back end link: 
-front end link 

Technology Used
    - HTML, CSS, React
    

Frameworks & Libraries
    -MongoDB Atlas, Mongoose -Node.js, Express

Class
    Ticket
    name = models.CharField(max_length=32)
    venue = models.CharField(max_length=32)
    date = models.DateTimeField
    Date(timestamp)
    Price(int)
    img(Str)


FUTURE FEATURES
    -Image upload capability with Cloudinary
    -User Login so everyone can have a unique experience
    -Possible Google Places API or Yelp for users to search for resturants
    -Use Bootstrap for React


General Assembly Project Requirements
A working full-stack application, built by you, using the MERN stack: Node.js, Mongoose, Express and ReactA working full-stack application, built by you, using the MERN stack: Node.js, Mongoose, Express and React.
Adhere to the MVC file structure: Models, Views, Controllers (Note, in this case views is React in it's own separate repository; there will not be an actual views directory in your Express backend)
At least one model with full CRUD.
At least three react components, defined in their own files, besides App.js.
Be deployed online and accessible to the public via Heroku
❗ Two git repositories not inside the class repo, one for your backend and one for your frontend.

User Story:
    -I was unable to get cloudinary to work due to error message: “Upload preset must be specified when using unsigned upload” 
    -Heroku deployment was successful, but is encountering Application Errors that I am having trouble deciphering

Notes to self:
    Set DateField to accept today and future dates
