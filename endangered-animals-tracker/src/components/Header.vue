<script setup></script>

<template>
  <img
    src="../assets/logo-placeholder-image.png"
    alt="Logo"
    width="50"
    height="50"
  />

  <h1>Endangered Animals Tracker</h1>

  <nav>
    <ul>
      <li><a>Settings</a></li>
      <li><a>About</a></li>
    </ul>
  </nav>
</template>

<style scoped>
* {
  margin: 0;
  padding: 0;
}

/* Logo */
img {
  margin-right: 15px;
}

/* Heading */
h1 {
  display: inline-block;
  margin: 10px;
}

/* Navigation */
ul {
  list-style-type: none;

  height: 100%;
  float: right;
}

li {
  text-align: center;

  height: 100%;
  float: left;

  margin-left: 10px;
}

a {
  font-size: 20px;

  color: black;
  transition: color 0.2s;

  padding: 25px;
}
</style>
