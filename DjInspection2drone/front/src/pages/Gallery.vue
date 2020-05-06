<template>
  <div class="row">
    <div class="col-md-12">
      <card>
        <template slot="header">
          <h4 class="card-title">Galería de Imágenes</h4>
          <p class="card-category">Fotografías tomadas por DroneIanalyzer</p>
        </template>
        <div class="content">
          <gallery :images="images" :index="index" @close="index = null"></gallery>
          <div
            class="image"
            v-for="(image, imageIndex) in images"
            :key="imageIndex"
            @click="index = imageIndex"
            :style="{ 'background-image': 'url(' + image + ')', width: '300px', height: '200px' }"
            
          ></div>
        </div>
      </card>
    </div>
  </div>
</template>
<script>
import axios from "axios";
import VueGallery from "vue-gallery";
export default {
  data() {
    return {
      images: [
        // require("@/assets/img/slide1.jpg"),
        "https://dummyimage.com/1600/ffffff/000000",
        "https://dummyimage.com/1600/ffffff/000000",
        "https://dummyimage.com/1280/000000/ffffff",
        "https://dummyimage.com/400/000000/ffffff"
      ],
      index: null,
      files: []
    };
  },
  mounted() {
    this.getPhotos();
  },
  components: {
    gallery: VueGallery
  },
  methods: {
    getPhotos() {
      const axiosInstance = axios.create(this.$store.getters.getBaseInstanceAxios);
      axiosInstance({
        url: "/image/list-photos/",
        method: "get",
        params: {}
      })
        .then(res => {
          this.images = []
          Object.values(res.data).forEach(element => {
            this.images.push(require("@/assets/img/inspections/"+element+""))
          });
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
<style scoped>
.image {
  float: left;
  background-size: cover;
  background-repeat: no-repeat;
  background-position: center center;
  border: 1px solid #ebebeb;
  margin: 5px;
}
</style>
