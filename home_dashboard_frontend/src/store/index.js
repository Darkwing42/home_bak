import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import vm from '../main'
Vue.use(Vuex)
const URL = 'http://api.openweathermap.org/data/2.5/weather?q=Bochum,de&&appid=6b21dea1b860e078964f59ba1c075972'
const forecast_URL = 'http://api.openweathermap.org/data/2.5/forecast?q=Bochum,de&&appid=6b21dea1b860e078964f59ba1c075972'
export default new Vuex.Store({
  state: {
    message:'',
    connection: {
      isConnected: false,

    },
    home: [],
    todo:{
      todo_list: []
    },
    weather: {
      api_key: '6b21dea1b860e078964f59ba1c075972',
      forecast: [],
      iconURL:'',
      loading: true
    }

  },
  mutations: {
    updateWeather(state, forecast) {
      state.weather.forecast = forecast
      state.weather.iconURL = 'http://openweathermap.org/img/w/' + forecast.weather[0].icon + '.png'
    },
    changeLoadingStatus(state, loading) {
      state.loading = loading
    },
    SOCKET_CONNECT(state) {
      state.connection.isConnected = true;
      console.log('SOCKET CONNECTED');
    },
    SOCKET_DISCONNECT(state) {
      state.connection.isConnected = false;
    },
    SOCKET_message(state, message) {
      console.log('GOT MESSAGE');
      console.log(message);
    },
    SOCKET_HELLO_WORLD(state, message) {
      state.message = message
    },
    SOCKET_HOME_DATA(state, payload) {
      state.home = payload
    },
    SOCKET_TODO_DATA(state, payload) {
      state.todo.todo_list = payload
    },
    SOCKET_WEATHER_DATA(state, payload) {
      state.weather.forecast = payload
    }

  },
  getters: {},
  actions: {
    GET_WEATHER({commit}){
      axios.get(URL).then((response) => {
        console.log(response.data, this)
        commit('updateWeather', response.data)
      })
    }
  }


})
