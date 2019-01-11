const checkNewsButton = document.getElementById('checkNewsButton');
const resultBox = document.getElementById('resultBox');

const loading = document.createElement("div");
loading.classList.add("loader");

const result = document.createElement("p");  
let url;

chrome.tabs.query({'active': true, 'lastFocusedWindow': true}, function (tabs) { url = tabs[0].url; });

checkNewsButton.onclick = function(element) {
  url = url.replace("index.html", "");
  resultBox.appendChild(loading); 
  checkNewsButton.remove();
  axios.post("http://localhost:5000/", { url : url })
    .then( function (res) {
      const score = parseInt(res.data);
      loading.remove();
      let message = "";
      (score === -1)
      ? message = "N/A"
      : message = score

      const text = document.createTextNode(message);
      (score < 5) 
        ? result.classList.add("not-trust")
        : result.classList.add("trust");
      result.appendChild(text);    
      resultBox.appendChild(result);    
    })
    .catch( function (err) {
      loading.remove();
      result.appendChild(checkNewsButton); 
      console.log(err);      
    });
  };