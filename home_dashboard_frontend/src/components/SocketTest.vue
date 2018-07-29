<template>
  <div class="weather">
    <div class="uk-container" v-if="!connection_state">
      <div class="spinner" uk-spinner="ratio: 3">
      </div>
    </div>
    <div class="uk-container" v-else>
      <ul class="uk-list" v-for="message in socketMessages">
        <li>{{ message.name }}</li>
      </ul>
      <button type="button" class="uk-button" name="button" v-on:click="sendMessage">Send</button>
    </div>

  </div>
</template>

<script>
import mapState from 'vuex'
export default {
  computed: {

    connection_state() {
      return this.$store.state.connection.isConnected
    }
  },
  data() {
    return {
      socketMessages: []
    }
  },
  sockets:{
//    connect(){
  //    console.log('Connected');
      //Fired when the socket connects
    //  this.isConnected = true;
  //  },
    //message(data) {
      //console.log(data);
      //this.socketMessages.push(data)
    //},
    //disconnect() {
      //this.isConnected = false;
    //}

  },
  methods: {
    sendMessage() {
      this.$socket.emit('message', { id: 1, name:'test'})
    }
  }
  }

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
