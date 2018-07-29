<template>
  <div class="home">
    <div class="uk-container" v-if="!connection_state">
      <div class="spinner" uk-spinner="ratio: 3">
      </div>
    </div>
    <div class="uk-container" v-else>
      <h1>Home</h1>
      <div uk-grid>
        <div class="uk-card uk-card-hover uk-card-default uk-card-body uk-width-1-3@m" v-for="home in home_data[0]">
          <h3 class="uk-card-title">{{ home.section_name }}</h3>
          <ul class="uk-list">
            <li v-for="url in home.urls">
              <a v-bind:href="'https://' + url" target="_blank" >{{ url }}</a>
            </li>
          </ul>
        </div>
      </div>





  </div>
  </div>
</template>

<script>
export default {
  computed: {
    home_data(){

      return this.$store.state.home
    },
    connection_state() {
      return this.$store.state.connection.isConnected
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
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
