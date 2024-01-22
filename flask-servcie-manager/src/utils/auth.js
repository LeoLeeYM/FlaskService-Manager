import Cookies from 'js-cookie'

const TokenKey = 'token'

export function getToken() {
  return Cookies.get(TokenKey)
}

export function setToken(_token) {
  return Cookies.set(TokenKey, _token)
}

export function removeToken() {
  return Cookies.remove(TokenKey)
}

export function getUserInfo(){
  return {
    name: localStorage.getItem('name'),
    department: localStorage.getItem('department'),
    position: localStorage.getItem('position'),
    profilePhotos: localStorage.getItem('profilePhotos'),
    studentid: localStorage.getItem('studentid'),
    power: localStorage.getItem('power')
  }
}