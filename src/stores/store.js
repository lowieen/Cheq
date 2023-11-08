import { createStore } from 'vuex';

const store = createStore({
  state() {
    return {
      isAuthenticated: false,
      userEmail: null,
      carrito: [],
      isAdmin: false
    };
  },
  mutations: {
    setUserEmail(state, email) {
      state.userEmail = email;
    },
    setAuthStatus(state, status) {
      state.isAuthenticated = status;
    },
    agregarAlCarrito(state, producto){
      state.carrito.push(producto);
    },
    setAdminStatus(state, isAdmin) {
      state.isAdmin = isAdmin;
    },
  },
  actions: {
    updateUserEmail({ commit }, email) {
      commit('setUserEmail', email);
    },
    updateAuthStatus({ commit }, status) {
      commit('setAuthStatus', status);
    },
    userLoggedOut({ commit }) {
      commit('setAdminStatus', false); // Limpia el estado de administrador al cerrar sesión
      commit('setAuthStatus', false); // Actualiza el estado de autenticación
      commit('setUserEmail', null);   // Limpia el correo del usuario
    },
    updateAdminStatus({ commit }, isAdmin) {
      commit('setAdminStatus', isAdmin);
    },
  }
});

export default store;

