<template>
  <div class="dr-bg-info">
    <b-container class="dr-bg-info">
      <nav class="navbar dr-bg-info navbar-expand-lg navbar-dark fixed-top">
        <b-navbar-brand href="#" :style="{'margin-left':'7em'}">
          <img src="@/assets/logo_mini.png" alt />
        </b-navbar-brand>

        <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

        <b-collapse id="nav-collapse" is-nav>
          <b-navbar-nav>
            <b-nav-item href="#">Servicios</b-nav-item>
            <b-nav-item href="#">Quiénes Somos</b-nav-item>
            <b-nav-item href="#">Contacto</b-nav-item>
            <b-nav-item href="#">Ingresar</b-nav-item>
          </b-navbar-nav>
          <!-- Right aligned nav items -->
          <b-navbar-nav class="ml-auto">
            <b-nav-item-dropdown right :style="{'margin-right':'7em'}">
              <!-- Using 'button-content' slot -->
              <template v-slot:button-content>
                <em>User</em>
              </template>
              <b-dropdown-item href="#">Profile</b-dropdown-item>
              <b-dropdown-item href="#">Sign Out</b-dropdown-item>
            </b-nav-item-dropdown>
          </b-navbar-nav>
        </b-collapse>
      </nav>
    </b-container>
    <b-container class="dr-banner dr-main" v-bind:style="{ 'background-image':image}" fluid>
      <b-row>
        <b-col>
          <h1
            class="text-white"
            v-bind:style="{'font-weight':700,'text-transform':'uppercase','font-family':'sans-serif','font-size':'65px'}"
          >Inspecciones de Obra</h1>
        </b-col>
      </b-row>
    </b-container>
    <b-container>
      
    </b-container>
  </div>
</template>

<script>
export default {
  data() {
    return {
      image: `url(${require("@/assets/bgdroneo.jpg")})`,
      logo: `url(${require("@/assets/logo_mini.png")})`
    };
  }
};
</script>

<style scoped>
.dr-bg-info {
  background-color: #33375c;
}

.dr-banner {
  background-position: center top;
  background-repeat: no-repeat;
  -moz-background-size: cover;
  -o-background-size: cover;
  -webkit-background-size: cover;
  background-size: cover;
  min-height: 750px;
}

.dr-main {
  display: flex;
  align-items: center;
  justify-content: center;
}
</style>
<!-- Add "scoped" attribute to limit CSS to this component only -->
