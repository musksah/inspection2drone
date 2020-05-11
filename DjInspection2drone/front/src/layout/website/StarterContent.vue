<template>
  <div>
    <section id="features" class="features section mt-5">
      <div class="container">
        <div class="row">
          <div class="col-md-4 col-sm-6 feature text-center">
            <span class="icon icon-camera"></span>
            <div class="feature-content">
              <h5>Captura de fotos 4k</h5>
              <p>Nuestros drones pueden tomar fotos de alta calidad y resolución en zonas de difícil acceso de cualquier obra de construcción.</p>
            </div>
          </div>
          <div class="col-md-4 col-sm-6 feature text-center">
            <span class="icon icon-pictures"></span>
            <div class="feature-content">
              <h5>Galería de fotografías</h5>
              <p>Gracias a nuestro incríble sistema de administración puedes acceder ver tus fotografías en una galería cómoda para ti.</p>
            </div>
          </div>
          <div class="col-md-4 col-sm-6 feature text-center">
            <span class="icon icon-profile-male"></span>
            <div class="feature-content">
              <h5>Pilotos Capacitados</h5>
              <p>Para realizar inspecciones de obra de calidad, contamos con pilotos de drones certificados y con una gran experiencia de vuelo.</p>
            </div>
          </div>
          <div class="col-md-4 col-sm-6 feature text-center">
            <span class="icon icon-genius"></span>
            <div class="feature-content">
              <h5>Inteligencia Artificial</h5>
              <p>Nuestros sistemas y drones usan la inteligencia artificial para ofrecerte un servicio con tecnología de punta.</p>
            </div>
          </div>
          <div class="col-md-4 col-sm-6 feature text-center">
            <span class="icon icon-presentation"></span>
            <div class="feature-content">
              <h5>Reportes amigables</h5>
              <p>Pensando en tu comodidad nuestros sistema de reportes es de fácil uso y comprensión. Para que puedas tomar las mejores desiciones en el desarrollo de tus obras de construcción.</p>
            </div>
          </div>
          <div class="col-md-4 col-sm-6 feature text-center">
            <span class="icon icon-desktop"></span>
            <div class="feature-content">
              <h5>Sistema Administrativo</h5>
              <p>Contamos con un sistema robusto, confiable, seguro y con las mejores prácticas para que te ayude a administrar tus inspecciones de obras de construcción.</p>
            </div>
          </div>
        </div>
      </div>
    </section>
    <section id="prices">
      <h2 style="text-align:center">Responsive Pricing Tables</h2>
      <p style="text-align:center">Resize the browser window to see the effect.</p>

      <div class="columns">
        <ul class="price">
          <li class="header">Basic</li>
          <li class="grey">$ 9.99 / year</li>
          <li>10GB Storage</li>
          <li>10 Emails</li>
          <li>10 Domains</li>
          <li>1GB Bandwidth</li>
          <li class="grey">
            <a href="#" class="button">Sign Up</a>
          </li>
        </ul>
      </div>

      <div class="columns">
        <ul class="price">
          <li class="header" style="background-color:#4CAF50">Pro</li>
          <li class="grey">$ 24.99 / year</li>
          <li>25GB Storage</li>
          <li>25 Emails</li>
          <li>25 Domains</li>
          <li>2GB Bandwidth</li>
          <li class="grey">
            <a href="#" class="button">Sign Up</a>
          </li>
        </ul>
      </div>

      <div class="columns">
        <ul class="price">
          <li class="header">Premium</li>
          <li class="grey">$ 49.99 / year</li>
          <li>50GB Storage</li>
          <li>50 Emails</li>
          <li>50 Domains</li>
          <li>5GB Bandwidth</li>
          <li class="grey">
            <a href="#" class="button">Sign Up</a>
          </li>
        </ul>
      </div>
    </section>
    <!-- teams -->
  </div>
