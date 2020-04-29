/*!

 =========================================================
 * Vue Paper Dashboard - v2.0.0
 =========================================================

 * Product Page: http://www.creative-tim.com/product/paper-dashboard
 * Copyright 2019 Creative Tim (http://www.creative-tim.com)
 * Licensed under MIT (https://github.com/creativetimofficial/paper-dashboard/blob/master/LICENSE.md)

 =========================================================

 * The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

 */
import Vue from "vue";
import App from "./App";
import router from "./router/index";

import PaperDashboard from "./plugins/paperDashboard";
import "vue-notifyjs/themes/default.css";
import { BootstrapVue, IconsPlugin, CarouselPlugin } from 'bootstrap-vue';
import VueSession from 'vue-session';
import Vuetify from 'vuetify';
import 'vuetify/dist/vuetify.min.css';

import axios from 'axios'
import VueAxios from 'vue-axios'
import jwt_decode from 'jwt-decode'
import Vuex from 'vuex'
// Se importan las tablas a usar
// import DataTables and DataTablesServer together

Vue.use(Vuex);
Vue.use(VueAxios, axios);

const store = new Vuex.Store({
  state: {
    jwt: localStorage.getItem('t'),
    username:"",
    endpoints: {
      obtainJWT: 'http://127.0.0.1:8000/api/v1.0/auth/obtain_token/',
      refreshJWT: 'http://127.0.0.1:8000/api/v1.0/auth/refresh_token/'
    },
    // configJWT: {
    //   headers: {
    //     Authorization: "Bearer " + yourJWTToken
    //   }
    // }
  },
  getters:{
    getBaseInstanceAxios: state =>{
      return  {
        baseURL: "http://127.0.0.1:8000/api/v1.0/",
        headers: {
          Authorization: `JWT ${state.jwt}`,
          "Content-Type": "application/json"
        },
        xhrFields: {
          withCredentials: true
        }
      };
    }
  },
  mutations: {
    updateToken(state, newToken) {
      localStorage.setItem('t', newToken);
      state.jwt = newToken;
    },
    removeToken(state) {
      localStorage.removeItem('t');
      state.jwt = null;
    },
    updateUsername(state, username){
      localStorage.setItem('username',username);
      state.username = username;
    }
  },
  actions: {
    obtainToken(context, credentials) {
      const payload = {
        username: credentials.username,
        password: credentials.password
      }
      return axios.post(this.state.endpoints.obtainJWT, payload);
    },
    refreshToken() {
      const payload = {
        token: this.state.jwt
      }
      axios.post(this.state.endpoints.refreshJWT, payload)
        .then((response) => {
          this.commit('updateToken', response.data.token)
        })
        .catch((error) => {
          console.log(error)
        })
    },
    inspectToken() {
      // WE WILL ADD THIS LATER
      const token = this.state.jwt;
      if (token) {
        const decoded = jwt_decode(token);
        const exp = decoded.exp
        const orig_iat = decode.orig_iat
        if (exp - (Date.now() / 1000) < 1800 && (Date.now() / 1000) - orig_iat < 628200) {
          this.dispatch('refreshToken')
        } else if (exp - (Date.now() / 1000) < 1800) {
          // DO NOTHING, DO NOT REFRESH          
        } else {
          // PROMPT USER TO RE-LOGIN, THIS ELSE CLAUSE COVERS THE CONDITION WHERE A TOKEN IS EXPIRED AS WELL
        }
      }
    },
    // WE WILL ADD THIS LATER
  }
});

// const store = new Vuex.Store({
//   state: {
//     count: 1
//   },
//   mutations: {
//     increment (state) {
//       state.count++
//     }
//   }
// });


// CommonJS
Vue.use(PaperDashboard);
// Install BootstrapVue
Vue.use(BootstrapVue)
// Optionally install the BootstrapVue icon components plugin
Vue.use(IconsPlugin)
Vue.use(CarouselPlugin)
Vue.use(Vuetify)
Vue.use(VueSession)


/* eslint-disable no-new */
new Vue({
  router,
  render: h => h(App),
  store: store
}).$mount("#app");
