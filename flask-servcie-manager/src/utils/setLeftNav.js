import { bus } from '@/main.js';

export function setLeftNav(showNav, nav = null) {
    bus.$emit('setLeftNav', {
      showNav: showNav,
      nav: nav
    });
  }