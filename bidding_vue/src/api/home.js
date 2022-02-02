import axios from '@/utils/http';

let token_s1 = sessionStorage.token || localStorage.token
export const fetchData = options => axios.request({
  ...options,
  url: '/users/login/',
  method:'post',

});

export const SelectData = options => axios.request({
  ...options,
  url: '/bidding/',
  method:'post',
  headers:{
    'Authorization':'jwt ' + sessionStorage.token || localStorage.token
  }

});

export const UpdateUser = options => axios.request({
  ...options,
  url: '/users/settings/',
  method:'post',
  headers:{
    'Authorization':'jwt ' + sessionStorage.token || localStorage.token
  }

});


export const GetUser = options => axios.request({
  ...options,
  url: '/users/settings/',
  method:'get',
  headers:{
    'Authorization':'jwt ' + sessionStorage.token || localStorage.token
  }

});


export default {};
