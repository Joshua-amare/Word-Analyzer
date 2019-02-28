
// input test data
obj =  [
            { label: "muh", y: 18 },
            { label: "don't care", y: 29 },
            { label: "what", y: 40 },
            { label: "seriousy", y: 34 },
            { label: "shwang", y: 24 },
	    { label: "n-word", y: 34 },
            { label: "blue boy", y: 24 }
    ];
// calling jason object to javascript object obj
// jason needs the format [ { label: "cake", y: 18 }, { label: "juice", y: 29 }]
// once done with json file uncomment the following line and it shall work as intended
/*var text, obj, color_val, color_array;
    text = localStorage.getItem("json name");
    obj = JSON.parse(text);
*/
window.onload = function () {

    var chart = new CanvasJS.Chart("chartContainer");

    chart.options.axisY = { prefix: "$", suffix: "K" };
    chart.options.title = { text: "The Word Frequency data presented in a bar-chart" };

    var series1 = { //dataSeries 
        type: "column",
        name: "Word Data",
        showInLegend: true
    };


    chart.options.data = [];
    chart.options.data.push(series1);



    series1.dataPoints = obj;


    chart.render();
}
