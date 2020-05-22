<template>
  <header class="header-global">
    <base-nav class="navbar-main" type expand style="background-color: #353E76;">
      <router-link slot="brand" class="navbar-brand mr-lg-5" to="/">
        <img src="@/assets/img/logo_mini.png" />
      </router-link>
      <!-- <div class="row" slot="content-header" slot-scope="{closeMenu}">
        <div class="col-6 collapse-brand">
          <router-link
            to="/"
            style="color:white;font-weight:700;"
          >{{ 'Inspection2Drone'.toUpperCase() }}</router-link>
        </div>
        <div class="col-6 collapse-close">
          <close-button @click="closeMenu"></close-button>
        </div>
      </div>-->

      <ul class="navbar-nav navbar-nav-hover align-items-lg-center">
        <li class="nav-item">
          <a class="nav-link" to="/prices" style="color:white" href="#">Planes y precios</a>
        </li>
        <li class="nav-item">
          <a class="nav-link active" style="color:white" href="#">Quienes somos</a>
        </li>
        <li class="nav-item">
          <!-- <a  style="color:white" href="#">Contacto</a> -->
          <b-button
            v-b-modal.modal-contact
            class="nav-link "
            style="color:white !important;"
            variant="outline-primary"
          >Contáctanos</b-button>
        </li>
        <b-modal id="modal-contact" title="Formulario de Contácto">
          <b-form @submit="onSubmit" @reset="onReset" v-if="show">
            <b-form-group
              id="input-group-1"
              label="Email address:"
              label-for="input-1"
              description="We'll never share your email with anyone else."
            >
              <b-form-input
                id="input-1"
                v-model="form.email"
                type="email"
                required
                placeholder="Enter email"
              ></b-form-input>
            </b-form-group>

            <!-- <b-form-group id="input-group-2" label="Your Name:" label-for="input-2">
              <b-form-input id="input-2" v-model="form.name" required placeholder="Enter name"></b-form-input>
            </b-form-group>

            <b-form-group id="input-group-3" label="Food:" label-for="input-3">
              <b-form-select id="input-3" v-model="form.food" required></b-form-select>
            </b-form-group>-->

            <b-button type="submit" variant="primary">Submit</b-button>
            <b-button type="reset" variant="danger">Reset</b-button>
          </b-form>
        </b-modal>
      </ul>
      <ul class="navbar-nav align-items-lg-center ml-lg-auto">
        <li class="nav-item">
          <a
            class="nav-link nav-link-icon"
            href="#"
            target="_blank"
            data-toggle="tooltip"
            title="Like us on Facebook"
          >
            <i class="fa fa-facebook-square" style="color:white;"></i>
            <span class="nav-link-inner--text d-lg-none">Facebook</span>
          </a>
        </li>
        <li class="nav-item">
          <a
            class="nav-link nav-link-icon"
            href="#"
            target="_blank"
            data-toggle="tooltip"
            title="Follow us on Instagram"
          >
            <i class="fa fa-instagram" style="color:white;"></i>
            <span class="nav-link-inner--text d-lg-none">Instagram</span>
          </a>
        </li>
        <li class="nav-item">
          <a
            class="nav-link nav-link-icon"
            href="#"
            target="_blank"
            data-toggle="tooltip"
            title="Follow us on Twitter"
          >
            <i class="fa fa-twitter-square" style="color:white;"></i>
            <span class="nav-link-inner--text d-lg-none">Twitter</span>
          </a>
        </li>
        <li class="nav-item d-none d-lg-block ml-lg-4">
          <router-link class="btn btn-neutral btn-icon" :to="{name:'register'}">
            <span class="btn-inner--icon" style="color:#66615B;">
              <i class="fa fa-credit-card-alt mr-2" aria-hidden="true"></i>
            </span>
            <span class="nav-link-inner--text gray" style="color:#66615B;">Comprar</span>
          </router-link>
          <router-link class="btn btn-neutral btn-icon" :to="{name:'login', params:{'from':'login'}}" v-if="!logged">
            <span class="btn-inner--icon" style="color:#66615B;">
              <i class="fa fa-sign-in mr-2" aria-hidden="true"></i>
            </span>
            <span class="nav-link-inner--text gray" style="color:#66615B;">Ingresar</span>
          </router-link>
          <router-link class="btn btn-neutral btn-icon" :to="{name:'dashboard'}" v-if="logged">
            <span class="btn-inner--icon" style="color:#66615B;">
              <i class="fa fa-sign-in mr-2" aria-hidden="true"></i>
              <!-- <i class="fa fa-file-signature"></i> -->
            </span>
            <span class="nav-link-inner--text gray" style="color:#66615B;">Ir a Dashboard</span>
          </router-link>
        </li>
      </ul>
    </base-nav>
  </header>
</template>
<script>
import BaseNav from "@/components/website/BaseNav";
import CloseButton from "@/components/website/CloseButton";

export default {
  data() {
    return {
      logged: false,
      form: {
        name: "",
        email: ""
      },
      show: true,
    };
  },
  mounted() {
    this.checkLoggedIn();
  },
  components: {
    BaseNav,
    CloseButton
  },
  methods: {
    checkLoggedIn() {
      if (this.$store.state.jwt != null) {
        this.logged = true;
      }
    },
    onSubmit(evt) {
      evt.preventDefault();
      alert(JSON.stringify(this.form));
    },
    onReset(evt) {
      evt.preventDefault();
      // Reset our form values
      this.form.email = "";
      this.form.name = "";
      // Trick to reset/clear native browser form validation state
      this.show = false;
      this.$nextTick(() => {
        this.show = true;
      });
    }
  }
};
</script>
<style>
</style>