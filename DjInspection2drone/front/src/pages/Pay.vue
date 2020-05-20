<template>
  <div>
    <m-header></m-header>
    <b-container style="margin-top:10rem;">
      <form method="post" action="https://sandbox.checkout.payulatam.com/ppp-web-gateway-payu/">
        <input name="merchantId" type="hidden" v-model="payUParams.merchantId" />
        <input name="accountId" type="hidden" v-model="payUParams.accountId" />
        <input name="description" type="hidden" v-model="payUParams.description" />
        <input name="referenceCode" type="hidden" v-model="payUParams.referenceCode" />
        <input name="amount" type="hidden" v-model="payUParams.amount" />
        <input name="tax" type="hidden" v-model="payUParams.tax" />
        <input name="taxReturnBase" type="hidden" v-model="payUParams.taxReturnBase" />
        <input name="currency" type="hidden" v-model="payUParams.currency" />
        <input name="signature" type="hidden" v-model="payUParams.signature" />
        <input name="test" type="hidden" v-model="payUParams.test" />
        <input name="buyerEmail" type="hidden" v-model="payUParams.buyerEmail" />
        <input name="responseUrl" type="hidden" v-model="payUParams.responseUrl" />
        <input name="confirmationUrl" type="hidden" v-model="payUParams.confirmationUrl" />
        <input name="Submit" type="submit" value="Enviar" />
      </form>
    </b-container>
    <div class="pricing-wrapper clearfix" style="margin-top:9rem; margin-bottom:3rem;">
      <!-- Titulo -->
      <h1
        class="pricing-table-title text-center"
        style="color:#454545;"
      >Tabla de Precios DroneIAnalyzer</h1>
      <div class="pricing-table">
        <h3 class="pricing-title" style="background: #E3D83D; color:#454545;">Oro</h3>
        <div class="price">
          $100
          <sup>/ mes</sup>
        </div>
        <!-- Lista de Caracteristicas / Propiedades -->
        <ul class="table-list">
          <li>
            20
            <span>Fotografías / mes</span>
          </li>
          <li>
            4
            <span>Inspecciones / mes</span>
          </li>
          <li>
            10
            <span>análisis con IA / mes</span>
          </li>
          <li>
            2
            <span class="unlimited">Usuarios Full</span>
          </li>
        </ul>
        <!-- Contratar / Comprar -->
        <div class="table-buy">
          <p>
            $100
            <sup>/ mes</sup>
          </p>
          <router-link class="pricing-action" :to="{name:'pay'}">Comprar</router-link>
        </div>
      </div>
    </div>
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
      payUParams:{
        merchantId:0,
        accountId:0,
        description:"null",
        referenceCode:"",
        amount:"null",
        tax:0,
        taxReturnBase:0,
        currency:"",
        signature:"",
        test:0,
        buyerEmail:"",
        responseUrl:"",
        confirmationUrl:"",
      },
      base_instance_axios: {},
      plan:1
    };
  },
  components: {
    "m-header": StarterHeader,
    StarterFooter
  },
  beforeMount() {
    this.base_instance_axios = this.$store.getters.getBaseInstanceAxios;
  },
  mounted() {
    this.getPayUInformation();
  },
  methods: {
    getPayUInformation() {
      const axiosInstance = axios.create(this.base_instance_axios);
      axiosInstance({
        url: "/transaction/go-pay/",
        method: "get",
        params: {'plan':this.plan}
      })
        .then(res => {
          console.log(res);
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
  }
};
</script>
<style lang="css">
</style>