<template>
  <div>
    <m-header></m-header>
    <m-carousel></m-carousel>
    <starter-content></starter-content>
    <starter-footer></starter-footer>
  </div>
</template>

<script>
import StarterHeader from "@/layout/website/StarterHeader";
import StarterFooter from "@/layout/website/StarterFooter";
import StarterContent from "@/layout/website/StarterContent";
import Carousel from "@/components/website/Carousel";
export default {
  data() {
    return {
      slide: 0,
      sliding: null
    };
  },
  mounted() {
  },
  components: {
    "m-header": StarterHeader,
    "m-carousel": Carousel,
    StarterFooter,
    StarterContent
  },
  methods: {
    onSlideStart(slide) {
      this.sliding = true;
    },
    onSlideEnd(slide) {
      this.sliding = false;
    },
    LoggedOut() {
      this.$session.destroy();
    },
    checkLoggedIn() {
    }
  }
};
</script>