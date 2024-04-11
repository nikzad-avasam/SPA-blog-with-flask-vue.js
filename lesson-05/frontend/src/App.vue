<template>
  <div id="app" class="container">
    <NavbarMain />
    <router-view />
  </div>
</template>
<script>
import NavbarMain from "./components/NavbarMain.vue";

export default {
  name: "App",
  components: {
    NavbarMain,
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
