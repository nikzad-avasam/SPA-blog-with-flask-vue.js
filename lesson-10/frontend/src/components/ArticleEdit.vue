<template>
  <div class="container mt-5">
    <div class="alert alert-success">
      <h3>Edit Article</h3>
      <form @submit.prevent="updateArticle">
        <input
          type="text"
          class="form-control mt-3"
          placeholder="enter title here"
          v-model="title"
        />

        <textarea
          cols="30"
          rows="10"
          class="form-control mt-3"
          placeholder="enter content of post here"
          v-model="body"
        ></textarea>

        <button class="mt-3 btn btn-success">PUBLISH ARTICLE</button>
        <div v-if="error" role="alert" class="alert alert-danger mt-3">
          {{ error }}
        </div>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      title: null,
      body: null,
      error: null,
    };
  },
  beforeRouteEnter(to, form, next) {
    if (to.params.id !== undefined) {
      fetch(`http://localhost:5000/get/${to.params.id}/`, {
        method: "GET",
        headers: {
          "Content-Type": "application/json",
        },
      })
        .then((resp) => resp.json())
        .then((data) => {
          return next((vm) => ((vm.title = data.title), (vm.body = data.body)));
        })
        .catch((error) => {
          console.log(error);
        });
    } else {
      return next();
    }
  },
  props: {
    id: {
      type: [Number, String],
      required: true,
    },
  },
  methods: {
    updateArticle() {
      if (!this.title || !this.body) {
        this.error = "pls add all fields in form.";
      } else {
        fetch(`http://localhost:5000/update/${this.id}/`, {
          method: "PUT",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            title: this.title,
            body: this.body,
          }),
        })
          .then((resp) => resp.json())
          .then(() => {
            this.$router.push({
              name: "home",
            });
          })
          .catch((error) => {
            console.log(error);
          });
      }
    },
  },
};
</script>

<style>
</style>