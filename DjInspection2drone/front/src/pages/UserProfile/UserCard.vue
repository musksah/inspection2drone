<template>
  <card class="card-user">
    <div slot="image">
      <img src="@/assets/img/background.jpg" alt="...">
    </div>
    <div>
      <div class="author">
        <img class="avatar border-white" src="@/assets/img/faces/face-4.jpg" alt="...">
        <h4 class="title">{{ pilot.name+" "+pilot.lastname }}
          <br>
          <a href="#">
            <small>@{{username}}</small>
          </a>
        </h4>
      </div>
    </div>
    <hr>
    <div class="text-center">
      <div class="row">
        <div v-for="(info, index) in details" :key="index" :class="getClasses(index)">
          <h5>{{info.title}}
            <br>
            <small>{{info.subTitle}}</small>
          </h5>
        </div>
      </div>
    </div>
  </card>
</template>
<script>
import axios from "axios";
export default {
  data() {
    return {
      details: [
        {
          title: "1",
          subTitle: "Inspección"
        },
        {
          title: "0",
          subTitle: "Fotos"
        },
        {
          title: "0",
          subTitle: "Análysis"
        }
      ],
      pilot: {
        company: "",
        email: "",
        lastName: "",
        address: "",
        city: "",
        postalCode: "",
      },
      allname:"",
      username:this.$store.state.username,
      company:"DroneIAnalyzer"
    }
  },
  created() {
    this.getDataProfile();
  },
  methods: {
    getClasses(index) {
      var remainder = index % 3;
      if (remainder === 0) {
        return "col-lg-3 offset-lg-1";
      } else if (remainder === 2) {
        return "col-lg-4";
      } else {
        return "col-lg-3";
      }
    },
    getDataProfile() {
      const axiosInstance = axios.create(this.$store.getters.getBaseInstanceAxios);
      axiosInstance({
        url: "/pilots/",
        method: "get",
        params: {}
      })
        .then(res => {
          console.log(res);
          this.pilot = res.data[0].fields
        })
        .catch(e => {});
    }
  }
};
</script>
<style>
</style>
