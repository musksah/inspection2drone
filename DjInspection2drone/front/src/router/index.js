import Vue from "vue";
import VueRouter from "vue-router";
import routes from "./routes";
Vue.use(VueRouter);

// configure router
const router = new VueRouter({
  scrollBehavior() {
    return { x: 0, y: 0 };
  },
  routes, // short for routes: routes
  linkActiveClass: "active"
});

export default router;
