function getBathValue() {
  var uiBathrooms = document.getElementsByName("uiBathrooms");
  for(var i in uiBathrooms) {
    if(uiBathrooms[i].checked) {
        return parseInt(i)+1;
    }
  }
  return -1; // Invalid Value
}

function getBHKValue() {
  var uiBHK = document.getElementsByName("uiBHK");
  for(var i in uiBHK) {
    if(uiBHK[i].checked) {
        return parseInt(i)+1;
    }
  }
  return -1; // Invalid Value
}

function onClickedEstimatePrice() {
  console.log("Estimate price button clicked");
  var m2 = document.getElementById("uiSqft");
  var bhk = getBHKValue();
  var bathrooms = getBathValue();
  var location = document.getElementById("uiLocations");
  var butor = document.getElementById("uiButorok");
  var emelet = document.getElementById("uiEmeletek");
  var lift = document.getElementById("uiLift");
  var estPrice = document.getElementById("uiEstimatedPrice");
  //console.log(m2+", "+bhk+", "+bathrooms+", "+location+", "+butor+", "+emelet+", "+lift+", "+estPrice);
  var url = "http://127.0.0.1:5000/predict_home_price";

  $.post(url, {
      m2: parseFloat(m2.value),
      location: location.value,
      room_f: parseInt(bhk),
      room_hf: parseInt(bathrooms),
      butor: butor.value,
      emelet: emelet.value,
      lift: lift.value
  },function(data, status) {
      console.log(data.estimated_price);
      estPrice.innerHTML = "<h2>" + data.estimated_price.toString() + " Ft</h2>";
      console.log(status);
  });
}

function onPageLoad() {
  console.log("document loaded");
  var url = "http://127.0.0.1:5000/get_location_names"; 
  $.get(url,function(data, status) {
      console.log("got response for get_location_names request");
      if(data) {
          var locations = data.locations;
          var uiLocations = document.getElementById("uiLocations");
          $('#uiLocations').empty();
          for(var i in locations) {
              var opt = new Option(locations[i]);
              $('#uiLocations').append(opt);
          }
      }
  });

  var url = "http://127.0.0.1:5000/get_butor_names"; 
  $.get(url,function(data, status) {
      console.log("got response for get_butor_names request");
      if(data) {
          var butorok = data.butorozott;
          var uiButorok = document.getElementById("uiButorok");
          $('#uiButorok').empty();
          for(var i in butorok) {
              var opt = new Option(butorok[i]);
              $('#uiButorok').append(opt);
          }
      }
  });

  var url = "http://127.0.0.1:5000/get_emelet_names"; 
  $.get(url,function(data, status) {
      console.log("got response for get_emelet_names request");
      if(data) {
          var emeletek = data.emeletek;
          var uiEmeletek = document.getElementById("uiEmeletek");
          $('#uiEmeletek').empty();
          for(var i in emeletek) {
              var opt = new Option(emeletek[i]);
              $('#uiEmeletek').append(opt);
          }
      }
  });

  var url = "http://127.0.0.1:5000/get_lift_names"; 
  $.get(url,function(data, status) {
      console.log("got response for get_lift_names request");
      if(data) {
          var liftek = data.lift;
          var uiLiftek = document.getElementById("uiLift");
          $('#uiLift').empty();
          for(var i in liftek) {
              var opt = new Option(liftek[i]);
              $('#uiLift').append(opt);
          }
      }
  });
}
window.onload = onPageLoad;