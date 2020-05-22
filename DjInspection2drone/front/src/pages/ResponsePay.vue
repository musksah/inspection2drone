<template>
  <div>
    <m-header></m-header>
    <b-container style="margin-top:12rem;margin-bottom:4rem;">
      <div class="text-center">
        <img src="@/assets/img/pay_done.png" alt="Pago Aceptado" />
      </div>
      <h3 class="text-center">Tú pago ha sido Aceptado</h3>
      <p class="text-center">Ya puedes disfrutar de nuestros servicios</p>
      <div class="text-center">
        <router-link style="font-size:1.3rem;" :to="{name:'dashboard'}" >Ir al dashboard</router-link>
      </div>
    </b-container>
    <starter-footer></starter-footer>
  </div>
</template>
<script>
import axios from "axios";
import StarterHeader from "@/layout/website/StarterHeader";
import StarterFooter from "@/layout/website/StarterFooter";
export default {
  data() {
    return {
      base_instance_axios: "",
      data_response: {},
      plan_id: ""
    };
  },
  components: {
    "m-header": StarterHeader,
    StarterFooter
  },
  beforeMount() {
    this.plan_id = this.$store.state.plan_tranc_id;
    console.log(" RP plan_id ");
    console.log(this.plan_id);
    this.base_instance_axios = this.$store.getters.getBaseInstanceAxios;
    console.log("Mounted");
    console.log(this.$route.query);
    this.data_response = this.$route.query;
    this.data_response.plan_id = this.$store.state.plan_tranc_id;
  },
  mounted() {
    this.storePay();
  },
  methods: {
    storePay() {
      const axiosInstance = axios.create(this.base_instance_axios);
      axiosInstance({
        url: "/transaction/store-pay/",
        method: "POST",
        params: { data_response: this.data_response }
      })
        .then(res => {
          console.log("Response axios django");
          console.log(res);
        })
        .catch(e => {
          this.loading = false;
          swal({
            type: "error",
            icon: "error",
            title: "Error",
            text: "El pago no fue guardado",
            timer: 3000
          });
        });
    }
  }
};
</script>
