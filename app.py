from pymongo import MongoClient
import json

# Connect to MongoDB server
client = MongoClient('mongodb://localhost:27017/')

# Create/select a database
db = client['movie_database']  # You can change 'movie_database' to your desired database name

# Create/select a collection (table-like in MongoDB)
movies_collection = db['movies']  # Change 'movies' to your desired collection name

# Sample movie data in JSON format (from the previous message)
movies_data = [
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


# Insert the data into the MongoDB collection
movies_collection.insert_many(movies_data)

print("Movies inserted successfully!")
