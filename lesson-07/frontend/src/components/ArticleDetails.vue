<template>
    <div class="container alert alert-primary">
        <h2 class="display-4">{{ article.title }}</h2>
        <p>{{ article.body }}</p>
        <p>{{ article.date }}</p>
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
    getArticleData() {
      fetch(`http://localhost:5000/get/${this.id}/`, {
        method: "GET",
        headers: {
          "Content-Type": "application/json",
        },
      })
        .then((resp) => resp.json())
        .then((data) => {
          this.article = data
          console.log("WWWWWWWWWWWWWWWWWWWWWWWWWWWW")
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