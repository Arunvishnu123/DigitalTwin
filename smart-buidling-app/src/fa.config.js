import Vue from 'vue';
import { library } from '@fortawesome/fontawesome-svg-core'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

import { faUser, faBars,faBuilding } from '@fortawesome/free-solid-svg-icons'
import { faUserCircle, faCheckCircle } from '@fortawesome/free-regular-svg-icons'

library.add(
  faUser,
  faBuilding,
  faUserCircle,
  faCheckCircle,
  faBars
);

Vue.component('font-awesome-icon', FontAwesomeIcon); // registered globallys