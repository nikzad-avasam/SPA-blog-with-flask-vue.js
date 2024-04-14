<template>
  <div class="container">
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
      <router-link class="navbar-brand text-style" to="/">FLAS+VuEJS</router-link>
      <button
        class="navbar-toggler"
        type="button"
        data-toggle="collapse"
        data-target="#navbarNavAltMarkup"
        aria-controls="navbarNavAltMarkup"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
        <div class="navbar-nav">
          <router-link class="nav-item nav-link" to="/">Home</router-link>
        </div>
        <div class="navbar-nav btn btn-secondary btn-block ">
          <router-link class="nav-item nav-link text-light" to="/create">Create</router-link>
        </div>
      </div>
    </nav>
  </div>
</template>
<script>
</script>
<style>
</style>