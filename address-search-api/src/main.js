import './style.css'

const btn = document.querySelector("#btn");
const number = document.querySelector("#number");
const zipcodeCell = document.querySelector(".zipcode");
const address1Cell = document.querySelector(".address1");
const address2Cell = document.querySelector(".address2");
const address3Cell = document.querySelector(".address3");

number.addEventListener("input", (e) => {
  if (e.target.value.length > 7) {
    e.target.value = e.target.value.slice(0, 7);
  }
});

const status_preview = () => {
  const zipcode = number.value;
  const url = `https://zipcloud.ibsnet.co.jp/api/search?zipcode=${zipcode}`

  fetch(url)
    .then(res => res.json())
    .then(data => {
      const results = data.results[0]
      zipcodeCell.textContent = zipcode;
      address1Cell.textContent = results.address1;
      address2Cell.textContent = results.address2;
      address3Cell.textContent = results.address3;
    });
};

btn.addEventListener("click", status_preview)