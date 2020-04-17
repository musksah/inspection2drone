<template>
  <header class="header-global">
    <base-nav class="navbar-main" fixed="top" type expand style="background-color: #233142;"> 
      <router-link slot="brand" class="navbar-brand mr-lg-5" to="/">
        <img src="@/assets/img/logo_mini.png" />
      </router-link>
      <div class="row" slot="content-header" slot-scope="{closeMenu}">
        <div class="col-6 collapse-brand">
          <a href="../index.html" style="color:white;font-weight:700;">
            {{ 'Inspection2Drone'.toUpperCase() }}
          </a>
        </div>
        <div class="col-6 collapse-close">
          <close-button @click="closeMenu"></close-button>
        </div>
      </div>

      <ul class="navbar-nav navbar-nav-hover align-items-lg-center">
        <li class="nav-item">
          <a class="nav-link active" style="color:white" href="#">Servicios</a>
        </li>
        <li class="nav-item">
          <a class="nav-link active" style="color:white" href="#">Quienes somos</a>
        </li>
        <li class="nav-item">
          <a class="nav-link active" style="color:white" href="#">Contacto</a>
        </li>
      </ul>
      <ul class="navbar-nav align-items-lg-center ml-lg-auto">
        <li class="nav-item">
          <a
            class="nav-link nav-link-icon"
            href="https://www.facebook.com/creativetim"
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
            href="https://www.instagram.com/creativetimofficial"
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
            href="https://twitter.com/creativetim"
            target="_blank"
            data-toggle="tooltip"
            title="Follow us on Twitter"
          >
            <i class="fa fa-twitter-square" style="color:white;"></i>
            <span class="nav-link-inner--text d-lg-none">Twitter</span>
          </a>
        </li>
        <li class="nav-item">
          <a
            class="nav-link nav-link-icon"
            href="https://github.com/creativetimofficial/vue-argon-design-system"
            target="_blank"
            data-toggle="tooltip"
            title="Star us on Github"
          >
            <i class="fa fa-github" style="color:white;"></i>
            <span class="nav-link-inner--text d-lg-none">Github</span>
          </a>
        </li>
        <li class="nav-item d-none d-lg-block ml-lg-4">
          <a
            href="https://www.creative-tim.com/product/vue-argon-design-system"
            target="_blank"
            class="btn btn-neutral btn-icon"
          >
            <span class="btn-inner--icon">
              <i class="fa fa-sign-in mr-2" aria-hidden="true"></i>
            </span>
            <span class="nav-link-inner--text">Ingresar</span>
          </a>
        </li>
      </ul>
    </base-nav>
  </header>
</template>
<script>
import BaseNav from "@/components/website/BaseNav";
import CloseButton from "@/components/website/CloseButton";

export default {
  components: {
    BaseNav,
    CloseButton
  }
};
</script>
<style>

</style>