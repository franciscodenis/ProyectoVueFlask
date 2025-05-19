import axios from 'axios';
// import https from 'https';

const apiService = axios.create({
    baseURL: import.meta.env.VITE_ADMIN_APP_BASE_URL,
    withCredentials: true,
    xsrfCookieName: 'csrf_access_token',
    headers: {
        "Content-type": "application/json",
    },
});

export { apiService };