<script setup>
import Header from "./components/Header.vue";
import Aside from "./components/Aside.vue";
import Article from "./components/Article.vue";
import Footer from "./components/Footer.vue";

const fetchItems = async (url) => {
    const res = await fetch(url, {
      'methods':'GET',
      headers : {
        'Content-Type':'application/json'
      }
    });
    const data = await res.json();
    console.log(data)
    return data;
  } 
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
  flex: 0 0 20%;
}

.article {
  flex: 1;
}
</style>
