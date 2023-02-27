<script setup></script>

<template>
  <div class="header">
    <img
      src="../assets/logo-placeholder-image.png"
      alt="Logo"
      width="50"
      height="50"
    />

    <span>Endangered Animals Tracker</span>

    <nav>
      <a href="#">Settings</a>
      <a href="#">About</a>
    </nav>
  </div>
</template>

<style scoped>
/* Logo & Title */
.header {
  display: flex;
  align-items: center;

  overflow: hidden;
}

img {
  padding: 2px 10px;
}

span {
  font-size: 24px;
  font-weight: bold;
}

/* Navigation */
nav {
  margin-left: auto;
  order: 2;
}

a:any-link {
  font-size: 20px;
  text-decoration: none;

  color: #000;

  padding: 100% 25px;
}

a:hover {
  background-color: #70c3ed;
}
</style>
