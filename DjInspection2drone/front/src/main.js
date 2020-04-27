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
import  VueSession  from  'vue-session';
import Vuetify from 'vuetify';
import 'vuetify/dist/vuetify.min.css';
import { library } from '@fortawesome/fontawesome-svg-core'
import { faUserSecret } from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
// Se importan las tablas a usar
// import DataTables and DataTablesServer together

// Librerías de font-awesome
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
  render: h => h(App)
}).$mount("#app");
