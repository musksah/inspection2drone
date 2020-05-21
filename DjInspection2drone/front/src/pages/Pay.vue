<template>
  <div>
    <m-header></m-header>
    <b-container style="margin-bottom:2rem;margin-top:7rem;">
      <div class="row">
        <div class="col-md-12" style="margin-top:1rem;">
          <h3 class="pricing-table-title text-center" style="color:#454545;font-size:2em !important;margin-bottom:0.5em;">Resumen de la compra</h3>
          <p class="text-center" style="margin-bottom:0;">Has elegido el plan {{ plan.name }}, revisa las características de tu plan y sigue con el proceso de compra</p>
        </div>
        <div
          class="pricing-wrapper clearfix"
          style="margin-bottom:2rem;display:flex;align-items:center; justify-content:center;"
        >
          <!-- Titulo -->
          <div class="pricing-table">
            <h3 class="pricing-title" :style="{background:plan.backgroundcolor, color:'#454545'}">{{ plan.name }}</h3>
            <div class="price">
              ${{ plan.price }}
              <sup>/ mes</sup>
            </div>
            <!-- Lista de Caracteristicas / Propiedades -->
            <ul class="table-list">
              <li>
                {{ plan.photos }}
                <span>Fotografías / mes</span>
              </li>
              <li>
                {{ plan.inspections }}
                <span>Inspecciones / mes</span>
              </li>
              <li>
                {{ plan.analysis }}
                <span>análisis con IA / mes</span>
              </li>
              <li>
                {{ plan.users }}
                <span class="unlimited">Usuario Full</span>
              </li>
            </ul>
            <!-- Contratar / Comprar -->
          </div>
        </div>
      </div>
      <div class="row text-center" style="display:flex;align-items:center; justify-content:center;">
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
          <router-link class="btn btn-secondary mr-2">Volver</router-link>
          <input name="Submit" class="btn btn-success" type="submit" value="Pagar" />
        </form>
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
      payUParams: {
        merchantId: 0,
        accountId: 0,
        description: "null",
        referenceCode: "",
        amount: "null",
        tax: 0,
        taxReturnBase: 0,
        currency: "",
        signature: "",
        test: 0,
        buyerEmail: "",
        responseUrl: "",
        confirmationUrl: ""
      },
      base_instance_axios: {},
      plan: {
        id: 1,
        name: "",
        price:0,
        photos:0,
        inspections:0,
        analysis:0,
        users:0,
        backgroundcolor:"#FA4343"
      },
      credentials:{
        username:"",
        password:""
      }
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
    this.plan = this.$route.params.plan;
    this.credentials = this.$route.params.credentials;
    console.log("Mounted");
    console.log(this.plan);
    console.log(this.credentials);
    // console.log(this.credentials.username);
    // console.log(this.credentials.password);
    this.getPayUInformation();
    this.Login();
  },
  methods: {
    getPayUInformation() {
      // this.plan = this.$route.params.plan;
      const axiosInstance = axios.create(this.base_instance_axios);
      axiosInstance({
        url: "/transaction/go-pay/",
        method: "get",
        params: { plan: this.plan.id }
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
    },
    Login() {
      // checking if the input is valid
      // this.loading = true;
      this.$store
        .dispatch("obtainToken", {
          username: this.credentials.username,
          password: this.credentials.password
        })
        .then(response => {
          this.$store.commit("updateToken", response.data.token);
          this.$store.commit("updateUsername", this.credentials.username);
          this.getPermissions()
            .then(res => {
              this.$store.commit("storePermissions", res.data);
            })
            .catch(e => {
              this.loading = false;
              swal({
                type: "error",
                icon: "error",
                title: "Error",
                text: "El usuaurio no pudo ser creado",
                timer: 3000
              });
            });
        })
        .catch(error => {
          this.loading = false;
          this.fail_login = true;
          setTimeout(() => (this.fail_login = false), 3000);
        });
    },
    getPermissions() {
      const axiosInstance = axios.create(
        this.$store.getters.getBaseInstanceAxios
      );
      return axiosInstance({
        url: "/permissions/",
        method: "get",
        params: {}
      });
    }
  }
};
</script>
<style lang="css">
</style>