<script setup>
import Header from "./components/Header.vue";
import Aside from "./components/Aside.vue";
import Article from "./components/Article.vue";
import Footer from "./components/Footer.vue";
</script>

<template>
  <Header class="header" />

  <div class="container">
    <Aside class="aside" />
    <Article class="article" />
  </div>

  <Footer class="footer" />
</template>

<style scoped>
/* LAYOUT */
.aside {
  width: 25%;
}
</style>
