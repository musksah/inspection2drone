<template>
  <div>
    <m-header></m-header>
    <b-container style="margin-top:7rem;">
        <p>Page Response</p>
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
      base_instance_axios:""
    }
  },
  components: {
    "m-header": StarterHeader,
    StarterFooter
  },
  beforeMount() {
    this.base_instance_axios = this.$store.getters.getBaseInstanceAxios;
  },
  mounted() {
      this.registerPay();
      console.log("Mounted");
      console.log(this.$route.query); 
  },
  methods: {
    registerPay(){
      const axiosInstance = axios.create(this.base_instance_axios);
      axiosInstance({
        url: "/transaction/go-pay/",
        method: "get",
        params: { plan: this.plan.id }
      })
        .then(res => {
          this.payUParams = res.data.data_pay_u;
        })
        .catch(e => {
          this.loading = false;
          swal({
            type: "error",
            icon: "error",
            title: "Error",
            text: "El usaurio no puedo ser creado",
            timer: 3000
          });
        });
    }
  },
};
</script>
