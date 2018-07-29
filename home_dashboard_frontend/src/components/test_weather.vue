<template>
  <div class="weather">
    <div class="uk-container" v-if="!connection_state">
      <div class="spinner" uk-spinner="ratio: 3">
      </div>
    </div>



      <div class="uk-container" v-else>

        <p>Getting Weather Date</p>  

      </div>
</template>

<script>
import mapState from 'vuex'
export default {

  computed: {
    connection_state() {
      return this.$store.state.connection.isConnected
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.spinner {
  margin: 0;
  position: absolute;
  top: 50%;
  left: 50%;
  margin-right: -50%;
  transform: translate(-50%, -50%)
}
</style>
