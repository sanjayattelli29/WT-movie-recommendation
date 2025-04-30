package com.movierecommendation.jdbc;

import java.sql.*;
import java.util.ArrayList;
import java.util.List;
import java.util.HashMap;
import java.util.Map;

public class MovieJDBCService {
    private static final String URL = "jdbc:mysql://localhost:3306/movie_user_db";
    private static final String USER = "root";
    private static final String PASSWORD = "sanjay123";

    static {
        try {
            Class.forName("com.mysql.cj.jdbc.Driver");
        } catch (ClassNotFoundException e) {
            throw new RuntimeException("MySQL JDBC Driver not found.", e);
        }
    }

    public void initializeDatabase() {
        try (Connection conn = getConnection()) {
            createTables(conn);
            System.out.println("Database initialized successfully!");
        } catch (SQLException e) {
            throw new RuntimeException("Failed to initialize database", e);
        }
    }

    private Connection getConnection() throws SQLException {
        return DriverManager.getConnection(URL, USER, PASSWORD);
    }

    private void createTables(Connection conn) throws SQLException {
        String createUsersTable = """
            CREATE TABLE IF NOT EXISTS users (
                user_id INT PRIMARY KEY AUTO_INCREMENT,
                username VARCHAR(50) UNIQUE NOT NULL,
                email VARCHAR(100) UNIQUE NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """;

        String createRatingsTable = """
            CREATE TABLE IF NOT EXISTS user_ratings (
                rating_id INT PRIMARY KEY AUTO_INCREMENT,
                user_id INT,
                movie_id VARCHAR(100),
                rating DECIMAL(3,1),
                rated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users(user_id)
            )
        """;

        String createWatchHistoryTable = """
            CREATE TABLE IF NOT EXISTS watch_history (
                history_id INT PRIMARY KEY AUTO_INCREMENT,
                user_id INT,
                movie_id VARCHAR(100),
                watched_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users(user_id)
            )
        """;

        try (Statement stmt = conn.createStatement()) {
            stmt.execute(createUsersTable);
            stmt.execute(createRatingsTable);
            stmt.execute(createWatchHistoryTable);
        }
    }

    public Map<String, Object> addUser(String username, String email) {
        String sql = "INSERT INTO users (username, email) VALUES (?, ?)";
        Map<String, Object> response = new HashMap<>();
        
        try (Connection conn = getConnection();
             PreparedStatement pstmt = conn.prepareStatement(sql, Statement.RETURN_GENERATED_KEYS)) {
            
            pstmt.setString(1, username);
            pstmt.setString(2, email);
            int affectedRows = pstmt.executeUpdate();

            if (affectedRows == 0) {
                throw new SQLException("Creating user failed, no rows affected.");
            }

            try (ResultSet generatedKeys = pstmt.getGeneratedKeys()) {
                if (generatedKeys.next()) {
                    response.put("success", true);
                    response.put("userId", generatedKeys.getInt(1));
                    response.put("message", "User created successfully");
                }
            }
        } catch (SQLException e) {
            response.put("success", false);
            response.put("error", e.getMessage());
        }
        return response;
    }

    public Map<String, Object> addRating(int userId, String movieId, double rating) {
        String sql = "INSERT INTO user_ratings (user_id, movie_id, rating) VALUES (?, ?, ?)";
        Map<String, Object> response = new HashMap<>();
        
        try (Connection conn = getConnection();
             PreparedStatement pstmt = conn.prepareStatement(sql)) {
            
            pstmt.setInt(1, userId);
            pstmt.setString(2, movieId);
            pstmt.setDouble(3, rating);
            pstmt.executeUpdate();
            
            response.put("success", true);
            response.put("message", "Rating added successfully");
        } catch (SQLException e) {
            response.put("success", false);
            response.put("error", e.getMessage());
        }
        return response;
    }

    public Map<String, Object> addToWatchHistory(int userId, String movieId) {
        String sql = "INSERT INTO watch_history (user_id, movie_id) VALUES (?, ?)";
        Map<String, Object> response = new HashMap<>();
        
        try (Connection conn = getConnection();
             PreparedStatement pstmt = conn.prepareStatement(sql)) {
            
            pstmt.setInt(1, userId);
            pstmt.setString(2, movieId);
            pstmt.executeUpdate();
            
            response.put("success", true);
            response.put("message", "Added to watch history successfully");
        } catch (SQLException e) {
            response.put("success", false);
            response.put("error", e.getMessage());
        }
        return response;
    }

    public Map<String, Object> getUserWatchHistory(int userId) {
        Map<String, Object> response = new HashMap<>();
        List<Map<String, Object>> history = new ArrayList<>();
        
        String sql = """
            SELECT w.movie_id, w.watched_at, r.rating 
            FROM watch_history w 
            LEFT JOIN user_ratings r ON w.user_id = r.user_id AND w.movie_id = r.movie_id 
            WHERE w.user_id = ? 
            ORDER BY w.watched_at DESC
        """;
        
        try (Connection conn = getConnection();
             PreparedStatement pstmt = conn.prepareStatement(sql)) {
            
            pstmt.setInt(1, userId);
            ResultSet rs = pstmt.executeQuery();
            
            while (rs.next()) {
                Map<String, Object> movie = new HashMap<>();
                movie.put("movieId", rs.getString("movie_id"));
                movie.put("watchedAt", rs.getTimestamp("watched_at").toString());
                movie.put("rating", rs.getObject("rating")); // might be null
                history.add(movie);
            }
            
            response.put("success", true);
            response.put("history", history);
        } catch (SQLException e) {
            response.put("success", false);
            response.put("error", e.getMessage());
        }
        return response;
    }

    public Map<String, Object> getRecommendations(int userId) {
        Map<String, Object> response = new HashMap<>();
        List<Map<String, Object>> recommendations = new ArrayList<>();
        
        String sql = """
            SELECT DISTINCT r.movie_id, AVG(r.rating) as avg_rating
            FROM user_ratings r 
            WHERE r.movie_id NOT IN (
                SELECT movie_id FROM watch_history WHERE user_id = ?
            )
            AND r.rating >= 4.0
            GROUP BY r.movie_id
            ORDER BY avg_rating DESC
            LIMIT 10
        """;
        
        try (Connection conn = getConnection();
             PreparedStatement pstmt = conn.prepareStatement(sql)) {
            
            pstmt.setInt(1, userId);
            ResultSet rs = pstmt.executeQuery();
            
            while (rs.next()) {
                Map<String, Object> movie = new HashMap<>();
                movie.put("movieId", rs.getString("movie_id"));
                movie.put("averageRating", rs.getDouble("avg_rating"));
                recommendations.add(movie);
            }
            
            response.put("success", true);
            response.put("recommendations", recommendations);
        } catch (SQLException e) {
            response.put("success", false);
            response.put("error", e.getMessage());
        }
        return response;
    }
} 