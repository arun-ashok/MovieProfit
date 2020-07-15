# Movies
A movie actor wants to make the max. money by picking the right movies in a given year.
Rules:
Consider that the actor gets a fixed amount of 1 Crore for each movie that he does, irrespective ofthe duration of the money. 
Movies have a contract where the actor is not allowed to work on other movies whose date conflicts with the selected movies date. 
For example if the actor have selected a movie from 10th Jan to 20th Jan (both dates inclusive) then the actor can’t select any movies 
which has a start or end date between 10th to 20th Jan.
Actors are not worried about optimization of ‘less work and more money’. His aim is to get the max. money 
even if he has to work for all the days of the year.

This is a REST API where the actor can submit the data containing the list of movies with movie name, start date and end date and 
the API will return the total amount that he can make along with the final list of movies to select.


**Steps to run the project:**

**1.Open CMD**

**2. Clone the repository from git**
        
        > git clone https://github.com/arun-ashok/Movies.git
        
**2. Enter into folder 'Movies'**

        > cd Movies
        
**3. Make sure python3 is installed.**

       >python --version
       Python 3.7.2
       
**4. Install virtulenv and create a vitual environment**

        > pip install virtualenv
        > virtualenv <virtualenv_name>
        > <virtualenv_name>\Scripts\activate
        
**4. Install the required packages from requirements.txt file**

        > pip install -r requirements.txt

**5. Run the server**

        > python -m Movies
        
 * Serving Flask app "__main__" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 210-114-321
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
        
Server starts listening to APIs.


**6. From POSTMAN , give input in JSON format.**

API :**http://localhost:5000/movies/v1/profit**
Request Type: **POST**

Sample Input :

[
        {
        "movie_name":"KGF",
        "start_date":"04 Feb",
        "end_date":"24 Feb"
        },
        {
		"movie_name": "Bala",
		"start_date": "08 Jan",
		"end_date": "28 Jan"
	    },
        {
		"movie_name": "Rock",
		"start_date": "20 Jan",
		"end_date": "30 Jan"
	    }
    ]
    
    
  Sample Output:
  
  {
  "movies": [
    {
      "end_date": "28 Jan",
      "movie_name": "Bala",
      "start_date": "08 Jan"
    },
    {
      "end_date": "24 Feb",
      "movie_name": "KGF",
      "start_date": "04 Feb"
    }
  ],
  "profit": 2
}





"movies" are the list of movies he can select and "profit" gives the maximum profit he can make.



 
