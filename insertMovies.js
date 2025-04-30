const { MongoClient } = require('mongodb');
const movies = require('./movies.json'); // <-- your JSON file with movies

async function main() {
    const uri = 'mongodb://localhost:27017'; // your MongoDB connection string
    const client = new MongoClient(uri);

    try {
        await client.connect();
        const db = client.db('moviesDB'); // your database name
        const collection = db.collection('movies');

        // Optional: Delete existing movies first
        await collection.deleteMany({});

        // Insert all movies
        const result = await collection.insertMany(movies);
        console.log(`${result.insertedCount} movies inserted successfully.`);
    } catch (err) {
        console.error('Error inserting movies:', err);
    } finally {
        await client.close();
    }
}

main();
