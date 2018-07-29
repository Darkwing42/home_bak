<template>
  <div id="app">
    <nav class="uk-navbar-container" uk-navbar>
    <div class="uk-navbar-left">

        <ul class="uk-navbar-nav">
            <li class="uk-active"><router-link to="/">Home-Dashboard</router-link></li>
            <li class="uk-active"><router-link to="/todo">Todo-List</router-link></li>
            <li class="uk-active"><router-link to="/weather">Weather</router-link></li>
            

        </ul>

    </div>
</nav>
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App',
  created(){
    this.$socket.emit('home_data')
    this.$socket.emit('todo_data')
    this.$socket.emit('weather_data', 'Bochum')

  },
}
</script>

<style>
.spinner {
  margin: 0;
  position: absolute;
  top: 50%;
  left: 50%;
  margin-right: -50%;
  transform: translate(-50%, -50%)
}
</style>
