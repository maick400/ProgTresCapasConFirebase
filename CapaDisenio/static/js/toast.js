//import { Toast } from 'bootstrap'

var toastElList = [].slice.call(
    document.querySelectorAll('#toaste_message'))

for(let i = 0; i < toastElList.length; i++){
    toast = new bootstrap.Toast(toastElList[i])
    toast.show();
}
// var toastList = toastElList.map(function (toastEl) {
//     return new bootstrap.Toast(toastEl)
// })
// toastList.forEach(toast => toast.show())