</template>
<script>
export default {
  name: "starter-content"
};
</script>
<style>
.feature {
  margin-bottom: 50px;
}
.feature-content {
  padding: 0 15px;
  margin-top: 30px;
}
.feature .icon {
  color: #e84545;
  font-size: 60px;
}

@font-face {
  font-family: "elegant-theme-line";
  src: url("../../assets/fonts/elegant-theme-line.ttf?1439850014")
      format("truetype"),
    url("../../assets/fonts/elegant-theme-line.eot?1439850014")
      format("embedded-opentype"),
    url("../../assets/fonts/elegant-theme-line.svg?1439850014") format("svg"),
    url("../../assets/fonts/elegant-theme-line.woff?1439850014") format("woff");
}
.icon {
  font-family: "elegant-theme-line";
  speak: none;
  font-style: normal;
  font-weight: normal;
  font-variant: normal;
  text-transform: none;
  line-height: 1;
  /* Better Font Rendering =========== */
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

.icon-mobile:before {
  content: "\e000";
}

.icon-laptop:before {
  content: "\e001";
}

.icon-desktop:before {
  content: "\e002";
}

.icon-tablet:before {
  content: "\e003";
}

.icon-phone:before {
  content: "\e004";
}

.icon-document:before {
  content: "\e005";
}

.icon-documents:before {
  content: "\e006";
}

.icon-search:before {
  content: "\e007";
}

.icon-clipboard:before {
  content: "\e008";
}

.icon-newspaper:before {
  content: "\e009";
}

.icon-notebook:before {
  content: "\e00a";
}

.icon-book-open:before {
  content: "\e00b";
}

.icon-browser:before {
  content: "\e00c";
}

.icon-calendar:before {
  content: "\e00d";
}

.icon-presentation:before {
  content: "\e00e";
}

.icon-picture:before {
  content: "\e00f";
}

.icon-pictures:before {
  content: "\e010";
}

.icon-video:before {
  content: "\e011";
}

.icon-camera:before {
  content: "\e012";
}

.icon-printer:before {
  content: "\e013";
}

.icon-toolbox:before {
  content: "\e014";
}

.icon-briefcase:before {
  content: "\e015";
}

.icon-wallet:before {
  content: "\e016";
}

.icon-gift:before {
  content: "\e017";
}

.icon-bargraph:before {
  content: "\e018";
}

.icon-grid:before {
  content: "\e019";
}

.icon-expand:before {
  content: "\e01a";
}

.icon-focus:before {
  content: "\e01b";
}

.icon-edit:before {
  content: "\e01c";
}

.icon-adjustments:before {
  content: "\e01d";
}

.icon-ribbon:before {
  content: "\e01e";
}

.icon-hourglass:before {
  content: "\e01f";
}

.icon-lock:before {
  content: "\e020";
}

.icon-megaphone:before {
  content: "\e021";
}

.icon-shield:before {
  content: "\e022";
}

.icon-trophy:before {
  content: "\e023";
}

.icon-flag:before {
  content: "\e024";
}

.icon-map:before {
  content: "\e025";
}

.icon-puzzle:before {
  content: "\e026";
}

.icon-basket:before {
  content: "\e027";
}

.icon-envelope:before {
  content: "\e028";
}

.icon-streetsign:before {
  content: "\e029";
}

.icon-telescope:before {
  content: "\e02a";
}

.icon-gears:before {
  content: "\e02b";
}

.icon-key:before {
  content: "\e02c";
}

.icon-paperclip:before {
  content: "\e02d";
}

.icon-attachment:before {
  content: "\e02e";
}

.icon-pricetags:before {
  content: "\e02f";
}

.icon-lightbulb:before {
  content: "\e030";
}

.icon-layers:before {
  content: "\e031";
}

.icon-pencil:before {
  content: "\e032";
}

.icon-tools:before {
  content: "\e033";
}

.icon-tools-2:before {
  content: "\e034";
}

.icon-scissors:before {
  content: "\e035";
}

.icon-paintbrush:before {
  content: "\e036";
}

.icon-magnifying-glass:before {
  content: "\e037";
}

.icon-circle-compass:before {
  content: "\e038";
}

.icon-linegraph:before {
  content: "\e039";
}

.icon-mic:before {
  content: "\e03a";
}

.icon-strategy:before {
  content: "\e03b";
}

.icon-beaker:before {
  content: "\e03c";
}

.icon-caution:before {
  content: "\e03d";
}

.icon-recycle:before {
  content: "\e03e";
}

.icon-anchor:before {
  content: "\e03f";
}

.icon-profile-male:before {
  content: "\e040";
}

.icon-profile-female:before {
  content: "\e041";
}

.icon-bike:before {
  content: "\e042";
}

.icon-wine:before {
  content: "\e043";
}

.icon-hotairballoon:before {
  content: "\e044";
}

.icon-globe:before {
  content: "\e045";
}

.icon-genius:before {
  content: "\e046";
}

.icon-map-pin:before {
  content: "\e047";
}

.icon-dial:before {
  content: "\e048";
}

.icon-chat:before {
  content: "\e049";
}

.icon-heart:before {
  content: "\e04a";
}

.icon-cloud:before {
  content: "\e04b";
}

.icon-upload:before {
  content: "\e04c";
}

.icon-download:before {
  content: "\e04d";
}

.icon-target:before {
  content: "\e04e";
}

.icon-hazardous:before {
  content: "\e04f";
}

.icon-piechart:before {
  content: "\e050";
}

.icon-speedometer:before {
  content: "\e051";
}

.icon-global:before {
  content: "\e052";
}

.icon-compass:before {
  content: "\e053";
}

.icon-lifesaver:before {
  content: "\e054";
}

.icon-clock:before {
  content: "\e055";
}

.icon-aperture:before {
  content: "\e056";
}

.icon-quote:before {
  content: "\e057";
}

.icon-scope:before {
  content: "\e058";
}

.icon-alarmclock:before {
  content: "\e059";
}

.icon-refresh:before {
  content: "\e05a";
}

.icon-happy:before {
  content: "\e05b";
}

.icon-sad:before {
  content: "\e05c";
}

.icon-facebook:before {
  content: "\e05d";
}

.icon-twitter:before {
  content: "\e05e";
}

.icon-googleplus:before {
  content: "\e05f";
}

.icon-rss:before {
  content: "\e060";
}

.icon-tumblr:before {
  content: "\e061";
}

.icon-linkedin:before {
  content: "\e062";
}

.icon-dribbble:before {
  content: "\e063";
}

* {
  box-sizing: border-box;
}

/* Create three columns of equal width */
.columns {
  float: left;
  width: 33.3%;
  padding: 8px;
}

/* Style the list */
.price {
  list-style-type: none;
  border: 1px solid #eee;
  margin: 0;
  padding: 0;
  -webkit-transition: 0.3s;
  transition: 0.3s;
}

/* Add shadows on hover */
.price:hover {
  box-shadow: 0 8px 12px 0 rgba(0, 0, 0, 0.2);
}

/* Pricing header */
.price .header {
  background-color: #111;
  color: white;
  font-size: 25px;
}

/* List items */
.price li {
  border-bottom: 1px solid #eee;
  padding: 20px;
  text-align: center;
}

/* Grey list item */
.price .grey {
  background-color: #eee;
  font-size: 20px;
}

/* The "Sign Up" button */
.button {
  background-color: #4caf50;
  border: none;
  color: white;
  padding: 10px 25px;
  text-align: center;
  text-decoration: none;
  font-size: 18px;
}

/* Change the width of the three columns to 100%
(to stack horizontally on small screens) */
@media only screen and (max-width: 600px) {
  .columns {
    width: 100%;
  }
}
</style>