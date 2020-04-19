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
    <section id="services" style="background-color:#e3e3e3;">
      <div class="container pt-5 pb-5">
        <div class="card-deck">
          <div class="card">
            <img class="card-img-top" alt="Card image cap" />
            <div class="card-body">
              <h5 class="card-title">Card title</h5>
              <p
                class="card-text"
              >This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
            </div>
            <div class="card-footer">
              <small class="text-muted">Last updated 3 mins ago</small>
            </div>
          </div>
          <div class="card">
            <img class="card-img-top" alt="Card image cap" />
            <div class="card-body">
              <h5 class="card-title">Card title</h5>
              <p
                class="card-text"
              >This card has supporting text below as a natural lead-in to additional content.</p>
            </div>
            <div class="card-footer">
              <small class="text-muted">Last updated 3 mins ago</small>
            </div>
          </div>
          <div class="card">
            <img class="card-img-top" alt="Card image cap" />
            <div class="card-body">
              <h5 class="card-title">Card title</h5>
              <p
                class="card-text"
              >This is a wider card with supporting text below as a natural lead-in to additional content. This card has even longer content than the first to show that equal height action.</p>
            </div>
            <div class="card-footer">
              <small class="text-muted">Last updated 3 mins ago</small>
            </div>
          </div>
        </div>
      </div>
    </section>
    <!-- teams -->
  </div>
</template>
<script>
export default {
  name: "starter-content",
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
</style>