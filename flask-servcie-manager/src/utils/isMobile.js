
export default {
    install(Vue) {
      Vue.prototype.$isMobile = window.innerWidth <= 800;
  
      const handleResize = () => {
        Vue.prototype.$isMobile = window.innerWidth <= 800;
      };
  
      window.addEventListener('resize', handleResize);
  
      // 也可以选择在组件销毁时移除事件监听器
      // Vue.mixin({
      //   beforeDestroy() {
      //     window.removeEventListener('resize', handleResize);
      //   }
      // });
    }
  };