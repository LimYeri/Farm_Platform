/* 날씨정보 */
function getWeather() {
  let temperature = document.getElementById("temperature");
  let description = document.getElementById("description");
  let location = document.getElementById("location");
  let humidity = document.getElementById("humidity");
  let sunrise = document.getElementById("sunrise_time");
  let sunset = document.getElementById("sunset_time");


  let api = "https://api.openweathermap.org/data/2.5/weather";
  let apiKey = "290304a7823c3aa687e558e7dbad5dbe";

  location.innerHTML = "위치 정보 확인 중 ...";

  navigator.geolocation.getCurrentPosition(success, error);

  function success(position) {
    latitude = position.coords.latitude;
    longitude = position.coords.longitude;

    let url =
      api +
      "?lat=" +
      latitude +
      "&lon=" +
      longitude +
      "&appid=" +
      apiKey +
      "&units=imperial";

    fetch(url)
      .then(response => response.json())
      .then(data => {
        console.log(data);
        let temp = data.main.temp;
        temperature.innerHTML = Math.round((temp-32)*5/9) + "° C";
        location.innerHTML = data.name;
        description.innerHTML = data.weather[0].description;
        humidity.innerHTML = data.main.humidity + " %";
        sunrise.innerHTML = Unix_timestamp(data.sys.sunrise);
        sunset.innerHTML = Unix_timestamp(data.sys.sunset);
      });
  }

  function error() {
    location.innerHTML = "위치 정보를 확인할 수 없습니다.";
  }
}

getWeather();

// 타임스탬프 값을 년월일로 변환
function Unix_timestamp(t){
    var date = new Date(t*1000);
    var hour = "0" + date.getHours();
    var minute = "0" + date.getMinutes();
    return hour.substr(-2) + ":" + minute.substr(-2);
}
