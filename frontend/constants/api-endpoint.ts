export const API_ENDPOINTS = {
  BASE_URL: process.env.NEXT_PUBLIC_API_URL,
  LOGIN:"/auth/login",
  POKEMON: {
    BASE: '/pokemon',
    GET_LIST: '/pokemon/list',
    GET_BY_ID: (id: string) => `/pokemon/${id}`,
  },
};
