
// Themes begin
am4core.useTheme(am4themes_animated);
// Themes end

var chart = am4core.create("chartdiv", am4maps.MapChart);

// Set map definition
chart.geodata = am4geodata_worldLow;

// Set projection
chart.projection = new am4maps.projections.Orthographic();
chart.panBehavior = "rotateLongLat";
chart.deltaLatitude = -20;
chart.padding(25, 20, 30, 60);

// Create map polygon series
var polygonSeries = chart.series.push(new am4maps.MapPolygonSeries());

// Make map load polygon (like country names) data from GeoJSON
polygonSeries.useGeodata = true;
//polygonSeries.include = ["BR", "UA", "MX", "CI"];

// Configure series
var polygonTemplate = polygonSeries.mapPolygons.template;
polygonTemplate.tooltipText = "{name}";
polygonTemplate.fill = am4core.color("#007FFF");
polygonTemplate.stroke = am4core.color("white");
polygonTemplate.strokeWidth = 0.5;
polygonTemplate.cursorOverStyle = am4core.MouseCursorStyle.pointer;
// polygonTemplate.url = "https://www.datadrum.com/main.php?package={id}";
// polygonTemplate.urlTarget = "_blank";

var graticuleSeries = chart.series.push(new am4maps.GraticuleSeries());
graticuleSeries.mapLines.template.line.stroke = am4core.color("#ffffff");
graticuleSeries.mapLines.template.line.strokeOpacity = 0.08;
graticuleSeries.fitExtent = false;


chart.backgroundSeries.mapPolygons.template.polygon.fillOpacity = 0.1;
chart.backgroundSeries.mapPolygons.template.polygon.fill = am4core.color("#ffffff");

// Create hover state and set alternative fill color
var hs = polygonTemplate.states.create("hover");
hs.properties.fill = chart.colors.getIndex(0).brighten(-0.5);

let animation;
setTimeout(function () {
  animation = chart.animate({ property: "deltaLongitude", to: 100000 }, 20000000);
}, 500)

chart.seriesContainer.events.on("down", function () {
  //  animation.stop();
})




//shout out css tricks "in page filtered search with vanilla javascript 
// and JT Homie for the help with this section"
let cards = document.querySelectorAll('.box')
    
function liveSearch() {
    let search_query = document.getElementById("searchbox").value;
    
    //Use innerText if all contents are visible
    //Use textContent for including hidden elements
    for (var i = 0; i < cards.length; i++) {
        if(cards[i].textContent.toLowerCase()
                .includes(search_query.toLowerCase())) {
            cards[i].classList.remove("is-hidden");
        } else {
            cards[i].classList.add("is-hidden");
        }
    }
}

//A little delay
let typingTimer;               
let typeInterval = 500;  
let searchInput = document.getElementById('searchbox');

searchInput.addEventListener('keyup', () => {
    clearTimeout(typingTimer);
    typingTimer = setTimeout(liveSearch, typeInterval);
});



var CALENDAR_URL = "https://date.nager.at/api/v3/NextPublicHolidays/"

var countrySearchInput = document.getElementById("myCheck")

function getCountries(event) {
  event.preventDefault();
  var countryCode = document.querySelector("#queryCountries").value;
  countrySearchInput.innerHTML
  fetch("https://date.nager.at/api/v3/NextPublicHolidays/" + countryCode)
    .then(response => response.json())
    .then(coderData => console.log(coderData))
    .catch(err => console.log(err))
}


function showPassword() {
  var x = document.getElementById("password");
  if (x.type === "password") {
    x.type = "text";
    console.log("i am text now")
  } else {
    x.type = "password";
    console.log("i am password now")
  }
}


function showPassword2() {
  var x = document.getElementById("conf_password");
  if (x.type === "password") {
    x.type = "text";
    console.log("i am text now")
  } else {
    x.type = "password";
    console.log("i am password now")
  }
}









