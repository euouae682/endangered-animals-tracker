<script setup>
import Header from "./components/Header.vue";
import Aside from "./components/Aside.vue";
import Article from "./components/Article.vue";
import Footer from "./components/Footer.vue";
</script>

<template>
  <Header class="header" />

  <div class="main-body">
    <Aside class="aside" />
    <Article class="article" />
  </div>

  <Footer class="footer" />
</template>

<style scoped>
/* MAIN BODY */
.main-body {
  display: flex;
}

.aside {
  width: 20%;
}

.article {
  width: 80%;
}
</style>
