<template>
  <div class="container alert alert-primary">
    <h2 class="display-4">{{ article.title }}</h2>
    <p>{{ article.body }}</p>
    <p>{{ article.date }}</p>
    <hr />
    <button @click="deleteArticle" class="btn btn-danger">DELETE</button>
    <router-link :to="{name:'articleedit',params:{id:article.id}}" class="btn btn-success"> EDIT</router-link>
  </div>
</template>

<script>
export default {
  data() {
    return {
      article: {},
    };
  },
  props: {
    id: {
      type: [Number, String],
      required: true,
    },
  },
  methods: {
    deleteArticle() {
      if (confirm("are you suer ? ")) {
        // if user click ok
        fetch(`http://localhost:5000/delete/${this.id}/`, {
          method: "DELETE",
          headers: {
            "Content-Type": "application/json",
          },
        })
          .then(() => {
            this.$router.push({ name: "home" });
          })
          .catch((error) => {
            console.log(error);
          });
      }
    },
    getArticleData() {
      fetch(`http://localhost:5000/get/${this.id}/`, {
        method: "GET",
        headers: {
          "Content-Type": "application/json",
        },
      })
        .then((resp) => resp.json())
        .then((data) => {
          this.article = data;
          console.log(data);
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
  created() {
    this.getArticleData();
  },
};
</script>

<style>
</style>