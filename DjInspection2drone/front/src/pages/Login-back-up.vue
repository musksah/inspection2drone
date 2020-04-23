<template>
  <div>
    <m-header></m-header>
    <!-- <main class="login-form" style="margin-top:7rem !important; margin-bottom:2rem !important;">
      <div class="cotainer">
        <div class="row justify-content-center">
          <div class="col-md-6">
            <div class="card" style="background-color:#ECECEC;">
              <div
                class="card-header pb-3"
                style="font-weight:700;background-color: #455199;color:white;"
              >Iniciar Sesión</div>
              <div class="card-body">
                <form action method class="mt-3" @submit.prevent="onSubmit">
                  <div class="form-group row">
                    <label
                      for="email_address"
                      class="col-md-4 col-form-label text-md-right"
                      style="color:#66615B;"
                    >Correo Electrónico/Usuario</label>
                    <div class="col-md-6">
                      <input
                        type="text"
                        id="email_address"
                        class="form-control"
                        name="username"
                        required
                        autofocus
                        v-model="username"
                        @keyup="Cleanform"
                      />
                    </div>
                  </div>

                  <div class="form-group row" style="margin-bottom:0; !important">
                    <label
                      for="password"
                      class="col-md-4 col-form-label text-md-right"
                      style="color:#66615B;"
                    >Contraseña</label>
                    <div class="col-md-6">
                      <input
                        type="password"
                        id="password"
                        class="form-control"
                        name="password"
                        required
                        v-model="password"
                        @keyup="Cleanform"
                      />
                    </div>
                  </div>
                  <div class="row" v-if="session_error">
                    <div class="col-md-4"></div>
                    <div class="col-md-6 mb-3">
                      <span style="color:#C62020;font-weight:700;">Usuario o contraseña incorrecta</span>
                    </div>
                  </div>
                  <div class="col-md-6 offset-md-4 mb-2">
                    <button type="submit" class="btn btn-danger">Ingresar</button>
                  </div>
                  <div class="col-md-6 offset-md-4">
                    <router-link to="/register">¿Olvidó su contraseña?</router-link>
                  </div>
                  <div class="col-md-6 offset-md-4 mb-2">
                    <router-link to="/register">Registrarse</router-link>
                  </div>
                </form>
              </div>
            </div>
          </div>
        </div>
      </div>
    </main>-->
    <v-container grid-list-md>
      <v-layout row wrap align-center justify-center fill-height>
        <v-flex xs12 sm8 lg4 md5>
          <v-card class="login-card">
            <v-card-title>
              <span class="headline">Login to Movies</span>
            </v-card-title>

            <v-spacer />

            <v-card-text>
              <v-layout row fill-height justify-center align-center v-if="loading">
                <v-progress-circular :size="50" color="primary" indeterminate />
              </v-layout>

              <v-form v-else ref="form" v-model="valid" lazy-validation>
                <v-container>
                  <v-text-field
                    v-model="credentials.username"
                    :counter="70"
                    label="username"
                    :rules="rules.username"
                    maxlength="70"
                    required
                  />

                  <v-text-field
                    type="password"
                    v-model="credentials.password"
                    :counter="20"
                    label="password"
                    :rules="rules.password"
                    maxlength="20"
                    required
                  />
                </v-container>
                <v-btn class="pink white--text" :disabled="!valid" @click="login">Login</v-btn>
              </v-form>
            </v-card-text>
          </v-card>
        </v-flex>
      </v-layout>
    </v-container>
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
  data() {
    return {
      username: "",
      password: "",
      session_error: false,
      credentials: {},
      valid: true,
      loading: false
    };
  },
  components: {
    "m-header": StarterHeader,
    StarterFooter
  },
  methods: {
    onSubmit(evt) {
      const path = `http://127.0.0.1:8000/api/v1.0/`;
      axios
        .post(path, { username: this.username, password: this.password })
        .then(response => {
          console.log(response);
          console.log(this.$router);
          if (response.data.session) {
            // swal("Te has logeado correctamente!", "", "success");
            // location.href("/dashboard")
            // router.go("/dashboard")
            console.log("entra");

            this.$router.push({ name: "dashboard" });
          } else {
            this.session_error = true;
          }
        })
        .catch(err => {
          swal(
            "Problemas de comunicación con el api, estamos trabajando para arreglarlo!",
            "",
            "error"
          );
        });
    },
    Cleanform() {
      if (this.session_error) {
        this.session_error = false;
      }
    },
    login() {}
  }
};
</script>
<style>
.my-form {
  padding-top: 1.5rem;
  padding-bottom: 1.5rem;
}

.my-form .row {
  margin-left: 0;
  margin-right: 0;
}

.login-form {
  padding-top: 1.5rem;
  padding-bottom: 1.5rem;
}

.login-form .row {
  margin-left: 0;
  margin-right: 0;
}

.btn:hover {
  color: #212529;
  text-decoration: none;
}

.btn-danger {
  color: #fff;
  background-color: #dc3545;
  border-color: #dc3545;
}
</style>