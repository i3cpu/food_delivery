new Vue({
    el: '#app',
    data: {
      message: "Hello, World!",
      index: 0,
      images: [
        { url: '/media/images/4.jpg' },
        { url: '/media/images/7.jpg' },
        { url: '/media/images/5.jpg' }
      ]
    },
    mounted() {
      setInterval(() => {
        this.next();
      }, 3000);
    },
    methods: {
      previous() {
        if (this.index > 0) {
          this.index--;
        } else {
          this.index = this.images.length - 1;
        }
      },
      next() {
        if (this.index < this.images.length - 1) {
          this.index++;
        } else {
          this.index = 0;
        }
      }
    }
  });