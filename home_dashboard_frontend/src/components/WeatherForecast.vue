<template>
  <div class="weather">
    <div class="uk-container">
      <h1>Weather</h1>
      <div class="uk-grid">
        <div class="uk-card uk-card-default uk-card-body uk-width-1-3@m" >
          <h3 class="uk-card-title">Wetter für {{ weather.forecast.name }}</h3>
          <ul class="uk-list">
            <li>Temperatur: {{ weather.forecast.main.temp / 10}} °C</li>
            <li>{{ weather.forecast.weather[0].main }} <img :src='weather.iconURL' /> </li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import mapState from 'vuex'
export default {
  created() {
    console.log('Ich werde ausgeführt');
    this.$store.dispatch('GET_WEATHER')
    this.$store.dispatch('GET_FORCAST')
    
  },
  computed: {
    weather() {
      console.log('test');
      return this.$store.state.weather
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
