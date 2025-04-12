<template>
    <div class="movies-view">
      <h1>Movie Collection</h1>
      <div class="movie-grid">
        <div v-for="movie in movies" :key="movie.id" class="movie-card">
          <img :src="movie.poster" :alt="movie.title" class="movie-poster" />
          <h3>{{ movie.title }}</h3>
          <p>{{ movie.description }}</p>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted } from "vue";
  
  const movies = ref([]);
  
  function fetchMovies() {
    fetch("/api/v1/movies")
      .then(response => response.json())
      .then(data => {
        movies.value = data.movies;
      })
      .catch(error => {
        console.error("Error fetching movies:", error);
      });
  }
  
  onMounted(() => {
    fetchMovies();
  });
  </script>
  
  <style scoped>
  .movie-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    gap: 20px;
  }
  .movie-card {
    border: 1px solid #ddd;
    padding: 15px;
    border-radius: 8px;
  }
  .movie-poster {
    max-width: 100%;
    height: auto;
  }
  </style>