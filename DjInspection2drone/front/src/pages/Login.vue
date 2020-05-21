<template>
  <div>
    <m-header></m-header>
    <center>
      <main class="login-form" style="margin-top:7rem !important; margin-bottom:2rem !important;">
        <div class="cotainer">
          <div class="row justify-content-center">
            <div class="col-md-6">
              <div class="card" style="background-color:#ECECEC;">
                <div
                  class="card-header pb-3"
                  style="font-weight:700;background-color: #455199;color:white;"
                >Iniciar Sesión</div>
                <div class="card-body">
                  <v-layout
                    row
                    fill-height
                    justify-center
                    align-center
                    v-if="loading"
                    style="display:flex;justify-content:center;"
                  >
                    <v-progress-circular :size="50" color="primary" indeterminate />
                  </v-layout>
                  <!-- <form action method class="mt-3" @submit.prevent="Login"> -->
                  <v-form ref="form" @submit.prevent="Login" class="mt-3">
                    <div class="form-group row" style="display:flex;justify-content:center;">
                      <div class="col-md-7">
                        <v-text-field
                          v-model="credentials.username"
                          :counter="70"
                          label="usuario"
                          maxlength="70"
                          required
                          color="red lighten-3"
                        />
                      </div>
                    </div>

                    <div
                      class="form-group row"
                      style="margin-bottom:0;display:flex;justify-content:center;"
                    >
                      <div class="col-md-7">
                        <v-text-field
                          type="password"
                          v-model="credentials.password"
                          :counter="20"
                          label="contraseña"
                          maxlength="20"
                          required
                        />
                      </div>
                    </div>
                    <div
                      class="row form-group mb-2"
                      style="margin-bottom:0;display:flex;justify-content:center;"
                    >
                      <div v-if="fail_login" class="col-md-7 mb-2 text-left">
                        <span style="color:#C62020;font-weight:700;">Usuario o contraseña incorrecta</span>
                      </div>
                    </div>
                    <div class="row" style="display:flex;justify-content:center;">
                      <div class="col-md-6 mb-2">
                        <button type="submit" class="btn btn-danger">Ingresar</button>
                      </div>
                    </div>
                    <div class="row" style="display:flex;justify-content:center;">
                      <div class="col-md-6">
                        <router-link to="/register">¿Olvidó su contraseña?</router-link>
                      </div>
                    </div>
                    <div class="row" style="display:flex;justify-content:center;">
                      <div class="col-md-6 mb-2">
                        <router-link to="/register">Registrarse</router-link>
                      </div>
                    </div>
                    <!-- </form> -->
                  </v-form>
                </div>
              </div>
            </div>
          </div>
        </div>
      </main>
    </center>
    <starter-footer></starter-footer>
  </div>
</template>

<script>
import axios from "axios";
import swal from "sweetalert";
import StarterHeader from "@/layout/website/StarterHeader";
import StarterFooter from "@/layout/website/StarterFooter";
export default {
  name: "Auth",
  data: () => ({
    credentials: {},
    valid: true,
    loading: false,
    fail_login: false,
    inputs: {
      user_border_b: "none",
      password_border_b: "none"
    }
  }),
  components: {
    "m-header": StarterHeader,
    StarterFooter
  },
  computed: {},
  methods: {
    Login() {
      // checking if the input is valid
      this.loading = true;
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
              console.log(res);
              this.$store.commit("storePermissions", res.data);
              if(this.$route.params.from == "pay"){
                this.$router.push("/pay");
              }else if (this.credentials.username == "sebastian"){
                this.$router.push("/users");
              }else if (this.credentials.username == "operator"){
                this.$router.push("/upload-photo");
              }else{
                this.$router.push("/dashboard");
              }
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