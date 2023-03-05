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
/* Container */
.header {
  border-top: 10px solid #70c3ed;
  background-color: rgba(112, 195, 237, 0.5);

  display: flex;
  align-items: center;

  overflow: hidden;
}

/* Logo & Title */
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
