const registerBut = document.querySelector(".loginRegister > span");
const loginBut = document.querySelector(".loginLogin > span");
let loginMain = document.querySelector(".loginMain");
let loginData = document.querySelector(".loginData");
let loginRegisterPage = document.querySelector(".loginRegisterPage");

registerBut.addEventListener("click", () => {
  loginData.style["display"] = "none";
  loginRegisterPage.style["display"] = "grid";
  loginMain.style["grid-template-areas"] = "loginRegisterPage loginBackground";
});

loginBut.addEventListener("click", () => {
  loginRegisterPage.style["display"] = "none";
  loginData.style["display"] = "grid";
  loginMain.style["grid-template-areas"] = "loginData loginBackground";
});
