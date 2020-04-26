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
                  <v-layout row fill-height justify-center align-center v-if="loading" style="display:flex;justify-content:center;">
                    <v-progress-circular :size="50" color="primary" indeterminate />
                  </v-layout>
                  <form action method class="mt-3" @submit.prevent="Login">
                    <div class="form-group row" style="display:flex;justify-content:center;">
                      <div class="col-md-7">
                        <v-text-field
                          v-model="credentials.username"
                          :counter="70"
                          label="usuario"
                          maxlength="70"
                          required
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
                  </form>
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
    loading: false
  }),
  components: {
    "m-header": StarterHeader,
    StarterFooter
  },
  methods: {
    Login() {
      // checking if the input is valid
      this.loading = true;
      axios
        .post(
          "http://127.0.0.1:8000/api/v1.0/auth/obtain_token/",
          this.credentials
        )
        .then(res => {
          console.log(res);
          this.$session.start();
          this.$session.set("token", res.data.token);
          this.$router.push("/dashboard");
        })
        .catch(e => {
          this.loading = false;
          swal({
            type: "error",
            icon: "error",
            title: "Error",
            text: "Wrong username or password",
            timer: 3000
          });
        });
    }
  }
};
</script>