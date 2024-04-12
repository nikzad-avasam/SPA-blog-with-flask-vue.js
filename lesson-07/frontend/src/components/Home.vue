<template>
  <div>
    <h1 class="p-3 mb-2 bg-danger text-white">this is Home Page</h1>
    <div class="container mt-5">
      <div
        v-for="article in articles"
        :key="article.id"
        class="alert alert-dark"
      >
        <h3>
          <router-link :to="{name:'details',params:{id:article.id}}">{{ article.title }}</router-link>
        </h3>
        <p>{{ article.date }}</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  methods: {
    getArticles() {
      fetch("http://localhost:5000/get", {
        method: "GET",
        headers: {
          "Content-Type": "application/json",
        },
      })
        .then((resp) => resp.json())
        .then((data) => {
          this.articles.push(...data);
          console.log(data);
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
  created() {
    this.getArticles();
  },
  data() {
    return {
      articles: [],
    };
  },
};
</script>

<style>
</style>