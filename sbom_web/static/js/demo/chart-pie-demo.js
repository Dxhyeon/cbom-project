//1 myPieChart
Chart.pluginService.register({
  beforeDraw: function(chart) {
    if (chart.config.options.elements.center) {
      // Get ctx from string
      var ctx = chart.chart.ctx;

      // Get options from the center object in options
      var centerConfig = chart.config.options.elements.center;
      var fontStyle = centerConfig.fontStyle || 'Arial';
      var txt = centerConfig.text;
      var color = centerConfig.color || '#000';
      var maxFontSize = centerConfig.maxFontSize || 75;
      var sidePadding = centerConfig.sidePadding || 20;
      var sidePaddingCalculated = (sidePadding / 10) * (chart.innerRadius * 2)
      // Start with a base font of 30px
      ctx.font = "30px " + fontStyle;

      // Get the width of the string and also the width of the element minus 10 to give it 5px side padding
      var stringWidth = ctx.measureText(txt).width;
      var elementWidth = (chart.innerRadius * 2) - sidePaddingCalculated;

      // Find out how much the font can grow in width.
      var widthRatio = elementWidth / stringWidth;
      var newFontSize = Math.floor(30 * widthRatio);
      var elementHeight = (chart.innerRadius * 2);

      // Pick a new font size so it will not be larger than the height of label.
      var fontSizeToUse = Math.min(newFontSize, elementHeight, maxFontSize);
      var minFontSize = centerConfig.minFontSize;
      var lineHeight = centerConfig.lineHeight || 25;
      var wrapText = false;

      if (minFontSize === undefined) {
        minFontSize = 20;
      }

      if (minFontSize && fontSizeToUse < minFontSize) {
        fontSizeToUse = minFontSize;
        wrapText = true;
      }

      // Set font settings to draw it correctly.
      ctx.textAlign = 'center';
      ctx.textBaseline = 'middle';
      var centerX = ((chart.chartArea.left + chart.chartArea.right) / 2) + 6;
      var centerY = ((chart.chartArea.top + chart.chartArea.bottom) / 2);
      ctx.font = fontSizeToUse + "px " + fontStyle;
      ctx.fillStyle = color;

      if (!wrapText) {
        ctx.fillText(txt, centerX, centerY);
        return;
      }

      var words = txt.split(' ');
      var line = '';
      var lines = [];

      // Break words up into multiple lines if necessary
      for (var n = 0; n < words.length; n++) {
        var testLine = line + words[n] + ' ';
        var metrics = ctx.measureText(testLine);
        var testWidth = metrics.width;
        if (testWidth > elementWidth && n > 0) {
          lines.push(line);
          line = words[n] + ' ';
        } else {
          line = testLine;
        }
      }

      // Move the center up depending on line height and number of lines
      centerY -= (lines.length / 2) * lineHeight;

      for (var n = 0; n < lines.length; n++) {
        ctx.fillText(lines[n], centerX, centerY);
        centerY += lineHeight;
      }
      //Draw text in center
      ctx.fillText(line, centerX, centerY);
    }
  }
});

if (vulCount == 0) {
  var a = 0;
} else {
  a = (vulCount / packageStatistics * 100).toFixed(2);
}

if (licenseCount == 0) {
  var b = 0;
} else {
  b = 0;
}

var config = {
type: 'doughnut',
data: {
labels: [
  "Vulnerability",
  "Packages"
],
datasets: [{
  data: [vulCount, packageStatistics],
  backgroundColor: [
    "#e74a3b",
    "#4e73df"
  ],
}]
},
options: {
elements: {
  center: {
    text: a.toString()+"%",
    color: '#e74a3b', // Default is #000000
    fontStyle: 'Arial', // Default is Arial
    sidePadding: 20, // Default is 20 (as a percentage)
    minFontSize: 37, // Default is 20 (in px), set to false and text will not wrap.
    lineHeight: 25 // Default is 25 (in px), used for when text wraps
  }
},
legend: {
  display: false
},
cutoutPercentage: 65,

}
};

var config2 = {
  type: 'doughnut',
  data: {
  labels: [
    "Conflict",
    "License"
  ],
  datasets: [{
    data: [0, licenseCount],
    backgroundColor: [
      "#f6c23e",
      "#1cc88a"
    ],
    hoverBackgroundColor: [
      "#f6c23e",
      "#1cc88a"
    ]
  }]
  },
  options: {
  elements: {
    center: {
      text: b.toString()+"%",
      color: '#f6c23e', // Default is #000000
      fontStyle: 'Arial', // Default is Arial
      sidePadding: 20, // Default is 20 (as a percentage)
      minFontSize: 20, // Default is 20 (in px), set to false and text will not wrap.
      lineHeight: 25 // Default is 25 (in px), used for when text wraps
    },
  },
  legend: {
    display: false
  },
  }
  };

var ctx = document.getElementById("myPieChart").getContext("2d");
var myPieChart = new Chart(ctx, config);

//var ctx2 = document.getElementById("myPieChart2").getContext("2d");
//var myPieChart2 = new Chart(ctx2, config2);
