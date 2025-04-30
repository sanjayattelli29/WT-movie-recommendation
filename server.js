const express = require('express');
const mongoose = require('mongoose');
const cors = require('cors');

// Initialize Express
const app = express();
const port = 5000;

// Middleware setup
app.use(cors());
app.use(express.json());

// MongoDB URI (replace with your own if using MongoDB Atlas)
const dbURI = 'mongodb://localhost:27017/movie_database';

// MongoDB connection
mongoose.connect(dbURI, { useNewUrlParser: true, useUnifiedTopology: true })
  .then(() => console.log('Connected to MongoDB'))
  .catch((err) => console.log('Error connecting to MongoDB:', err));

// Define movie schema
const movieSchema = new mongoose.Schema({
  title: String,
  genres: [String],
  rating: Number,
  year: Number,
  director: String,
  actors: [String],
  poster: String,
});

// Create Movie model
const Movie = mongoose.model('Movie', movieSchema);

// GET route to fetch movies with filters
app.get('/api/movies', async (req, res) => {
  try {
    // Get filter parameters from query string
    const { genre, minRating, maxRating, year } = req.query;

    // Build a filter object based on the query parameters
    const filter = {};

    if (genre) {
      filter.genres = { $in: [genre] };  // Matches if genre is in the array
    }
    if (minRating) {
      filter.rating = { $gte: parseFloat(minRating) };  // Matches movies with rating greater than or equal to minRating
    }
    if (maxRating) {
      filter.rating = { ...filter.rating, $lte: parseFloat(maxRating) };  // Matches movies with rating less than or equal to maxRating
    }
    if (year) {
      filter.year = parseInt(year);  // Matches movies from a specific year
    }

    // Query the movies collection with the filters
    const movies = await Movie.find(filter);

    res.json(movies);
  } catch (error) {
    console.log(error);
    res.status(500).send('Error retrieving movies');
  }
});

// Start the server
app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
