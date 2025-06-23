import axios from 'axios';

const API_URL = 'http://localhost:8000/api/';

export const login = (data) => axios.post(`${API_URL}auth/login/`, data);
export const register = (data) => axios.post(`${API_URL}auth/register/`, data);
export const getProfile = (token) => axios.get(`${API_URL}profiles/me/`, {
  headers: { Authorization: `Bearer ${token}` }
});