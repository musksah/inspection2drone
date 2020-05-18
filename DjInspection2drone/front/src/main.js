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
import { store } from './store';
import router from "./router/index";
import Vue from "vue";
import App from "./App";

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
import { library } from '@fortawesome/fontawesome-svg-core'
import { faUserSecret } from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import VeeValidate from 'vee-validate';

Vue.use(VeeValidate);
library.add(faUserSecret)
Vue.component('font-awesome-icon', FontAwesomeIcon)
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
