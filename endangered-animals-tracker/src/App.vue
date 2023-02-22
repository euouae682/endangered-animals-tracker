<script setup>
import Header from "./components/Header.vue";
</script>

<template>
  <body>
    <header class="main-header">
      <Header />
    </header>
  </body>
</template>

<style scoped>
body {
  border: 1px solid black;
  width: 1000px;
}

.main-header {
  border: 1px solid black;
  width: 100%;

  background-color: aquamarine;
}
</style>
