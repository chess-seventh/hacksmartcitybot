/**
 * Created by oritlewski on 13.05.17.
 */
$(function () {

  var exemple_data = {
    'bike' : {
      name: "bike",
      dataPoints: [
        { "1 Jan 2015": 25987.50},
        { "1 Feb 2015": 23436.00},
        { "1 Mar 2015": 29988.00},
      ]
    },
    'car' : {
      name: "car",
      dataPoints: [
        { "1 Jan 2015": 22000.50},
        { "1 Feb 2015": 21436.00},
        { "1 Mar 2015": 29388.00},
      ]
    }
  }
  console.log()


  var chartsContainers =  $('.chart');

  var chart_name = 'transport-comparison';

// CanvasJS spline area chart to show revenue from Jan 2015 - Dec 2015
  var revenueSplineAreaChart = new CanvasJS.Chart(chart_name + "-chart", {
    animationEnabled: true,
    backgroundColor: "transparent",
    axisX: {
      interval: 2,
      intervalType: "month",
      labelFontColor: "#717171",
      labelFontSize: 16,
      lineColor: "#a2a2a2",
      minimum: new Date("1 Jan 2015"),
      tickColor: "#a2a2a2",
      valueFormatString: "MMM YYYY"
    },
    axisY: {
      gridThickness: 0,
      includeZero: false,
      labelFontColor: "#717171",
      labelFontSize: 16,
      lineColor: "#a2a2a2",
      prefix: "",
      tickColor: "#a2a2a2"
    },
    toolTip: {
      borderThickness: 0,
      cornerRadius: 0,
      fontStyle: "normal"
    },

    data: [
      {
        type: "splineArea",
        color: "#B36491",
        showInLegend: true,
        legendText: "SOFT MOBILITY",
        fillOpacity: .1,
        lineThickness: 2,
        dataPoints: [
          { x: new Date("1 Jan 2015"), y: 250 },
          { x: new Date("1 Feb 2015"), y: 300 },
          { x: new Date("1 Mar 2015"), y: 200 },
          { x: new Date("1 Apr 2015"), y: 900 },
          { x: new Date("1 May 2015"), y: 800 },
          { x: new Date("1 Jun 2015"), y: 500 },
          { x: new Date("1 Jul 2015"), y: 400 },
          { x: new Date("1 Aug 2015"), y: 300 },
          { x: new Date("1 Sep 2015"), y: 250 },
          { x: new Date("1 Oct 2015"), y: 600 },
          { x: new Date("1 Nov 2015"), y: 500 },
          { x: new Date("1 Dec 2015"), y: 600 }
        ]
      },
      {
        type: "splineArea",
        color: "#6DCFF6",
        showInLegend: true,
        legendText: "CAR",
        fillOpacity: .3,
        dataPoints: [
          { x: new Date("1 Jan 2015"), y:333 },
          { x: new Date("1 Feb 2015"), y:566 },
          { x: new Date("1 Mar 2015"), y:555 },
          { x: new Date("1 Apr 2015"), y:700 },
          { x: new Date("1 May 2015"), y:800 },
          { x: new Date("1 Jun 2015"), y:300 },
          { x: new Date("1 Jul 2015"), y:400 },
          { x: new Date("1 Aug 2015"), y:300 },
          { x: new Date("1 Sep 2015"), y:300 },
          { x: new Date("1 Oct 2015"), y:400 },
          { x: new Date("1 Nov 2015"), y:300 },
          { x: new Date("1 Dec 2015"), y:300 }
        ]
      }
    ]
  });

  revenueSplineAreaChart.render();


  $.each(chartsContainers, function(i, v) {
    console.log(v.data("chart"));
  });

});