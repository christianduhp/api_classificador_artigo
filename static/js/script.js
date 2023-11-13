function flipCard() {
  var login = document.querySelector(".card");
  login.style.transform =
    login.style.transform === "rotateY(180deg)"
      ? "rotateY(0deg)"
      : "rotateY(180deg)";
}

const button = document.querySelector(".flip-button");
button.addEventListener("click", () => {
  console.log("clicked");
  flipCard();
});
