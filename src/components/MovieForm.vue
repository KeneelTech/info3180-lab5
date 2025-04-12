<template>
  <div class="movie-form">
    <div v-if="successMessage" class="alert alert-success">
      {{ successMessage }}
    </div>

    <div v-if="errors.length" class="alert alert-danger">
      <ul>
        <li v-for="(error, index) in errors" :key="index">{{ error }}</li>
      </ul>
    </div>


  <form id="movieForm" @submit.prevent="saveMovie" enctype="multipart/form-data">
    <div class="form-group mb-3">
      <label for="title" class="form-label">Movie Title</label>
      <input type="text" name="title" class="form-control" required />
    </div>

    <div class="form-group mb-3">
      <label for="description" class="form-label">Description</label>
      <textarea name="description" class="form-control" required></textarea>
    </div>

    <div class="form-group mb-3">
      <label for="poster" class="form-label">Movie Poster</label>
      <input type="file" name="poster" class="form-control" accept="image/*" required />
    </div>

    <button type="submit" class="btn btn-primary">Submit</button>
  </form>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";

const csrf_token = ref("");
const successMessage = ref("");
const errors = ref([]);

function getCsrfToken() {
  fetch('/api/v1/csrf-token')
    .then((response) => response.json())
    .then((data) => {
      csrf_token.value = data.csrf_token;
    });
}

function saveMovie() {

  errors.value = []; 
  successMessage.value = "";

  const movieForm = document.getElementById('movieForm');
  const formData = new FormData(movieForm);

  fetch("/api/v1/movies", {
    method: 'POST',
    body: formData,
    headers: {
      'X-CSRFToken': csrf_token.value
    }
  })
  .then(response => {
    if (!response.ok) {
      return response.json().then(err => { throw err; });
    }
    return response.json();
  })
  .then(data => {
    successMessage.value = "Movie successfully uploaded!";
    document.getElementById('movieForm').reset();
  })
  .catch(error => {
    if (error.errors) {
      errors.value = error.errors;
    } else {
      errors.value = ["An unexpected error occurred"];
    }
  });
}

onMounted(() => {
  getCsrfToken();
});
</script>