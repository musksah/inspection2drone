import Vue from 'vue';
import axios from 'axios'
import VueAxios from 'vue-axios'
import jwt_decode from 'jwt-decode'
import Vuex from 'vuex'
Vue.use(Vuex);
Vue.use(VueAxios, axios);

export const store = new Vuex.Store({
    state: {
        jwt: localStorage.getItem('t'),
        username: localStorage.getItem('username'),
        endpoints: {
            obtainJWT: 'http://127.0.0.1:8000/api/v1.0/auth/obtain_token/',
            refreshJWT: 'http://127.0.0.1:8000/api/v1.0/auth/refresh_token/'
        },
        permissions: localStorage.getItem('permissions'),
        modules: localStorage.getItem('modules'),
        plan_tranc_id: localStorage.getItem('plan_id'),
        info_modules: {
            'view_dashboard': {
                name: "Dashboard",
                route: "dashboard",
                icon: "ti-dashboard"
            },
            'view_user': {
                name: "Users",
                route: "users",
                icon: "ti-user"
            },
            'view_inspection': {
                name: "Inspecciones",
                route: "inspection",
                icon: "ti-calendar"
            },
            'view_company': {
                name: "Compañías",
                route: "company",
                icon: "ti-briefcase"
            },
            'view_plan': {
                name: "Planes",
                route: "plans",
                icon: "ti-notepad"
            },
            'view_image': {
                name: "Galería",
                route: "gallery",
                icon: "ti-gallery"
            },
            'add_image': {
                name: "Cargar Imágenes",
                route: "upload-photo",
                icon: "ti-gallery"
            },
            'view_pilot': {
                name: "Pilotos",
                route: "pilot",
                icon: "ti-id-badge"
            },
            'view_profile': {
                name: "profile",
                route: "profile",
                icon: "ti-id-badge"
            },
            'view_drone': {
                name: "Drones",
                route: "drones",
                icon: "ti-vector"
            },
            'view_analysis': {
                name: "Análisis",
                route: "analysis",
                icon: "ti-briefcase"
            },
        }
    },
    getters: {
        getBaseInstanceAxios: state => {
            return {
                baseURL: "http://127.0.0.1:8000/api/v1.0/",
                headers: {
                    Authorization: `JWT ${state.jwt}`,
                    "Content-Type": "application/json"
                },
                xhrFields: {
                    withCredentials: true
                }
            };
        },
        getModules: state => {
            let modules_new = []
            JSON.parse(state.modules).forEach(element => {
                console.log(element);
                if (state.info_modules.hasOwnProperty(element)) {
                    modules_new.push(state.info_modules[element]);
                }
            });
            return modules_new;
        }
    },
    mutations: {
        updatePlan(state, plan_id) {
            localStorage.setItem('plan_id', plan_id);
            state.plan_tranc_id = plan_id;
        },
        updateToken(state, newToken) {
            localStorage.setItem('t', newToken);
            state.jwt = newToken;
        },
        removeToken(state) {
            localStorage.removeItem('t');
            state.jwt = null;
        },
        updateUsername(state, username) {
            localStorage.setItem('username', username);
            state.username = username;
        },
        storePermissions(state, permissions) {
            state.permissions = []
            let arr_modules = []
            permissions.forEach(element => {
                state.permissions.push(element.fields.codename)
            });
            localStorage.setItem('permissions', JSON.stringify(state.permissions))
            arr_modules = state.permissions.filter(function (perm) {
                return perm.includes("view") || perm.includes("add");
            });
            state.modules = JSON.stringify(arr_modules);
            localStorage.setItem('modules', JSON.stringify(arr_modules));
        }
    },
    actions: {
        obtainToken(context, credentials) {
            const payload = {
                username: credentials.username,
                password: credentials.password
            }
            return axios.post(this.state.endpoints.obtainJWT, payload);
        },
        refreshToken() {
            const payload = {
                token: this.state.jwt
            }
            axios.post(this.state.endpoints.refreshJWT, payload)
                .then((response) => {
                    this.commit('updateToken', response.data.token)
                })
                .catch((error) => {
                    console.log(error)
                })
        },
        inspectToken() {
            // WE WILL ADD THIS LATER
            const token = this.state.jwt;
            if (token) {
                const decoded = jwt_decode(token);
                const exp = decoded.exp
                const orig_iat = decode.orig_iat
                if (exp - (Date.now() / 1000) < 1800 && (Date.now() / 1000) - orig_iat < 628200) {
                    this.dispatch('refreshToken')
                } else if (exp - (Date.now() / 1000) < 1800) {
                    // DO NOTHING, DO NOT REFRESH          
                } else {
                    // PROMPT USER TO RE-LOGIN, THIS ELSE CLAUSE COVERS THE CONDITION WHERE A TOKEN IS EXPIRED AS WELL
                }
            }
        }
    }
});