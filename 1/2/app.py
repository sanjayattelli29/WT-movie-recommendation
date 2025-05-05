# from pymongo import MongoClient
import json
import mysql.connector
from mysql.connector import Error

# MongoDB code commented out
"""
# Connect to MongoDB server
client = MongoClient('mongodb://localhost:27017/')

# Create/select a database
db = client['movie_database']  # You can change 'movie_database' to your desired database name

# Create/select a collection (table-like in MongoDB)
movies_collection = db['movies']  # Change 'movies' to your desired collection name
"""

# MySQL connection
try:
    connection = mysql.connector.connect(
        host='localhost',
        database='movie_user_db',
        user='root',
        password='sanjay123'
    )
    
    if connection.is_connected():
        cursor = connection.cursor()
        
        # First, drop the existing table if it exists
        cursor.execute("DROP TABLE IF EXISTS movies")
        
        # Create movies table
        cursor.execute("""
            CREATE TABLE movies (
                movie_id INT PRIMARY KEY AUTO_INCREMENT,
                title VARCHAR(255) NOT NULL,
                year INT,
                genres VARCHAR(255),
                rating DECIMAL(3,1),
                director VARCHAR(255),
                actors TEXT
            )
        """)
        
        # Sample movie data
        movies_data = [
    {
        "title": "Baahubali: The Beginning",
        "year": 2015,
        "genres": ["Action", "Adventure", "Drama"],
        "rating": 8.0,
        "director": "S.S. Rajamouli",
        "actors": ["Prabhas", "Rana Daggubati", "Anushka Shetty", "Tamannaah"]
    },
    {
        "title": "Baahubali: The Conclusion",
        "year": 2017,
        "genres": ["Action", "Adventure", "Drama"],
        "rating": 8.2,
        "director": "S.S. Rajamouli",
        "actors": ["Prabhas", "Rana Daggubati", "Anushka Shetty", "Tamannaah"]
    },
    {
        "title": "RRR",
        "year": 2022,
        "genres": ["Action", "Drama", "History"],
        "rating": 8.0,
        "director": "S.S. Rajamouli",
        "actors": ["N.T. Rama Rao Jr.", "Ram Charan", "Alia Bhatt", "Ajay Devgn"]
    },
    {
        "title": "Magadheera",
        "year": 2009,
        "genres": ["Action", "Fantasy", "Romance"],
        "rating": 7.7,
        "director": "S.S. Rajamouli",
        "actors": ["Ram Charan", "Kajal Aggarwal", "Dev Gill", "Srihari"]
    },
    {
        "title": "Srimanthudu",
        "year": 2015,
        "genres": ["Action", "Drama", "Family"],
        "rating": 7.9,
        "director": "Koratala Siva",
        "actors": ["Mahesh Babu", "Shruti Haasan", "Jagapathi Babu", "Rajendra Prasad"]
    },
    {
        "title": "Eega",
        "year": 2012,
        "genres": ["Fantasy", "Thriller", "Action"],
        "rating": 7.8,
        "director": "S.S. Rajamouli",
        "actors": ["Nani", "Sudeep", "Samantha Ruth Prabhu"]
    },
    {
        "title": "Attarintiki Daredi",
        "year": 2013,
        "genres": ["Comedy", "Drama", "Family"],
        "rating": 7.6,
        "director": "Trivikram Srinivas",
        "actors": ["Pawan Kalyan", "Samantha Ruth Prabhu", "Pranitha Subhash", "Brahmanandam"]
    },
    {
        "title": "Ala Vaikunthapurramuloo",
        "year": 2020,
        "genres": ["Action", "Drama", "Family"],
        "rating": 7.4,
        "director": "Trivikram Srinivas",
        "actors": ["Allu Arjun", "Pooja Hegde", "Tabu", "Murali Sharma"]
    },
    {
        "title": "Kshana Kshanam",
        "year": 1991,
        "genres": ["Action", "Comedy", "Crime"],
        "rating": 7.8,
        "director": "Ramesh Aravind",
        "actors": ["Venkatesh", "Sridevi", "Satyaraj", "Ravi Shankar"]
    },
    {
        "title": "Sye",
        "year": 2004,
        "genres": ["Action", "Sports"],
        "rating": 7.0,
        "director": "S.S. Rajamouli",
        "actors": ["Nithin", "Shriya Saran", "Sushant", "Nawab Shah"]
    },
    {
        "title": "Nannaku Prematho",
        "year": 2016,
        "genres": ["Action", "Drama", "Family"],
        "rating": 7.6,
        "director": "Sukumar",
        "actors": ["NTR Jr.", "Rakul Preet Singh", "Rajendra Prasad", "Jagapathi Babu"]
    },
    {
        "title": "Pelli Sandadi",
        "year": 1996,
        "genres": ["Romance", "Drama"],
        "rating": 7.0,
        "director": "K. Raghavendra Rao",
        "actors": ["Srikanth", "Rupa Gaur", "K. Viswanath", "Jayasudha"]
    },
    {
        "title": "Shankar Dada M.B.B.S",
        "year": 2004,
        "genres": ["Comedy", "Drama"],
        "rating": 7.5,
        "director": "Jayanth C. Paranjee",
        "actors": ["Chiranjeevi", "Sreenu Vaitla", "Shriya Saran", "Sonali Bendre"]
    },
    {
        "title": "Kshana Kshanam",
        "year": 1991,
        "genres": ["Action", "Comedy", "Crime"],
        "rating": 7.8,
        "director": "Ramesh Aravind",
        "actors": ["Venkatesh", "Sridevi", "Satyaraj", "Ravi Shankar"]
    },
    {
        "title": "Baadshah",
        "year": 2013,
        "genres": ["Action", "Comedy", "Crime"],
        "rating": 6.6,
        "director": "Sreenu Vaitla",
        "actors": ["NTR Jr.", "Kajal Aggarwal", "Sampath Raj", "Jaya Prakash Reddy"]
    },
    {
        "title": "Bhale Bhale Magadivoy",
        "year": 2015,
        "genres": ["Comedy", "Romance"],
        "rating": 7.9,
        "director": "Maruthi Dasari",
        "actors": ["Nani", "Lavanya Tripathi", "Murali Sharma", "Raghubabu"]
    },
    {
        "title": "Chiranjeevi",
        "year": 1990,
        "genres": ["Action", "Drama"],
        "rating": 7.2,
        "director": "Raghavendra Rao",
        "actors": ["Chiranjeevi", "Sridevi", "Allu Aravind"]
    },
    {
        "title": "Pawan Kalyan",
        "year": 1996,
        "genres": ["Action", "Drama", "Romance"],
        "rating": 6.9,
        "director": "Renu Desai",
        "actors": ["Pawan Kalyan", "Renu Desai", "Pooja Bedi"]
    },
    {
        "title": "Rangasthalam",
        "year": 2018,
        "genres": ["Drama", "Action", "Romance"],
        "rating": 8.2,
        "director": "Sukumar",
        "actors": ["Ram Charan", "Samantha Ruth Prabhu", "Aadhi Pinisetty", "Jagapathi Babu"]
    },
    {
        "title": "Kshana Kshanam",
        "year": 1991,
        "genres": ["Comedy", "Drama"],
        "rating": 7.0,
        "director": "Ramesh Aravind",
        "actors": ["Venkatesh", "Sridevi", "Satyaraj", "Ravi Shankar"]
    },
    {
        "title": "Maharshi",
        "year": 2019,
        "genres": ["Drama", "Action"],
        "rating": 7.5,
        "director": "Vamsi Paidipally",
        "actors": ["Mahesh Babu", "Pooja Hegde", "Allari Naresh", "Jagapathi Babu"]
    },
    {
        "title": "Nuvvu Naaku Nachav",
        "year": 2001,
        "genres": ["Comedy", "Romance"],
        "rating": 7.6,
        "director": "K. Vijaya Bhaskar",
        "actors": ["Venkatesh", "Aarti Agarwal", "Suman", "Sunil"]
    },
    {
        "title": "Fidaa",
        "year": 2017,
        "genres": ["Romance", "Drama"],
        "rating": 7.7,
        "director": "Sekhar Kammula",
        "actors": ["Varun Tej", "Sai Pallavi", "Saikumar", "Rajendra Prasad"]
    },
    {
        "title": "Raja The Great",
        "year": 2017,
        "genres": ["Action", "Comedy"],
        "rating": 7.2,
        "director": "Anil Ravipudi",
        "actors": ["Ravi Teja", "Radhika Apte", "Maharshi", "Srinivasa Reddy"]
    },
    {
        "title": "Annamayya",
        "year": 1997,
        "genres": ["Action", "Drama"],
        "rating": 7.5,
        "director": "K. Raghavendra Rao",
        "actors": ["Akkineni Nagarjuna", "Ramya Krishna", "K. Viswanath", "Gollapudi Maruti Rao"]
    },
    {
        "title": "Jalsa",
        "year": 2008,
        "genres": ["Action", "Drama", "Romance"],
        "rating": 7.5,
        "director": "Trivikram Srinivas",
        "actors": ["Pawan Kalyan", "Kajal Aggarwal", "Parvati Melton", "Ahuti Prasad"]
    },
    {
        "title": "Srirama Rajyam",
        "year": 2011,
        "genres": ["Drama", "Fantasy"],
        "rating": 7.4,
        "director": "Bapu",
        "actors": ["Nandamuri Balakrishna", "Nayanthara", "Venkatesh", "Sai Kumar"]
    },
    {
        "title": "Toli Prema",
        "year": 1998,
        "genres": ["Romance", "Drama"],
        "rating": 7.8,
        "director": "A. Karunakaran",
        "actors": ["Pawan Kalyan", "Keerthi Reddy", "Srihari", "Ali"]
    },
    {
        "title": "Bhaagamathie",
        "year": 2018,
        "genres": ["Horror", "Thriller"],
        "rating": 7.0,
        "director": "G. Ashok",
        "actors": ["Anushka Shetty", "Unni Mukundan", "Jayaram", "Asha Sharath"]
    },
    {
        "title": "Prathi Roju Pandage",
        "year": 2019,
        "genres": ["Comedy", "Drama"],
        "rating": 7.3,
        "director": "Maruthi Dasari",
        "actors": ["Ravi Teja", "Sai Pallavi", "Kajal Aggarwal", "Srinivasa Reddy"]
    },
    {
        "title": "Chitralahari",
        "year": 2019,
        "genres": ["Drama", "Romance"],
        "rating": 7.1,
        "director": "Kishore Tirumala",
        "actors": ["Sai Dharam Tej", "Kalyani Priyadarshan", "Nivetha Pethuraj", "Posani Krishna Murali"]
    },
    {
        "title": "S/O Satyamurthy",
        "year": 2015,
        "genres": ["Drama", "Action"],
        "rating": 7.2,
        "director": "Trivikram Srinivas",
        "actors": ["Allu Arjun", "Samantha Ruth Prabhu", "Nithya Menen", "Rajendra Prasad"]
    },
    {
        "title": "Dhruva",
        "year": 2016,
        "genres": ["Action", "Thriller"],
        "rating": 7.7,
        "director": "Surender Reddy",
        "actors": ["Ram Charan", "Rakul Preet Singh", "Arvind Swamy", "Navdeep"]
    },
    {
        "title": "Kick",
        "year": 2009,
        "genres": ["Action", "Comedy"],
        "rating": 7.3,
        "director": "Surrender Reddy",
        "actors": ["Ravi Teja", "Kajal Aggarwal", "Illeana", "Sayaji Shinde"]
    },
    {
        "title": "Arya",
        "year": 2004,
        "genres": ["Action", "Romance"],
        "rating": 7.0,
        "director": "Sukumar",
        "actors": ["Allu Arjun", "Anu Mehta", "Siddharth", "Sayaji Shinde"]
    },
    {
        "title": "Adhurs",
        "year": 2010,
        "genres": ["Action", "Comedy", "Romance"],
        "rating": 6.7,
        "director": "V.V. Vinayak",
        "actors": ["NTR Jr.", "Nayantara", "Sheela", "Suman"]
    },
    {
        "title": "Sarrainodu",
        "year": 2016,
        "genres": ["Action", "Drama"],
        "rating": 7.0,
        "director": "Boyapati Srinu",
        "actors": ["Allu Arjun", "Rakul Preet Singh", "Catherine Tresa", "Aadhi Pinisetty"]
    },
    {
        "title": "Kalyan Ram",
        "year": 2016,
        "genres": ["Action", "Drama"],
        "rating": 7.2,
        "director": "Hanu Raghavapudi",
        "actors": ["Kalyan Ram", "Niveda Thomas", "Sai Kumar", "Rajendra Prasad"]
    },
    {
        "title": "Maanagaram",
        "year": 2017,
        "genres": ["Action", "Thriller"],
        "rating": 7.6,
        "director": "Lokesh Kanagaraj",
        "actors": ["Sivakarthikeyan", "Regina Cassandra", "Sree", "Naveen"]
      },
      {
        "title": "Jigarthanda",
        "year": 2014,
        "genres": ["Crime", "Drama", "Thriller"],
        "rating": 8.0,
        "director": "Karthik Subbaraj",
        "actors": ["Siddharth", "Lakshmi Menon", "Bobby Simha"]
      },
      {
        "title": "Aruvi",
        "year": 2016,
        "genres": ["Drama"],
        "rating": 8.0,
        "director": "Kohil",
        "actors": ["Aditi Balan", "Lakshmi Gopalaswamy", "Saara Ramesh"]
      },
      {
        "title": "Vikram Vedha",
        "year": 2017,
        "genres": ["Action", "Thriller"],
        "rating": 8.2,
        "director": "Pushkar-Gayathri",
        "actors": ["Vijay Sethupathi", "R. Madhavan", "Shraddha Srinath"]
      },
      {
        "title": "Kumki",
        "year": 2012,
        "genres": ["Drama", "Romance"],
        "rating": 7.7,
        "director": "Prabhu Solomon",
        "actors": ["Vikram Prabhu", "Lakshmi Menon", "Thambi Ramaiah"]
      },
      {
        "title": "96",
        "year": 2018,
        "genres": ["Romance", "Drama"],
        "rating": 8.4,
        "director": "C. Prem Kumar",
        "actors": ["Trisha Krishnan", "Vijay Sethupathi", "Varsha Bollamma"]
      },
      {
        "title": "Super Deluxe",
        "year": 2019,
        "genres": ["Comedy", "Drama"],
        "rating": 8.0,
        "director": "Thiagarajan Kumararaja",
        "actors": ["Vijay Sethupathi", "Fahadh Faasil", "Samantha Ruth Prabhu"]
      },
      {
        "title": "Kaithi",
        "year": 2019,
        "genres": ["Action", "Thriller"],
        "rating": 8.4,
        "director": "Lokesh Kanagaraj",
        "actors": ["Karthi", "Narain", "Arjun Das"]
      },
      {
        "title": "Vikram",
        "year": 2022,
        "genres": ["Action", "Thriller"],
        "rating": 8.2,
        "director": "Lokesh Kanagaraj",
        "actors": ["Kamal Haasan", "Fahadh Faasil", "Vijay Sethupathi"]
      },
      {
        "title": "Mersal",
        "year": 2017,
        "genres": ["Action", "Drama"],
        "rating": 7.9,
        "director": "Atlee",
        "actors": ["Vijay", "Samantha Ruth Prabhu", "Nithya Menen"]
      },
      {
        "title": "Ratchasan",
        "year": 2018,
        "genres": ["Crime", "Thriller"],
        "rating": 8.3,
        "director": "Ram Kumar",
        "actors": ["Vishnu Vishal", "Amala Paul", "Kaali Venkat"]
      },
      {
        "title": "Kaanal Neer",
        "year": 2020,
        "genres": ["Drama"],
        "rating": 7.5,
        "director": "R. K. Suresh",
        "actors": ["Shanthi Priya", "Ajay"]
      },
      {
        "title": "Vada Chennai",
        "year": 2018,
        "genres": ["Crime", "Drama"],
        "rating": 8.4,
        "director": "Vetrimaaran",
        "actors": ["Dhanush", "Ameer", "Andrea Jeremiah"]
      },
      {
        "title": "Asuran",
        "year": 2019,
        "genres": ["Action", "Drama"],
        "rating": 8.5,
        "director": "Vetrimaaran",
        "actors": ["Dhanush", "Manju Warrier", "Pasupathi"]
      },
      {
        "title": "Nerkonda Paarvai",
        "year": 2019,
        "genres": ["Drama", "Thriller"],
        "rating": 7.8,
        "director": "H. Vinoth",
        "actors": ["Ajith Kumar", "Shraddha Srinath", "Abhirami"]
      },
      {
        "title": "Sivakarthikeyan's Hero",
        "year": 2020,
        "genres": ["Action", "Comedy"],
        "rating": 6.6,
        "director": "P.S. Mithran",
        "actors": ["Sivakarthikeyan", "Kalyani Priyadarshan", "Arjun Sarja"]
      },
      {
        "title": "Kuruthi",
        "year": 2021,
        "genres": ["Action", "Thriller"],
        "rating": 7.4,
        "director": "Manu Warrier",
        "actors": ["Prithviraj Sukumaran", "Murali Gopy", "Srinda Arhaan"]
      },
      {
        "title": "Kaaka Muttai",
        "year": 2015,
        "genres": ["Drama"],
        "rating": 8.2,
        "director": "Manikandan",
        "actors": ["Vignesh", "Ramesh", "Muthuraman"]
      },
      {
        "title": "Kuttram 23",
        "year": 2017,
        "genres": ["Thriller", "Crime"],
        "rating": 7.5,
        "director": "Arivazhagan Venkatachalam",
        "actors": ["Arulnithi", "Saiyami Kher", "Aishwarya Rajesh"]
      },
      {
        "title": "Anjali",
        "year": 1990,
        "genres": ["Drama"],
        "rating": 7.7,
        "director": "Mani Ratnam",
        "actors": ["Ramesh Arvind", "Revathi", "Sridevi"]
      },
      {
        "title": "Vinnai Thandi Varuvaya",
        "year": 2010,
        "genres": ["Romance", "Drama"],
        "rating": 8.1,
        "director": "Gautham Vasudev Menon",
        "actors": ["Silambarasan", "Trisha Krishnan", "K.S. Ravikumar"]
      },
      {
        "title": "Taramani",
        "year": 2017,
        "genres": ["Drama", "Romance"],
        "rating": 7.4,
        "director": "Ram",
        "actors": ["Andrea Jeremiah", "Vasanth Ravi", "Azhagam Perumal"]
      },
      {
        "title": "Sila Samayangalil",
        "year": 2018,
        "genres": ["Drama"],
        "rating": 7.5,
        "director": "P. Ramesh",
        "actors": ["Ashok Selvan", "Vidya Pradeep", "Sriranjani"]
      },
      {
        "title": "Vishwaroopam",
        "year": 2013,
        "genres": ["Action", "Thriller"],
        "rating": 8.0,
        "director": "Kamal Haasan",
        "actors": ["Kamal Haasan", "Rahul Bose", "Pooja Kumar"]
      },
      {
        "title": "Iru Mugan",
        "year": 2016,
        "genres": ["Action", "Sci-Fi"],
        "rating": 6.9,
        "director": "A. L. Vijay",
        "actors": ["Vikram", "Nayanthara", "Nithya Menen"]
      },
      {
        "title": "Jeeva",
        "year": 2014,
        "genres": ["Drama", "Action"],
        "rating": 6.8,
        "director": "Suseenthiran",
        "actors": ["Jiiva", "Nayanthara", "Sampath Raj"]
      },
      {
        "title": "Oru Kuppai Kadhai",
        "year": 2018,
        "genres": ["Drama"],
        "rating": 7.3,
        "director": "Virumandi",
        "actors": ["M.S. Bhaskar", "Nivetha Pethuraj", "Gajaraj"]
      },
      {
        "title": "Kalyana Samayal Saadham",
        "year": 2013,
        "genres": ["Romance", "Comedy"],
        "rating": 7.5,
        "director": "R. S. Prasanna",
        "actors": ["Prasanna", "Lekha Washington", "Sathish"]
      },
      {
        "title": "Malli Raava",
        "year": 2017,
        "genres": ["Romance", "Drama"],
        "rating": 7.7,
        "director": "Gautham Tinnanuri",
        "actors": ["Sree Vishnu", "Aakanksha Singh", "Siva Parvathi"]
      },
      {
        "title": "Anukokunda Oka Roju",
        "year": 2005,
        "genres": ["Thriller", "Crime"],
        "rating": 7.9,
        "director": "Chandra Sekhar Yeleti",
        "actors": ["Charmy Kaur", "Srikant", "Sunil"]
      },
      {
        "title": "Sye",
        "year": 2004,
        "genres": ["Drama", "Sports"],
        "rating": 7.7,
        "director": "Sekhar Kammula",
        "actors": ["Nitin", "Shashank", "Genelia D'Souza"]
      },
      {
        "title": "Pellichoopulu",
        "year": 2016,
        "genres": ["Romance", "Comedy"],
        "rating": 7.8,
        "director": "Tharun Bhascker",
        "actors": ["Vijay Devarakonda", "Ritu Varma", "Nassar"]
      },
      {
        "title": "Thiruttu Payale 2",
        "year": 2017,
        "genres": ["Thriller", "Crime"],
        "rating": 6.6,
        "director": "Susi Ganesan",
        "actors": ["Bobby Simha", "Amala Paul", "Prasanna"]
      }
]


# Insert each movie record
    insert_query = """
        INSERT INTO movies (title, year, genres, rating, director, actors)
        VALUES (%s, %s, %s, %s, %s, %s)
    """

    for movie in movies_data:
        title = movie.get("title")
        year = movie.get("year")
        genres = json.dumps(movie.get("genres"))  # Store as JSON string
        rating = movie.get("rating")
        director = movie.get("director")
        actors = json.dumps(movie.get("actors"))  # Store as JSON string

        cursor.execute(insert_query, (title, year, genres, rating, director, actors))

    connection.commit()
    print("All movie data inserted successfully.")
except Error as e:
    print(f"Error: {e}")
# MongoDB code commented out
"""
# Insert the data into the MongoDB collection
movies_collection.insert_many(movies_data)

print("Movies inserted successfully!")
"""
