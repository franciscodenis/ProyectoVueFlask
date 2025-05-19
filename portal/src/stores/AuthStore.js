import { apiService } from "@/services/api";
import { defineStore } from "pinia";
import { useCookies } from "vue3-cookies";

export const useAuthStore = defineStore("AuthStore", {
    state: () => {
        return {
            isLoggedIn: false,
            user: null
        }
    },
    persist: true,
    actions: {
        async login(user) {
            await apiService.post("api/authentication/", user)
                .then(async () => {
                    await this.fetchUser();
                });
        },
        async fetchUser() {
            await apiService.get("api/me/profile/")
                .then(({data}) => {
                    this.user = data;
                    this.isLoggedIn = true;
                });
        },
        async logout() {
            await apiService.get("api/authentication/logout")
                .catch(() => {
                    const { cookies } = useCookies();
                    cookies.remove("csrf_access_token");
                });
            this.user = null;
            this.isLoggedIn = false;
        }
    }
});