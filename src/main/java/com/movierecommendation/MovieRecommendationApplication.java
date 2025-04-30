package com.movierecommendation;

import com.movierecommendation.jdbc.MovieJDBCService;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.*;
import java.util.Map;

@SpringBootApplication
@RestController
@RequestMapping("/api/jdbc")
@CrossOrigin(origins = "*")
public class MovieRecommendationApplication {

    private final MovieJDBCService jdbcService;

    public MovieRecommendationApplication() {
        this.jdbcService = new MovieJDBCService();
        this.jdbcService.initializeDatabase();
    }

    public static void main(String[] args) {
        SpringApplication.run(MovieRecommendationApplication.class, args);
    }

    @PostMapping("/users")
    public Map<String, Object> createUser(@RequestBody Map<String, String> userData) {
        return jdbcService.addUser(userData.get("username"), userData.get("email"));
    }

    @PostMapping("/ratings")
    public Map<String, Object> addRating(@RequestBody Map<String, Object> ratingData) {
        return jdbcService.addRating(
            (Integer) ratingData.get("userId"),
            (String) ratingData.get("movieId"),
            ((Number) ratingData.get("rating")).doubleValue()
        );
    }

    @PostMapping("/watch-history")
    public Map<String, Object> addToWatchHistory(@RequestBody Map<String, Object> watchData) {
        return jdbcService.addToWatchHistory(
            (Integer) watchData.get("userId"),
            (String) watchData.get("movieId")
        );
    }

    @GetMapping("/users/{userId}/history")
    public Map<String, Object> getWatchHistory(@PathVariable int userId) {
        return jdbcService.getUserWatchHistory(userId);
    }

    @GetMapping("/users/{userId}/recommendations")
    public Map<String, Object> getRecommendations(@PathVariable int userId) {
        return jdbcService.getRecommendations(userId);
    }
} 