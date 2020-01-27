<template>
  <div id="app">
    <header>
      <img alt="Vue logo" src="./assets/logo.png">
      <nav class="topnav">
        <ul>
          <li class="nav-item"><router-link :to="{name: 'home'}">Home</router-link></li>
          <li class="nav-item"><router-link :to="{name: 'about'}">About</router-link></li>
          <li class="nav-item"><router-link :to="{name: 'routine-list'}">Routines</router-link></li>
        </ul>
      </nav>
    </header>
    <main>
      <router-view>
      </router-view>
    </main>
  </div>
</template>

<script>
export default {
  name: 'app',
};
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
.topnav ul {
  list-style-type: none;
  margin: 0 auto;
  width: 100px;
  padding: 0;
}
.topnav li.nav-item {
  display: inline;
  padding: 0.4rem;
}
</style>
