<template>
  <div class="weather">
    <div class="uk-container" v-if="!connection_state">
      <div class="spinner" uk-spinner="ratio: 3">
      </div>
    </div>
    <div class="uk-container" v-else>
      <h1>Weather</h1>
      {{ forecast_data[0] }}
      <ul class="uk-list">
        <h3>Wetter Daten für den heutigen Tag {{ new Date }} </h3>
        <li>Stadt: {{ forecast_data[0].name }}</li>
        <li>aktuelle Temperatur: {{ (forecast_data[0].main.temp / 10 ).toFixed(1) }}°C</li>
        <li>min. Temp: {{ (forecast_data[0].main.temp_min / 10 ).toFixed(1) }}°C</li>
        <li>max. Temp: {{ (forecast_data[0].main.temp_max / 10 ).toFixed(1) }}°C</li>
      </ul>
    </div>
    <hr>


  </div>

</template>

<script>
export default {
  computed: {
    connection_state() {
      return this.$store.state.connection.isConnected
    },
    forecast_data() {
      return this.$store.state.weather.forecast
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
