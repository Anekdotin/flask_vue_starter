
const state = {
    user: null
}

export const Auth = {
    state,
    getters: {
        user: (state) => {
            return state.user;
        }
    },
    actions: {
        user (context, user) {
            context.commit('user', user);
        }
    },
    mutations: {
        user (state, user) {
            state.user = user;
        }
    },
  
   
}

export default Auth;